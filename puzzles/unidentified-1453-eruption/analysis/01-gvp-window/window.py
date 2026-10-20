import csv,sys,re,collections
src,out=sys.argv[1],sys.argv[2]
rows=list(csv.DictReader(open(src,encoding='utf-8')))
sel=[r for r in rows if r['StartDateYear'] and 1400<=int(r['StartDateYear'])<=1500]
sel.sort(key=lambda r:int(r['StartDateYear']))
for r in sel:
    m=re.match(r'POINT \(([-\d.]+) ([-\d.]+)\)',r['GeoLocation']); r['lat'],r['lon']=(m.group(1),m.group(2)) if m else ('','')
f=list(sel[0].keys()); w=csv.DictWriter(open(out,'w',newline=''),fieldnames=f); w.writeheader(); w.writerows(sel)
print('total rows',len(rows),'1400-1500',len(sel))
win=[r for r in sel if 1420<=int(r['StartDateYear'])<=1490 and (r['ExplosivityIndexMax']=='' or int(r['ExplosivityIndexMax'])>=4)]
print('1420-1490 VEI>=4 or unknown:',len(win),' VEI>=4:',sum(1 for r in win if r['ExplosivityIndexMax']),' unknown:',sum(1 for r in win if not r['ExplosivityIndexMax']))
print('method counts',collections.Counter(r['StartEvidenceMethod'] for r in win))
for r in win:
    print('|',r['Volcano_Name'],'|',r['Volcano_Number'],'|',r['Activity_Type'],'|',r['StartDateYearModifier']+r['StartDateYear'],'±'+r['StartDateYearUncertainty'] if r['StartDateYearUncertainty'] else '','|',r['ExplosivityIndexMax'] or '?','|',r['lat'],r['lon'],'|',r['StartEvidenceMethod'],'|',r['ActivityUnit'][:40],'|')
