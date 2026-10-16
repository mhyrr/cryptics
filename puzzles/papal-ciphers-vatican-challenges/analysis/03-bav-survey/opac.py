import urllib.request,urllib.parse,http.cookiejar,re,sys,json
cj=http.cookiejar.CookieJar(); op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
H={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15","Accept":"text/html","Accept-Language":"en-US,en;q=0.9","Referer":"https://opac.vatlib.it/mss/"}
op.open(urllib.request.Request("https://opac.vatlib.it/mss/",headers=H),timeout=40).read()
def search(q,page=1,r=100):
    u="https://opac.vatlib.it/mss/search?"+urllib.parse.urlencode({"sm":"os","k_v":q,"k_f":"0","r":r,"p":page})
    return op.open(urllib.request.Request(u,headers=H),timeout=90).read().decode('utf-8','ignore')
def count(b):
    m=re.search(r'emphasise-number">(\d+)</span>\s*results found',b); return int(m.group(1)) if m else 0
if __name__=="__main__":
    for q in sys.argv[1:]:
        b=search(q,r=10); print(count(b),'\t',q)
