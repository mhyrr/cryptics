import re,html,json,sys
from opac import search,count
terms=["cifra","cifre","cifrario","cifrari","decifrato","decifrata","decifrate","decifrati","decifrazione","decifrazioni","cifrata","cifrate","cifrati","deciferazione","chiffre","chiffres","chiffrée","déchiffrement","cipher","ciphers","ziffer","zifre","ciffra","crittografia","cryptographia","steganographia","steganografia","occultis litteris","notis arcanis","alfabeto segreto","caratteri segreti","contrasegni","dicifera","diciferato","diciferata","diciferate","cifera","cifere","zifera"]
recs={}
for q in terms:
    b=search(q,r=100); n=count(b)
    print(n,q,file=sys.stderr)
    pages=[b]
    for p in range(2,(n+99)//100+1): pages.append(search(q,page=p,r=100))
    for b in pages:
        # split into items at each 'Manuscript' label preceding detail link
        for m in re.finditer(r'href="/mss/detail/([^"]+)"',b):
            sid=html.unescape(m.group(1))
            if sid.isdigit(): continue
            seg=b[m.start():m.start()+6000]
            nxt=re.search(r'href="/mss/detail/(?!\d)',seg[10:])
            if nxt: seg=seg[:nxt.start()+10]
            t=re.sub(r'<[^>]+>','\n',seg); t=html.unescape(re.sub(r'\n\s*\n+','\n',t)).strip()
            r=recs.setdefault(sid,{"terms":set(),"text":t[:1500]})
            r["terms"].add(q)
for v in recs.values(): v["terms"]=sorted(v["terms"])
json.dump(recs,open('opac-cipher-hits.json','w'),ensure_ascii=False,indent=1)
print(len(recs),'unique shelfmarks')
