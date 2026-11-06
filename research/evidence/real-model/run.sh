S=__SCRATCH__
export no_proxy="*" NO_PROXY="*" PATH=$S/tools/go/bin:$PATH GOCACHE=$S/gocache GOPATH=$S/gopath TIKTOKEN_CACHE_DIR=$S/bpe GOFLAGS=-mod=mod GOLD=$S/real/gold.md
cd $S/hxg; timeout 1200 $S/venv-g/bin/python go7.py $S/hxg/run gold,gold.md,8192 > $S/real/helix.out 2>&1
K=internal/ingestion/component/knowledge_compiler
cd $S/upstream/ragflow
timeout 1500 go test -count=1 -timeout 1500s -run "TestRealClaims" -v ./$K/tree 2>&1 | grep -v -E "^\{|zap" > $S/real/rf_claims.out
timeout 1500 go test -count=1 -timeout 1500s -run "TestRealGraph" -v ./$K/structure 2>&1 | grep -v -E "^\{|zap" > $S/real/rf_graph.out
rm -f $K/structure/h_real_test.go $K/tree/h_real_test.go
echo done > $S/real/DONE
