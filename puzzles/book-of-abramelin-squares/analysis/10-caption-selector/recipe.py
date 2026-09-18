"""E1 caption-only selection and exact T completions. No answer-file access."""
import itertools
import string
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'stressbench'))
from common import orbits


def tokens(text):
    parts, current = [], ''
    for c in text.replace('ſ', 's').casefold():
        if c.isalpha():
            current += c
        elif current:
            parts.append(current)
            current = ''
    return parts + ([current] if current else [])


def occurs(phrase, caption):
    return bool(phrase) and any(caption[i:i + len(phrase)] == phrase
                               for i in range(len(caption) - len(phrase) + 1))


def select(caption, n, entries):
    """Entries have id, headword_raw, words (raw/joined), uncertain.

    joined is a source-verified line-join, never an inferred spelling repair.
    A caption is None unless its source and target alignment are verified.
    """
    result = {'status': None, 'matches': [], 'exclusions': [], 'words': []}
    if n < 3 or n % 2 == 0:
        result['status'] = 'ineligible_size'
        return result
    if caption is None:
        result['status'] = 'missing_caption'
        return result
    ts = tokens(caption)
    uncertain = False
    for entry in entries:
        if not any(occurs(tokens(a), ts) for a in entry['headword_raw'].split('/')):
            continue
        result['matches'].append(entry['id'])
        if entry['uncertain']:
            uncertain = True
            result['exclusions'].append([entry['id'], 'uncertain_entry'])
            continue
        if not entry['words']:
            result['exclusions'].append([entry['id'], 'no_transliteration'])
        for word in entry['words']:
            raw = word.get('joined', word['raw'])
            normalized = raw.replace('ſ', 's')
            normalized = ''.join(c.upper() if c in string.ascii_lowercase else c
                                 for c in normalized)
            reason = ('alphabet' if not normalized or any(c not in string.ascii_uppercase for c in normalized)
                      else 'length' if len(normalized) != n else None)
            if reason:
                result['exclusions'].append([entry['id'], word['raw'], reason])
            else:
                result['words'].append(normalized)
    result['words'] = sorted(set(result['words']))
    result['status'] = ('uncertain_input' if uncertain else
                        'sample_miss' if not result['matches'] else
                        'no_eligible_word' if not result['words'] else 'ready')
    if uncertain:
        result['words'] = []
    return result


def solve(observed, words, alphabet=string.ascii_uppercase):
    """All fixed-central-row lexical alternatives; untouched T orbits stay free."""
    n = len(observed)
    if n < 3 or n % 2 == 0 or any(len(row) != n for row in observed):
        raise ValueError('Expected odd square of size >=3')
    if not alphabet or len(set(alphabet)) != len(alphabet):
        raise ValueError('Invalid alphabet')
    if any(x is not None and x not in alphabet for row in observed for x in row):
        raise ValueError('Observed letter outside alphabet')
    if any(len(w) != n or any(c not in alphabet for c in w) for w in words):
        raise ValueError('Invalid word')
    os = orbits(n, 'transpose')
    lookup = {p: i for i, orbit in enumerate(os) for p in orbit}
    path = [(n // 2, c) for c in range(n)]
    branches = {}
    for word in sorted(set(words)):
        assigned = {}
        pairs = [(lookup[r, c], observed[r][c]) for r in range(n) for c in range(n)
                 if observed[r][c] is not None]
        pairs += [(lookup[p], ch) for p, ch in zip(path, word)]
        for i, letter in pairs:
            if i in assigned and assigned[i] != letter:
                break
            assigned[i] = letter
        else:
            key = tuple(sorted(assigned.items()))
            branches[key] = {'assigned': [[i, v] for i, v in key],
                             'free': [i for i in range(len(os)) if i not in assigned]}
    bs = list(branches.values())
    predictions = []
    for r, c in itertools.product(range(n), repeat=2):
        if observed[r][c] is not None or not bs:
            continue
        domains = [set(dict(b['assigned']).get(lookup[r, c], alphabet)) for b in bs]
        domain = set.union(*domains)
        if len(domain) == 1:
            predictions.append([r, c, next(iter(domain))])
    for b in bs:
        b['completions'] = len(alphabet) ** len(b['free'])
    return {'status': 'compatible' if bs else 'contradiction' if words else 'no_words',
            'orbits': os, 'free_domain': alphabet, 'branches': bs,
            'completion_count': sum(b['completions'] for b in bs),
            'predictions': predictions}
