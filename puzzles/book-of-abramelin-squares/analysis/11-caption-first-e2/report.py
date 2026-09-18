"""Render the checked-in E2 result without exposing hidden letters."""
import argparse
from evaluate import read, save


def report():
    d, tasks = read('results.json'), read('tasks.json')
    lines = ['# E2 results — uninformative caption-selector pilot', '',
        '**No evidence for a caption selector.** E2 made no predictions on the',
        'three complete aligned targets. Their caption lookups never supplied a',
        'usable word domain. Accuracy is undefined, not 0% or 100%. This tests the',
        'operational coverage of the narrow procedure; it does not reject semantic',
        'selection, dictionary derivation, or a different placement.', '',
        f"Inputs: {d['captions']} consecutive German captions; {d['aligned']} purpose-label alignments; "
        f"{d['complete_odd_targets']} complete odd Mathers targets.",
        'Lookups: ' + ', '.join(f'{v} {k}' for k,v in d['lookup_status_counts'].items()) + '.', '',
        '## Every sampled caption remains in the ledger', '',
        '| German caption ID | Mathers label | Size | Complete | Selection | Evaluation exclusion |',
        '|---|---|---:|---|---|---|']
    for r in tasks['ledger']:
        lines.append(f"| {r['caption_id']} | {r['target_id'] or 'unmatched'} | {r['n'] or '—'} | "
            f"{r['complete']} | {r['selection']['status'] if r['selection'] else 'not joined'} | "
            f"{', '.join(r['evaluation_exclusions']) or 'none; model may abstain'} |")
    lines += ['', '## All-interior mask', '',
        'Each of three 5×5 targets contributes nine hidden cells in three whole D4',
        'groups. All comparisons use these same targets; all have prior internal',
        'Mathers exposure. There is no untouched-witness stratum.', '',
        '| Method | Correct | Errors | Predicted / hidden | Exact tasks | Contradictions |',
        '|---|---:|---:|---:|---:|---:|']
    for r in d['scores']:
        if r['variant']=='original' and r['mask_kind']=='all_interior' and 'shuffle' not in r['method']:
            lines.append(f"| {r['method']} | {r['correct']} | {r['errors']} | {r['predicted']} / {r['target_cells']} | {r['exact_tasks']} | {r['contradictions']} |")
    lines += ['', '## One whole interior D4 group at a time', '',
        '| Method | Correct | Errors | Predicted / hidden | Correct groups | Wrong groups | Abstained groups |',
        '|---|---:|---:|---:|---:|---:|---:|']
    for r in d['scores']:
        if r['variant']=='original' and r['mask_kind']=='one_inner_orbit' and 'shuffle' not in r['method']:
            lines.append(f"| {r['method']} | {r['correct']} | {r['errors']} | {r['predicted']} / {r['target_cells']} | {r['correct_groups']} | {r['wrong_groups']} | {r['abstained_groups']} |")
    controls = [r for r in d['scores'] if 'shuffle' in r['variant'] or 'shuffle' in r['method']]
    lines += ['', '## Controls and interpretation', '',
        f"All {len(controls)} control/mask summary rows have zero caption predictions.",
        'Twenty within-size caption permutations ran. The unchanged-caption counts',
        'are `' + str([r['unchanged'] for r in d['caption_permutations']]) + '`.',
        'All three complete originals are T-compatible and enter the twenty',
        'orbit-value permutations; their matched original rows are saved separately.',
        'Word-letter controls have empty selected domains and are explicitly vacuous.',
        'Changing captions cannot fix an unresolved lookup under this procedure.', '',
        'Baseline comparisons on the caption-predicted subset have denominator zero.',
        'The caption-free pool includes all five retrieved relevant-sense entries,',
        'including spelling-excluded caption joins. Its no-prediction outcome here',
        'is contradiction, whereas the caption model abstains before placement.',
        'These different failure modes must not be presented as equivalent models.',
        'Dictionary positional-frequency guesses do not use captions; their limited',
        'matches are not evidence for a selector. No complete square was recovered.', '',
        '## What this run can and cannot tell us', '',
        'The sampled source solves the caption-access problem for this pilot. The',
        'strict lookup policy does not solve usable lexical input. Six searches are',
        'unresolved, not verified absences. Three found headwords need unpermitted',
        'German spelling changes. The three -gestalt compounds were not split.',
        'The unmatched giant and four incomplete aligned targets remain recorded.', '',
        'Do not broaden spelling, split compounds, drop an unresolved alternative,',
        'or redraw captions inside E2. Use these as development observations for a',
        'separately frozen E3 on a new cohort. No incomplete-square witness stage',
        'is justified. H7/H12/H15 remain open; E1 and H14 are unchanged.', '',
        'See [README](README.md), [protocol](PROTOCOL.md), [exposure audit](EXPOSURE.md),',
        '[lexicon](lexicon.json), [per-task results](results.json), and the complete',
        '[frozen per-cell predictions](predictions.json).', '']
    return '\n'.join(lines)


if __name__ == '__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
    from pathlib import Path
    path=Path(__file__).with_name('RESULTS.md')
    content=report()
    if args.check: assert path.read_text()==content
    else: path.write_text(content)
    print('E2 report verified.' if args.check else 'E2 report written.')
