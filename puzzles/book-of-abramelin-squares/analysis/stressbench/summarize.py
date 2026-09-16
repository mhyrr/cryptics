"""Build the human report from checked per-case results; no manual arithmetic."""
from collections import Counter
import json

from common import ANALYSIS, HERE


EXPERIMENTS = ('02-frame-model', '03-fragment-transfer', '04-local-recurrence')


def main():
    data = {name[:2]: json.loads((ANALYSIS/name/'results.json').read_text())
            for name in EXPERIMENTS}
    manifest = json.loads((HERE/'manifest.json').read_text())
    selections = [
        ('02', 'Frame rules; scattered blanks', 'original|cells|frame_mdl'),
        ('02', 'Exact global symmetry; scattered blanks', 'original|cells|global_exact'),
        ('02', 'Frame rules; whole orbits hidden', 'original|orbits|frame_mdl'),
        ('03', 'Fragments; whole orbits hidden', 'original|orbits|fragments'),
        ('03', 'Fragments added after frames; scattered blanks', 'original|cells|fragments_added_after_frames'),
        ('04', 'Local rule; selected-corner boundary; modal rollout', 'original|selected_corner_boundary|modal_rollout'),
        ('04', 'Local rule; selected-corner boundary; confident rollout', 'original|selected_corner_boundary|confident_rollout'),
        ('04', 'Local rule; whole orbits hidden; modal rollout', 'original|orbits|modal_rollout'),
    ]
    lines = ['# Abramelin: three attacks under stress', '',
             'Generated from experiments 02–04. The frame model supplies useful candidate',
             'fills for scattered blanks. Fragment transfer and learned local recurrence',
             'do not provide reliable reconstruction of the independent letters.', '',
             'The [ten-attack plan](ATTACKS.md) was written before these runs. All tests',
             f"use the same {len(manifest['records'])} complete digital grids in {manifest['groups']} seed/orientation groups,",
             'with five fixed folds. These are internal tests on a previously inspected',
             'transcription, not German-witness validation or a decipherment.', '',
             '## Principal results', '',
             '| Method and target | Correct / predicted | Accuracy | Coverage | Frequency baseline correct on same cells | Exact tasks |',
             '|---|---:|---:|---:|---:|---:|']
    for experiment, label, key in selections:
        s = data[experiment]['summary'][key]
        accuracy = '—' if s['accuracy'] is None else f"{100*s['accuracy']:.1f}%"
        lines.append(f"| {label} | {s['correct']}/{s['predicted']} | {accuracy} | {100*s['coverage']:.1f}% | {s['baseline_correct_same_cells']} | {s['exact_tasks']}/{s['tasks']} |")
    damage = data['02']['corruption']['original|0']
    one = data['02']['corruption']['original|1']
    lines += ['', 'The frame method trades precision and exact task recovery for more cell',
              'predictions. Its success concerns letters with surviving geometric copies;',
              'it predicts none when every copy is hidden. The global comparator uses',
              'transpose plus half-turn symmetry and rejects visible contradictions.', '',
              f"On the unmodified export it flags {damage['suggested']} letters in {damage['grids']-damage['exact_grid']} grids.",
              'These are disagreements with the digital reading, not established scribal errors.',
              f"With one artificial substitution per grid, {one['correct']}/{one['suggested']} suggested repairs restore",
              f"the original letter; {one['collateral']} proposals change cells that were not corrupted.",
              'The method is unsuitable for automatic transcription correction.', '',
              'The recurrence result contains a small pooled gain over the frequency baseline,',
              'but no exact reconstruction and no confident predictions. The selected boundary',
              'comes from the traversal chosen on training data. It is not necessarily the',
              'top-left boundary, so it must not be compared directly with a different mask.', '',
              '## Negative controls', '',
              'Orbit-shuffled values preserve letter counts and paired-diagonal geometry.',
              'Compare that control only with the same symmetric subset. The fully shuffled',
              'control uses all complete grids. These are fixed permutations, not a p-value',
              'or a sampling distribution.', '',
              '| Method / mask | Dataset | Correct / predicted | Baseline correct |',
              '|---|---|---:|---:|']
    for experiment, method, pattern in [('02','frame_mdl','cells'),
                                         ('03','fragments','orbits'),
                                         ('04','modal_rollout','selected_corner_boundary')]:
        for control in ('original','shuffled','symmetric_original','orbit_shuffled'):
            s = data[experiment]['summary'][f'{control}|{pattern}|{method}']
            lines.append(f"| {method} / {pattern} | {control} | {s['correct']}/{s['predicted']} | {s['baseline_correct_same_cells']} |")
    lines += ['', 'Frame completion also succeeds when lexical ordering has been shuffled but',
              'symmetry survives. Thus high fill accuracy alone is not evidence of meaningful',
              'language or a generator. Fragment transfer is too sparse and error-prone',
              'to support its proposed use. The recurrence loses to the frequency baseline',
              'on the matched original symmetric subset.', '',
              '## Planted positive controls', '',
              '| Known construction | Correct / predicted | Hidden cells | Exact tasks |',
              '|---|---:|---:|---:|']
    for experiment, key, label in [
            ('02','planted_frames|cells|frame_mdl','Mixed frame symmetries'),
            ('03','planted_fragments|motif_centers|fragments','Recurring fragments'),
            ('04','planted_recurrence|gnomon|confident_rollout','Nonlinear local recurrence')]:
        s = data[experiment]['summary'][key]
        lines.append(f"| {label} | {s['correct']}/{s['predicted']} | {s['hidden']} | {s['exact_tasks']}/{s['tasks']} |")
    lines += ['', 'These controls establish sensitivity to the specific planted constructions.',
              'They do not replicate the historical Soyga algorithm. The composed frame-plus-',
              'fragment method introduces one wrong answer on the planted fragment data;',
              'its standalone fragment stage recovers every target.', '',
              '## Results by outer fold', '',
              'Counts concern the three principal masks; cells within a grid are dependent.',
              'The frame model fits visible target cells only. Its fold assignment affects',
              'the frequency baseline; the other methods exclude the fold from fitting.', '',
              '| Experiment / mask | Fold | Correct / predicted | Hidden | Baseline correct |',
              '|---|---:|---:|---:|---:|']
    for experiment, method, pattern in [('02','frame_mdl','cells'),
                                         ('03','fragments','orbits'),
                                         ('04','modal_rollout','selected_corner_boundary')]:
        for fold in range(5):
            counts = Counter()
            for r in data[experiment]['records']:
                if (r['control'], r['mask'], r['method'], r['fold']) == ('original',pattern,method,fold):
                    counts.update(r['score'])
            lines.append(f"| {experiment} / {pattern} | {fold} | {counts['correct']}/{counts['predicted']} | {counts['hidden']} | {counts['baseline_correct_same_cells']} |")
    lines += ['', '## Decision and limits', '',
              'Retain frame fills as candidates for a facsimile audit. Do not tune these',
              'three methods against the same outer folds and call the result validation.',
              'The next distinct attack is the period-dictionary hypothesis already in the',
              'literature: verify its sources, then test whether an independent lexicon',
              'predicts letters hidden as whole symmetry orbits. A curated vocabulary and',
              'reliable captions are missing inputs for that experiment.', '',
              'Historical verification still needs an image audit of this transcription and',
              'uncorrected German witness targets. No failure here establishes randomness,',
              'corruption as the sole explanation, or absence of every possible generator.', '',
              '## Reproduce and inspect', '',
              '[Shared harness and checks](analysis/stressbench/README.md) ·',
              '[02 frame method](analysis/02-frame-model/README.md) ·',
              '[03 fragment method](analysis/03-fragment-transfer/README.md) ·',
              '[04 recurrence method](analysis/04-local-recurrence/README.md).', '',
              f"Corpus SHA-256: `{manifest['corpus_sha256']}`.",
              'Each JSON result includes the manifest hash and every predicted cell.',
              'The digitized source is PRIMARY text mediated by',
              '[Peterson](https://www.esotericarchives.com/abramelin/abramelin.htm);',
              'its letters have not been collated to a facsimile.']
    (ANALYSIS.parent/'STRESS-TESTS.md').write_text('\n'.join(lines)+'\n')


if __name__ == '__main__':
    main()
