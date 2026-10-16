"""page.py <shelfmark> <label> [label...]  -> pages/<shelf>_<label>.jpg (1400px wide)"""
import urllib.request,urllib.error,json,sys,os,time
UA={"User-Agent":"Mozilla/5.0"}
def get(u):
    for a in range(6):
        try: return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=120).read()
        except urllib.error.HTTPError as e:
            if e.code==429: time.sleep(20*(a+1)); continue
            raise
    raise SystemExit("rate limited: "+u)
s=sys.argv[1]; os.makedirs('pages',exist_ok=True)
mf=f'manifests/{s}.json'; os.makedirs('manifests',exist_ok=True)
if not os.path.exists(mf):
    open(mf,'wb').write(get(f"https://digi.vatlib.it/iiif/MSS_{s}/manifest.json"))
cv=json.load(open(mf))["sequences"][0]["canvases"]
lab={c["label"]:c for c in cv}
for want in sys.argv[2:]:
    c=lab.get(want)
    if not c: print('no label',want,[x["label"] for x in cv][:0]); continue
    svc=c["images"][0]["resource"]["service"]["@id"]
    out=f'pages/{s}_{want}.jpg'
    if not os.path.exists(out):
        open(out,'wb').write(get(f"{svc}/full/1400,/0/native.jpg")); time.sleep(2)
    print(out)
