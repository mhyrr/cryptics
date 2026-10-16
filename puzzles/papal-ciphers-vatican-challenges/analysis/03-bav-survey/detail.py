import re,html,sys,time
from opac import op,H
import urllib.request
def detail(s):
    b=op.open(urllib.request.Request("https://opac.vatlib.it/mss/detail/"+s,headers=H),timeout=90).read().decode('utf-8','ignore')
    b=re.sub(r'<(script|style).*?</\1>','',b,flags=re.S)
    t=re.sub(r'<[^>]+>','\n',b); t=html.unescape(re.sub(r'[ \t]+',' ',t)); t=re.sub(r'\n\s*\n+','\n',t)
    return t
for s in sys.argv[1:]:
    t=detail(s); open(f'detail-{s}.txt','w').write(t)
    lines=[l.strip() for l in t.split('\n')]
    hits=[i for i,l in enumerate(lines) if re.search(r'cifr|chiffr|decif|zifr|occult',l,re.I)]
    print('=====',s,len(t))
    shown=set()
    for i in hits[:12]:
        for j in range(max(0,i-3),min(len(lines),i+2)):
            if j not in shown: print('  ',lines[j][:220]); shown.add(j)
        print('   --')
    time.sleep(1.5)
