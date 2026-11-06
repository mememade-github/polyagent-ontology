import random,sys
ko=" ".join(f"제{i}조 임차인은 계약 만료 {i}일 전까지 임대인에게 서면으로 갱신 의사를 통지하여야 한다." for i in range(1,201))
open('long_noheading.txt','w').write((ko+"\n\n")*10)          # ~105k chars, paragraphs, no heading
open('long_oneparagraph.txt','w').write(ko*10)                 # no newline at all
sec="\n\n".join(f"## 장 {n}\n\n"+" ".join(f"제{n}-{i}조 Jane Doe promised Globex a {i}% service credit." for i in range(1,60)) for n in range(1,41))
open('long_sections.md','w').write("# 표준 약관\n\n"+sec)
