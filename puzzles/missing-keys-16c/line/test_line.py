"""Tests for the key line tools. Run from line/:  python3 -m unittest test_line.py"""
import importlib.util, os, random, tempfile, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
import align, compare, fluency  # noqa: E402

_spec = importlib.util.spec_from_file_location("line_queue", os.path.join(HERE, "queue.py"))
lq = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(lq)


class SplitToken(unittest.TestCase):
    def test_marks(self):
        self.assertEqual(align.split_token("20:hook^v^bar?"), (["20", ":hook", "^v", "^bar"], True))
        self.assertEqual(align.split_token("25"), (["25"], False))
        self.assertEqual(align.split_token("25^v"), (["25", "^v"], False))

    def test_alternative(self):
        self.assertEqual(align.split_token("a|b"), (["a"], True))

    def test_bare_unread(self):
        self.assertEqual(align.split_token("?"), (["?"], True))


class ParsePlain(unittest.TestCase):
    def test_boundaries_lacuna_anchor(self):
        P, wb, lac, anch = align.parse_plain("de la ca[sa], [...] @x tierra")
        self.assertEqual(P, "delacasatierra")
        self.assertEqual([j for j, b in enumerate(wb) if b], [0, 2, 4, 8, 14])
        self.assertFalse(wb[6])                      # '[sa]' is not a lacuna and not a boundary
        self.assertEqual([j for j, b in enumerate(lac) if b], [8])
        self.assertEqual(anch, {"@x": 8})

    def test_comment_rows_and_ellipsis_char(self):
        P, wb, lac, _ = align.parse_plain("# note\nuno […] dos")
        self.assertEqual(P, "unodos")
        self.assertTrue(lac[3])

    def test_punctuation_is_boundary(self):
        P, wb, _, _ = align.parse_plain("si,no")
        self.assertEqual(P, "sino")
        self.assertTrue(wb[2])


class NormLetters(unittest.TestCase):
    def test_merges(self):
        self.assertEqual(align.norm_letters("Vjña"), "uina")
        self.assertEqual(align.norm_letters("Vjña", merge=False), "vjna")
        self.assertEqual(align.norm_letters("Æsop Straße œuvre"), "aesopstrasseoeuure")
        self.assertEqual(align.norm_letters("Ç-12é"), "ce")


class Score(unittest.TestCase):
    def test_identical(self):
        self.assertEqual(align.score(["a", "b", "c"], "abc"), (3, 3, 3))

    def test_one_substitution(self):
        self.assertEqual(align.score(["a", "x", "c"], "abc"), (2, 3, 3))

    def test_unknown_absorbs(self):
        self.assertEqual(align.score(["a", None, "d"], "abcd"), (2, 2, 4))
        self.assertEqual(align.score(["qu", None, "ro"], "quiero"), (4, 4, 6))

    def test_null_and_clear(self):
        self.assertEqual(align.score(["", "[de]", "l"], "del"), (3, 3, 3))


WORDS = ("el rey nuestro senor manda que se haga la paz con los de francia y que el duque salga de la ciudad "
         "por tierra con su gente para dar orden en las cosas del estado porque conuiene mucho al seruicio "
         "de dios y de su magestad").split()


def planted_pair(seed=7, nletters=600):
    rng = random.Random(seed)
    text, n = [], 0
    while n < nletters:
        w = rng.choice(WORDS)
        text.append(w)
        n += len(w)
    alphabet = sorted(set("".join(text)))
    signs = list(range(10, 10 + 2 * len(alphabet) + 1))
    rng.shuffle(signs)
    homs = {c: [str(signs[2 * k]), str(signs[2 * k + 1])] for k, c in enumerate(alphabet)}
    null = str(signs[-1])
    truth = {s: c for c, ss in homs.items() for s in ss}
    truth[null] = ""
    toks = []
    for w in text:
        for c in w:
            if rng.random() < 0.05:
                toks.append(null)
            toks.append(rng.choice(homs[c]))
    rows = [" ".join(toks[i:i + 12]) for i in range(0, len(toks), 12)]
    return "\n".join(rows) + "\n", " ".join(text) + "\n", truth


class Build(unittest.TestCase):
    def test_planted_pair(self):
        ctext, ptext, truth = planted_pair()
        units, ca, _ = align.parse_cipher(ctext)
        P, wb, lac, pa = align.parse_plain(ptext)
        segs = align.make_segments(units, P, wb, lac, align.tie_pairs(units, P, ca, pa))
        table = align.train(segs, iters=8)
        path, _ = align.best_path(segs, table)
        rows = {r["unit"]: r["value"] for r in align.key_from_path(path)}
        counts = {}
        for u in units:
            counts[u.sym] = counts.get(u.sym, 0) + 1
        common = [s for s, k in counts.items() if k >= 5]
        right = [s for s in common if rows.get(s) == truth[s]]
        wrong = {s: (rows.get(s), truth[s]) for s in common if rows.get(s) != truth[s]}
        self.assertGreaterEqual(len(right) / len(common), 0.9, f"wrong (got, true): {wrong}")


