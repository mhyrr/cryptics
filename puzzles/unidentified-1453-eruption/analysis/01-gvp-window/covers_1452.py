import csv,sys
rows=list(csv.DictReader(open(sys.argv[1],encoding='utf-8')))
print([ (r['StartDateYear'],r['StartDateYearUncertainty'],r['ExplosivityIndexMax'],r['StartEvidenceMethod'],r['ActivityUnit']) for r in rows if r['Volcano_Name'] in('Kuwae',)])
print('\nCovers 1452 (year±unc), VEI>=4 or unknown:')
n=0
for r in rows:
    if not r['StartDateYear']: continue
    y=int(r['StartDateYear']); u=int(r['StartDateYearUncertainty'] or 0)
    if y-u<=1452<=y+u and u>0 and (r['ExplosivityIndexMax']=='' or int(r['ExplosivityIndexMax'])>=4):
        n+=1;print(r['Volcano_Name'],y,'±',u,'VEI',r['ExplosivityIndexMax'] or '?',r['GeoLocation'],r['StartEvidenceMethod'],r['ActivityUnit'][:30])
print(n)
