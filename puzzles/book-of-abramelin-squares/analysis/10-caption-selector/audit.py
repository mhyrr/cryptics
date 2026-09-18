"""Reproduce E1 freezes, sample selection and input audit; no historical scoring."""
import argparse
import hashlib
import json
from pathlib import Path
from recipe import occurs, tokens, select

HERE = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def audit():
    for name in ['freeze.json', 'lexicon-freeze.json']:
        for f, expected in json.loads((HERE / name).read_text())['files'].items():
            assert sha(HERE / f) == expected, f'Frozen file changed: {f}'
    images = json.loads((HERE / 'images.json').read_text())
    for image in images:
        assert sha(HERE / image['file']) == image['sha256'], image['file']
    selection = json.loads((HERE / 'sample-selection.json').read_text())
    excluded = {s+d for s in selection['previously_acquired_scans'] for d in [-1, 0, 1]}
    starts = [s for s in range(55, 1153) if s not in excluded and s+1 not in excluded]
    digest = hashlib.sha256(selection['seed'].encode()).hexdigest()
    start = starts[int(digest, 16) % len(starts)]
    assert selection['selected_scans'] == [start, start+1]
    assert selection['seed_sha256'] == digest
    assert selection['recipe_freeze_sha256'] == sha(HERE / 'freeze.json')
    lexicon = json.loads((HERE / 'lexicon.json').read_text())['records']
    # Domain availability is not a caption match. Probe with each entry's own
    # headword solely to expose length/alphabet exclusions, clearly separated.
    domains = []
    for e in lexicon:
        runs = {str(n): select(e['headword_raw'], n, [e]) for n in range(3, 26, 2)}
        domains.append({'id': e['id'], 'has_transliteration': bool(e['words']),
                        'uncertain': e['uncertain'],
                        'eligible_domains': {n: r['words'] for n, r in runs.items() if r['words']},
                        'exclusions_across_sizes': sorted({tuple(x) for r in runs.values() for x in r['exclusions']})})
    discovery_source = HERE.parent / '06-construction-evidence/examples.json'
    discovery = []
    for e in json.loads(discovery_source.read_text())['examples']:
        if e['headword'] is None:
            continue
        discovery.append({'id': e['id'], 'caption': e['caption_display'],
                          'reported_headword': e['headword'],
                          'literal_match': occurs(tokens(e['headword']), tokens(e['caption_display']))})
    # Audit schema only; never pass grid letters into the selector or scorer.
    corpus_path = HERE.parent.parent / 'sources/mathers-squares.json'
    corpus = json.loads(corpus_path.read_text())['squares']
    fields = sorted({key for s in corpus for key in s})
    has_caption = any('caption' in key.lower() for key in fields)
    assert not has_caption, 'Caption schema changed; review input gate explicitly'
    return {'status': 'recipe_and_independent_lexicon_frozen; target_caption_alignment_missing',
            'historical_scores': None, 'historical_predictions': None,
            'historical_controls_run': False,
            'sample_scans': [start, start+1], 'sample_entries': len(lexicon),
            'entries_without_transliteration': sum(not e['words'] for e in lexicon),
            'uncertain_entries': sum(e['uncertain'] for e in lexicon),
            'caption_join_performed': False,
            'domain_probes_not_evaluation': domains,
            'discovery_only': {'source_sha256': sha(discovery_source),
                               'records': discovery,
                               'literal_matches': sum(e['literal_match'] for e in discovery)},
            'target_input_audit': {'corpus_sha256': sha(corpus_path), 'fields': fields,
                                   'has_caption_field': has_caption},
            'hashes': {f: sha(HERE / f) for f in ['PROTOCOL.md', 'recipe.py', 'test_recipe.py',
                       'freeze.json', 'sample-selection.json', 'images.json', 'lexicon.json',
                       'lexicon-freeze.json', 'audit.py']}}


def report(d):
    lines = ['# E1 input audit — no historical score', '',
             'A testable exploratory recipe and independent dictionary block are frozen.',
             'The historical run is blocked on source-backed German captions and target alignment.',
             'Controls were specified but not run; scores and predictions are null.', '',
             f"Sample: scans {d['sample_scans']}, {d['sample_entries']} entries; "
             f"{d['entries_without_transliteration']} have no Hebrew transliteration; "
             f"{d['uncertain_entries']} entry has an unresolved reading and abstains.", '',
             '| Entry | Eligible domains for odd n=3..25 (not caption matches) |', '|---|---|']
    for e in d['domain_probes_not_evaluation']:
        eligible = e['eligible_domains']
        lines.append(f"| {e['id']} | {json.dumps(eligible) if eligible else 'none'} |")
    lines += ['', '## Discovery diagnostic, kept out of evaluation', '',
              'Literal caption-to-reported-headword matching only. This does not test word',
              'placement, dictionary completeness, or square-letter recovery.', '',
              '| Example | Caption | Reported headword | Literal match |', '|---|---|---|---|']
    for e in d['discovery_only']['records']:
        lines.append(f"| {e['id']} | {e['caption']} | {e['reported_headword']} | {e['literal_match']} |")
    lines += ['', f"Literal matches: {d['discovery_only']['literal_matches']}/{len(d['discovery_only']['records'])} discovery associations.",
              'This is a limit of literal selection as a general explanation, not an independent success rate.', '',
              'No sampled entry has been declared absent from historical captions: the caption join',
              'has not occurred. Lexical exclusions, caption misses and alignment failures are distinct.', '',
              'The exact missing artifact is a caption-only table with German source text, locator,',
              'verified Mathers target ID, alignment evidence independent of letters, and exposure flags.',
              'English translation or square seeds cannot silently substitute for that input.', '']
    return '\n'.join(lines)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--check', action='store_true')
    args = p.parse_args()
    d = audit()
    for f, content in {'results.json': json.dumps(d, indent=2, ensure_ascii=False)+'\n',
                       'RESULTS.md': report(d)}.items():
        if args.check:
            assert (HERE / f).read_text() == content, f'Output changed: {f}'
        else:
            (HERE / f).write_text(content)
    print('E1 freezes and input audit verified; historical evaluation not run')