def abridged_pair(seed=5):
    """A planted pair of the 2911 kind: letters and open syllables, a quarter of the plain text cut out."""
    rng = random.Random(seed)
    words = ("intendesi come pare che el papa seguiti nella medesima opinione di uoler rifare la armata per "
             "andare a genoua doue si e ferma de uiniziani si dice esserui giunte tre galee bastarde e quattro "
             "aspettarsene qui si mette ad ordine con altri legni quali ui si truouano ancora franzesi questi "
             "di stata dubitossi non uolessi affrontarsi quella pure ritornata da bologna fu auuisato dello "
             "essere sute rimesse le sue gente sino uerso imola perche lettera del legato dato colpa duca").split()
    T = "".join(rng.choice(words) for _ in range(330))
    cv = sorted({T[i:i + 2] for i in range(len(T) - 1) if T[i] not in "aeiou" and T[i + 1] in "aeiou"})
    values = sorted(set(T)) + cv[:30]
    key = {f"k{i}": v for i, v in enumerate(values)}
    sign = {v: k for k, v in key.items()}
    out, starts, i = [], [], 0
    while i < len(T):
        two = T[i:i + 2]
        if len(two) == 2 and two in sign:
            out.append(sign[two]), starts.append(i)
            i += 2
        else:
            out.append(sign[T[i]]), starts.append(i)
            i += 1
    keep = [True] * len(T)
    for a in (150, 600, 1100):
        for k in range(a, a + len(T) // 12):
            keep[k] = False
    plain = "".join(ch for k, ch in enumerate(T) if keep[k] and rng.random() > 0.03)
    return " ".join(out) + "\n", plain + "\n", key


class BuildAbridged(unittest.TestCase):
    def test_planted_abridged_pair(self):
        ctext, ptext, truth = abridged_pair()
        units, ca, _ = align.parse_cipher(ctext)
        P, wb, lac, pa = align.parse_plain(ptext)
        old = align.AB_BEAM
        align.AB_BEAM = 2000      # a smaller beam finds half the table on this pair (none wrong)
        try:
            rows = align.build_abridged(units, P, wb, lac)
        finally:
            align.AB_BEAM = old
        marked = align.key_map(rows)
        wrong = {u: (v, truth[u]) for u, v in marked.items() if truth.get(u) != v}
        counts = {}
        for u in units:
            counts[u.sym] = counts.get(u.sym, 0) + 1
        common = [u for u, k in counts.items() if k >= 10]
        right = [u for u in common if marked.get(u) == truth[u]]
        self.assertGreaterEqual(len(right), 0.8 * len(common), f"{len(right)} of {len(common)} common signs")
        self.assertLessEqual(len(wrong), 0.1 * len(marked), f"wrong (got, true): {wrong}")
        self.assertEqual(align.null_share(rows), 0.0)

    def test_null_share(self):
        rows = [dict(value="", support=6), dict(value="a", support=2)]
        self.assertEqual(align.null_share(rows), 0.75)


A_TXT = "# reader A\n1 2 3\n4 5? 6\n[[de]] 7\n"
B_TXT = "1 2 3\n4 5 9\n[[de]] 7\n"


class Compare(unittest.TestCase):
    def test_agreement(self):
        r = compare.compare_texts(A_TXT, B_TXT)
        self.assertEqual((r["tokens_a"], r["tokens_b"], r["tok_matched"]), (8, 8, 7))
        self.assertAlmostEqual(compare.ratio(r["tok_matched"], 8, 8), 0.875)
        self.assertEqual((r["doubt_a"], r["doubt_b"]), (1, 0))

    def test_tokens_vs_units(self):
        r = compare.compare_texts("20:hook^v 3\n", "20:hook 3\n")
        self.assertEqual((r["tokens_a"], r["tok_matched"]), (2, 1))
        self.assertEqual((r["units_a"], r["units_b"], r["unit_matched"]), (4, 3, 3))

    def test_one_entry_per_token(self):
        ua, _, _ = align.parse_cipher("20:hook^v [[de la]] ?\n")
        self.assertEqual([t.text for t in compare.tokens(ua)], ["20:hook^v", "[[de]]", "[[la]]", "?"])

    def test_consensus(self):
        ua, _, _ = align.parse_cipher(A_TXT)
        ub, _, _ = align.parse_cipher(B_TXT)
        self.assertEqual(compare.consensus(ua, ub), ["1", "2", "3", "4", "5?", "?", "[[de]]", "7"])
        ub2, _, _ = align.parse_cipher("1 8 8 8 7\n")
        ua2, _, _ = align.parse_cipher("1 2 7\n")
        self.assertEqual(compare.consensus(ua2, ub2), ["1", "?", "7"])

    def test_consensus_file_keeps_lines_and_anchors(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "c.txt")
            compare.write_consensus("1 2\n@a 3 4\n", "1 2 3 5\n", p)
            with open(p, encoding="utf-8") as f:
                body = [l for l in f.read().splitlines() if not l.startswith("#")]
            self.assertEqual(body, ["1 2", "@a 3 ?"])
            units, anch, _ = align.parse_cipher("\n".join(body))
            self.assertEqual(anch, {"@a": 2})


class Fluency(unittest.TestCase):
    def test_covered_share(self):
        words = {"casa", "de", "la", "mar"}
        self.assertAlmostEqual(fluency.covered_share("lacasademar", words, 3), 7 / 11)
        self.assertAlmostEqual(fluency.covered_share("lacasademar", words, 2), 1.0)
        self.assertAlmostEqual(fluency.covered_share("casa|xx", words, 3), 4 / 6)
        self.assertEqual(fluency.covered_share("", words, 3), 0.0)

    def test_dp_beats_greedy(self):
        words = {"casad", "casa", "demar"}           # greedy 'casad' leaves 'emar'; best is casa+demar
        self.assertAlmostEqual(fluency.covered_share("casademar", words, 3), 1.0)

    def test_stream_breaks_on_unknown(self):
        units, _, _ = align.parse_cipher("1 2 9 [[de]] 1\n")
        self.assertEqual(fluency.stream(units, {"1": "a", "2": ""}), "a||a")


def entry(i, **kw):
    e = dict(id=i, cls="A", access="online", needs_archive_scan="no", reserved=None, writeup=None,
             outcome=None, language="Spanish", solvability=3, difficulty=2, repository="r1", status="s",
             title=f"t{i}", year=1580, shelfmark="x")
    e.update(kw)
    return e


CAT = [entry(1),
       entry(2, language="German", solvability=4),
       entry(3, cls="B"),
       entry(4, access="archive", needs_archive_scan="yes"),
       entry(5, language="French", repository="r2"),
       entry(6, language="Italian", reserved={"by": "x"}),
       entry(7, language="Latin", solvability=5, access=None),
       entry(8, language="unknown (probably Italian)", solvability=5),
       entry(9, language="Italian", writeup="w.html"),
       entry(10, language="Italian", solvability=3, difficulty=1)]
LEDGER = [dict(id="7", status="walled", repository="r9"), dict(id="99", status="key-built", repository="r2"),
          dict(id="1", status="queued", repository="r1")]


class Queue(unittest.TestCase):
    def test_filter_and_order(self):
        q = lq.build(CAT, LEDGER)
        self.assertEqual([e["id"] for e in q], [10, 5, 1, 8, 2])

    def test_prev_drops_changed_status(self):
        prev = [dict(e) for e in CAT if e["id"] != 10] + [entry(11)]
        prev[0]["status"] = "older text"
        logs = []
        q = lq.build(CAT, LEDGER, prev, logs.append)
        self.assertEqual([e["id"] for e in q], [10, 5, 8, 2])
        self.assertTrue(any(l.startswith("changed\t1\tstatus") for l in logs))
        self.assertTrue(any(l.startswith("vanished\t11") for l in logs))
        self.assertTrue(any(l.startswith("dropped") and l.endswith(" 1") for l in logs))

    def test_readable(self):
        self.assertTrue(lq.readable("Spanish (probably)"))
        self.assertTrue(lq.readable("German / French"))
        self.assertFalse(lq.readable("unknown"))
        self.assertFalse(lq.readable("Portuguese"))

    def test_ledger_header(self):
        rows = lq.read_ledger(os.path.join(HERE, "ledger.tsv"))
        self.assertTrue(all(len(r) == 17 for r in rows))        # every row has every column
        with open(os.path.join(HERE, "ledger.tsv"), encoding="utf-8") as f:
            head = f.readline().rstrip("\n").split("\t")
        self.assertEqual(head, ["id", "title", "cls", "form", "language", "repository", "status", "reason",
                                "pair_tokens", "bare_tokens", "heldout_acc", "coverage", "control_acc", "key_commit",
                                "agents_used", "opened", "closed"])


if __name__ == "__main__":
    unittest.main()
