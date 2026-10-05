"""Serial, throttled fetch of whole native pages (one request per page) for exp 06. Waits until Gallica answers.
Page = (folio label, canvas, side). Left page x 0..W/2+150, right page W/2-150..W (W from the manifest).
Exp 07 (H17): `python3 fetch_pages.py spreads` fetches whole spreads c197..c288 (one request per canvas, saved
as spreads/cNNN.jpg); `split_spreads.py` cuts them into folio pages locally after the folio numbers are checked."""
import urllib.request, json, time, os, sys
M = json.load(open("../manifest.json"))["sequences"][0]["canvases"]
PAGES = [("f003r",5,"R"),("f003v",6,"L"),("f004r",6,"R"),
         ("f011r",13,"R"),("f011v",14,"L"),("f012r",14,"R"),("f012v",15,"L"),
         ("f017r",19,"R"),("f017v",20,"L"),("f018r",20,"R"),("f018v",21,"L"),("f019r",21,"R"),("f019v",22,"L"),("f020r",22,"R"),("f020v",23,"L"),
         ("f022r",24,"R"),("f022v",25,"L"),("f023r",25,"R"),("f023v",26,"L"),("f024r",26,"R"),("f024v",27,"L"),("f025r",27,"R"),
         ("f026r",28,"R"),("f029L",29,"L"),
         ("f032r",29,"R"),("f032v",30,"L"),("f033r",30,"R"),
         ("f034r",31,"R"),("f034v",32,"L"),("f035r",32,"R"),
         ("f005r",7,"R"),("f007r",9,"R"),("f009r",11,"R"),("f014r",16,"R"),("f015r",17,"R"),
         ("f006r",8,"R"),("f006v",9,"L"),("f007v",10,"L"),("f015v",18,"L")]
def get(url, out):
    r = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (research; one request per 20 s)"})
    data = urllib.request.urlopen(r, timeout=180).read()
    open(out, "wb").write(data); return len(data)
probe = "https://gallica.bnf.fr/iiif/ark:/12148/btv1b10032556x/f5/0,0,200,200/full/0/native.jpg"
while True:
    try:
        get(probe, "probe.jpg"); print("gallica up", flush=True); break
    except Exception as e:
        print("waiting:", type(e).__name__, flush=True); time.sleep(300)
SPREADS = list(range(197, 289))
if len(sys.argv) > 1 and sys.argv[1] == "spreads":
    os.makedirs("spreads", exist_ok=True)
    PAGES = [(f"spreads/c{c:03d}", c, "F") for c in SPREADS]
for name, c, side in PAGES:
    out = f"{name}.jpg"
    if os.path.exists(out) and os.path.getsize(out) > 100000:
        continue
    W, H = M[c-1]["width"], M[c-1]["height"]
    x0, x1 = {"L": (0, W//2 + 150), "R": (W//2 - 150, W), "F": (0, W)}[side]
    url = f"https://gallica.bnf.fr/iiif/ark:/12148/btv1b10032556x/f{c}/{x0},0,{x1-x0},{H}/full/0/native.jpg"
    for k in range(6):
        try:
            n = get(url, out); print(f"ok {name} {n}", flush=True); break
        except Exception as e:
            print(f"fail {name} {type(e).__name__}; sleep {120*(k+1)}", flush=True); time.sleep(120*(k+1))
    time.sleep(20)
print("done", flush=True)
