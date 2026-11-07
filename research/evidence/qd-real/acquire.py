"""Single authorized acquisition. No retries, tuning, judging or threshold changes."""
from pathlib import Path
import sys,json,time,hashlib,shutil,datetime,subprocess,os
P=Path(__file__).parent
W=Path('__RESEARCH__')
sys.path.insert(0,str(W/'prototype/qd'))
import scientific as s
OUT=P/'acquisition'
OUT.mkdir(exist_ok=False)
lock=json.loads((P/'execution-lock.json').read_text())
for path,digest in lock['files'].items():
 if hashlib.sha256(Path(path).read_bytes()).hexdigest()!=digest:raise RuntimeError('lock mismatch')
units=json.loads((P/'units-final.json').read_text())
digest=json.loads((P/'model.json').read_text())['digest'];endpoint=(P/'endpoint.txt').read_text().strip()
start=time.monotonic();deadline=start+1800
manifest=[];controls=[];abort=None

def persist(name,value):
 with (OUT/name).open('x') as f:json.dump(value,f,ensure_ascii=False,indent=2)

def acquire(name,seed,arm=None):
 if shutil.disk_usage('/workspaces').free<2_000_000_000:raise RuntimeError('disk floor')
 left=deadline-time.monotonic()
 if left<=0:raise RuntimeError('global deadline')
 driver=s.Driver(endpoint,digest,seed,OUT/name,global_deadline=deadline)
 try:result=s.execute(units,driver,arm) if arm else s.controls(driver)
 finally:driver.raw.close()
 with (OUT/name/'result.json').open('x') as f:json.dump(result,f,ensure_ascii=False,indent=2)
 if not arm:controls.append({'phase':name,'path':str(OUT/name/'result.json'),'status':result['status']})
 else:manifest.append({'arm':arm,'seed':seed,'path':str(OUT/name/'result.json')})
 print(json.dumps({'completed':name,'status':result['status'],'attempts':result['accounting']['attempts'],'actual_tokens':result['accounting']['actual_tokens'],'wall_seconds':result['accounting']['wall_seconds']},ensure_ascii=False),flush=True)
 if time.monotonic()>deadline:raise RuntimeError('global deadline')
 if result.get('error_type') or (arm and result['status']!='complete'):raise RuntimeError('accounting or arm abort')
 return result

try:
 try:
  acquire('pre-controls',7)
  arms=['onto','original-random','original-coverage','fact-random','fact-coverage']
  for index,seed in enumerate([7,11,19]):
   order=arms[index:]+arms[:index]
   for arm in order:acquire(str(seed)+'-'+arm,seed,arm)
  acquire('post-controls',7)
 except BaseException as exc:
  abort={'error_type':type(exc).__name__,'reason':str(exc) if type(exc) is RuntimeError else 'unexpected failure'}
  print(json.dumps({"acquisition_error":abort}),file=sys.stderr,flush=True)
 try:
  elapsed=time.monotonic()-start
  persist('manifest.json',manifest)
  persist('controls-manifest.json',controls)
  persist('acquisition-summary.json',{'utc_finished':datetime.datetime.now(datetime.timezone.utc).isoformat(),'wall_seconds':elapsed,'limit_seconds':1800,'abort':abort,'completed_arms':len(manifest),'completed_control_batches':len(controls),'total_clock_scope':'before precontrol driver initialization through elapsed timestamp after postcontrol and arm I/O; includes setup, queue, controller and inter-arm I/O; excludes subsequent manifest/summary writes and cleanup'})
  print(json.dumps({'acquisition_complete':abort is None,'completed_arms':len(manifest),'wall_seconds':elapsed,'abort':abort}),flush=True)
 except BaseException:
  if abort is None:raise
  import traceback
  traceback.print_exc()
finally:
 # Parent collects logs from this stopped container, then removes it.
 try:
  stop=subprocess.run(["docker","stop","--time","10","ollama-t"],capture_output=True,text=True,timeout=20)
  cleanup={"cleanup_stop_exit":stop.returncode,"stderr":stop.stderr}
 except subprocess.TimeoutExpired:
  cleanup={"cleanup_stop_timeout_seconds":20}
 except BaseException as exc:
  cleanup={"cleanup_stop_error_type":type(exc).__name__}
 print(json.dumps(cleanup),file=sys.stderr,flush=True)
if abort is not None:sys.exit(1)
if cleanup.get("cleanup_stop_exit")!=0:sys.exit(1)
