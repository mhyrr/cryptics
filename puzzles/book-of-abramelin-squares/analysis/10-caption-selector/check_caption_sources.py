"""Bounded caption-input check on supplied PDFs; emit no square-letter rows."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
SOURCES = HERE.parent.parent / 'sources'


def run():
    files = json.loads((SOURCES / 'LOCAL-PDFS.json').read_text())['records']
    out = {'scope': 'Text-layer input availability check, not a square comparison or historical score.',
           'visual_check': 'Edition PDF page 125 rendered and inspected: blank LESEPROBE leaf.',
           'terms': ['Dolmetschen', 'Dolmetſchen', 'Dolmetschung', 'Dolmetſchung'],
           'caveat': 'Zero text-layer hits do not prove absence from unprovided captions or facsimiles.',
           'records': []}
    for name in ['lp_wp.pdf', 'buchstabenquadrate.pdf']:
        p = SOURCES / name
        digest = hashlib.sha256(p.read_bytes()).hexdigest()
        assert digest == next(r['sha256'] for r in files if r['file'] == name)
        text = subprocess.check_output(['pdftotext', '-layout', str(p), '-'], text=True)
        pages = text.split('\f')
        r = {'file': name, 'sha256': digest,
             'text_layer_term_pages': {term: [i+1 for i, page in enumerate(pages)
                       if term.casefold() in page.casefold()] for term in out['terms']}}
        if name == 'lp_wp.pdf':
            r['boundary_headers'] = {str(i+1): next((x.strip() for x in pages[i].splitlines() if x.strip()), '')
                                     for i in [119, 120, 121, 122, 123, 124, 125, 126]}
        out['records'].append(r)
    return out


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    content = json.dumps(run(), ensure_ascii=False, indent=2)+'\n'
    p = HERE / 'caption-source-audit.json'
    if args.check:
        assert p.read_text() == content
    else:
        p.write_text(content)
    print('Supplied-source caption audit verified; no square rows emitted')
