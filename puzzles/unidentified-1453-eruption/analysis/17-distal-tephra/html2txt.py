"""Print the visible text of a saved HTML page, one table row per line.
Run: python3 -I html2txt.py data/<file>.html"""
import html, re, sys

t = open(sys.argv[1], encoding='latin-1').read()
t = re.sub(r'<(script|style).*?</\1>', '', t, flags=re.S)
t = re.sub(r'<(tr|br|p|h\d|li)[^>]*>', '\n', t, flags=re.I)
t = re.sub(r'<[^>]+>', ' | ', t)
t = html.unescape(re.sub(r'[ \t]+', ' ', t))
t = re.sub(r'(\| *)+', '| ', t)
print('\n'.join(l.strip() for l in t.split('\n') if l.strip(' |\r')))
