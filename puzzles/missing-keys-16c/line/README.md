# line/ — tools for the key line

The design is in `../PIPELINE.md`. The method as practised, end to end, is in `METHOD.md`. Python 3.11+, standard library only. Run every command from this directory.

| File | What it does |
|---|---|
| `align.py` | Builds a key table from a pair, runs the held-out test, decodes with a key. Formats are in its docstring. |
| `queue.py` | Rebuilds the work queue from a catalogue pull. |
| `ledger.tsv` | One row per item and its status. Rows change status; they are not deleted. |
| `compare.py` | Agreement between two readers' transcriptions; diffs; a both-readers-agree transcription. |
| `merge.py` | One transcription from three or more readers, by vote. |
| `fluency.py` | Share of decoded letters covered by period words, against permuted keys. |
| `test_line.py` | Tests for all of the above. |

## Commands

    python3 -m unittest test_line.py

    python3 queue.py ../sources/cache/bourdeau-catalogue.json [--prev older.json] [--ledger ledger.tsv] > queue.tsv

Keeps class A, desk-workable, unreserved, unwritten items not closed in the ledger. With `--prev`, changes since
the older pull go to stderr, and items whose status text changed leave the queue. The count by repository goes
to stderr. `--ledger` defaults to `ledger.tsv` here.

    python3 compare.py readerA/ readerB/ --out agreement.tsv --diffs diffs.txt
    python3 compare.py a.txt b.txt --consensus both.txt

Two files or two directories (paired by file name). Token and unit agreement = 2 x matched / (A + B).
`--consensus` takes one file pair. Each stretch where the readers disagree becomes one `?`, in A's line breaks.

    python3 fluency.py cipher.txt key-v1.tsv words.txt [--perms 20] [--minlen 3] [--seed 1] [--min probable]

Unknown units and clear words break the decode into runs. In each run the best segmentation into list words
of at least `minlen` letters is found. Output is `key<TAB>value` lines: the share for the key, then the mean and
maximum share over permuted keys.

    python3 align.py build   cipher.txt plain.txt --out key-v0.tsv [--aligned aligned.txt]
    python3 align.py build   cipher.txt plain.txt --out key-v0.tsv --abridged    # plain side cut and reworded (no. 2911)
    python3 align.py heldout cipher.txt plain.txt [--folds 5] [--perms 20] [--out heldout.tsv]
    python3 align.py decode  cipher.txt key.tsv [--min probable]

Note: `queue.py` shadows the standard-library module `queue` for scripts run from here.
