# Research log — append-only, newest first

## Dead ends
- 2026-11-16 — The key census as a product of its own (plan Track 2, Q1). Bourdeau's "How keys changed" already
  covers 783 systems. Closed before it started; see the entry below.

---

## 2026-11-16 (night) — Pilot gate: four candidates, none through
After no. 2192 (below), in the order the prompt gives:
- **No. 2345** (Baldovino del Monte, ASF): race passes. Images, pair and size not checked: the ASF host
  (`archiviodistatofirenze.cultura.gov.it`) timed out for the scout over 30 minutes and for the main thread twice,
  two hours apart; the web-fetch network got "connection refused". The scout found that DECODE lists the Cosimo I
  key volume (`ASFi_SIVol3_*`, records 6087–6097 dated 1554–55, login needed), which the catalogue entry denies.
  `items/2345/gate.md`. Ledger: `queued`.
- **No. 1468** (head of the queue): not gated. Scans need a reader account at CEHM. It is also a 1913 telegraph code.
- **No. 2911** (Dieci di Balìa to Machiavelli, 17 Aug 1510; with 2910 and 1549): race passes; BNCF Teca serves
  300 dpi masters (`…ImageViewer?idr=<id>&azione=showImg&usage=2`), not the 900 px the catalogue reports; a real
  period pair exists (V/140, the Dieci's cipher copy of Niccolini's letter from Rome of 5 Aug 1510, with
  Machiavelli's autograph decipherment V/139 cc. 1v–2r). **Gated out on check 5:** a Fable agent, isolated so that
  the main thread stays blind, compared the period key sheets BNCF Carte Machiavelli VI/82 with the letters by sign
  inventory and by six glossed signs on V/139 c. 1r. Units 1–4 are one cipher and it is this one; unit 5 ("Cifera di
  messer Goro", cipher of Messer Goro) is another. So the item is a key lookup. A 19th-century sheet in VI/82 and
  the modern clear text of V/136 suggest someone has read these letters with it. Not verified: whether the Edizione
  Nazionale prints V/134 and V/125. `items/2911/gate.md`, `items/2911/keysheet-check.md`.

**What the gate cost.** Four scouts and one check. The four that ran to the end: 79k, 122k, 232k and 173k tokens
(3, 17, 19 and 8 minutes). No item reached stage 1.

**What is left in the queue for 1450–1700 that can be worked today** (`line/queue.tsv`, main-thread scan of
access notes): nothing clean. ASF holds 13 of the candidates and is down. The 33 Sforza items and no. 880 need a
DECODE login. BnF fr. 15567–15568 (nos. 2838–2841) are in ciphers Tomokiyo has keys for, and Bourdeau's
contributors are reading them now (`canon.md`). The rest are German, Swedish or one line long.

## 2026-11-16 (later) — Key line, phase 0: tools and calibration; pilot gate
Ran `PROMPT-key-line.md`. Built `line/` (`align.py`, `compare.py`, `fluency.py`, `queue.py`, `taken.py`,
`ledger.tsv`, 24 tests). One Opus agent wrote the support tools; the aligner and both calibrations are main-thread.

**Differences from `PIPELINE.md`, as the prompt asks to be noted.**
- *Real calibration pair.* Saint-Goard's letter of 23 Dec 1579 cannot test the aligner: its cipher side exists
  only as letter values read with the key, and the Longlée table only as an image. Used es. 132 f. 255 (blind sign
  transcription) against Teulet's print of the Simancas minute, scored on Cp.30. `analysis/03-calibration-real/`.
- *Control bar.* The edit-distance scorer gives a shuffled table 0.25 by chance. A bar of "≤ 25%" is that chance
  level. Calibration used ≤ 0.30; stage 4 should say "control ≤ 0.30 and at least 25 points under the accuracy".
- *Composite signs.* The design treats a token as one sign. Cp.30 needs base, mark after and marks above as
  separate units (`25:curl^bar` → `25`, `:curl`, `^bar`). `align.py` does that; a sign guide chooses the split.
- *Status rule.* `probable` needs four supporting places, not three (calibration run 4).
- *Queue size.* The catalogue gives 132 class A desk-workable items, not 76. 43 of them are named in a target
  folder of Bourdeau's repository. Queue after `--taken`: 89.

**Calibration.** Both pass after three fixes to the aligner; each failure and fix is in the experiment README.
The failures: (1) on the real pair every sign went to null and rare signs took whole phrases; (2) the first cure
cut code words to a syllable on the synthetic pairs; (3) a code sign and its mark split one word. Final figures:
synthetic, five seeds, 0 wrong among 41–44 marked values, held-out 0.93–0.95, control 0.25; real, 26 of 29
frequent signs right, 0 of 13 `certain` wrong, held-out 0.83 against a true-key ceiling of 0.79.
The five seeds and the real pair were used to fix the aligner, so they are spent as tests.

**Pilot gate, no. 2192: gated out, race lost.** The scout found `targets/sosa1554/` in Bourdeau's repository
(commit cbd93dbe, merged 12 Nov 2026): a contributor rebuilt the letter-1 key from the Panama 29 clear copy and ran
a held-out test (their figure: 447 of 587 letters). Verified by the main thread on the repository tree.
`catalogue.json` shows none of this: no `reserved`, no `writeup`. `items/2192/gate.md`.
The scout read that project's notes, which summarise sign values; it is exposed and was not used again.
PARES returned HTTP 429 to every image request, so no image recipe was verified.

**Consequence for the queue.** Work in progress is visible only in `targets/*/profile.json`. `line/taken.py`
reads the 879 profiles (fetched 2026-11-16) and `queue.py --taken` drops the ids they name. A profile may name
an id as a cross-reference, so 43 is an upper bound on items truly taken.

## 2026-11-16 — Race check and target choice
Merged the plan branch. Greg redirected: recover a missing key, easiest first, using Tomokiyo's unsolved list and
the existing keys as leverage. Fetched and read `unsolved.htm` and `henryiii.htm` (cached, `sources/cache/cryptiana/`),
then Bourdeau's site and `catalogue.json`.

Found:
- Nearly every item on Tomokiyo's list in our period is solved or has been attempted by Bourdeau's group
  (Birago 1571, Blancmesnil offline, Moncada, Segur, Throckmorton margin, f. 151 too short).
- Bourdeau's project has grown into a collective with a 1,388-item open catalogue and a published key census.
  Both planned tracks sit inside it. `canon.md`, "The field".
- `analysis/01-gaps/`: 56 desk-workable items of 1550–1620 in his catalogue (17 A, 22 B, 17 C).
- Among them, the Terranova → Sfondrati set (nos. 2077, 2518) has the most same-key ciphertext with no key
  claimed, is Spanish of 1583 (the family we hold four keys for), and is not attempted. Chosen as target.
- Viewed one page (SCMisc 50207). Its features match Tomokiyo's description of the general cipher Cg.12 (1582).
  Recorded as H1. If H1 holds, this target yields a reading, not a new key.
- Passed over: Añover 1610 (key already rebuilt by a contributor, 13 Nov); Bazin 1573 (probably Monluc's cipher,
  H5); Nevers 1595 and Duplessis-Mornay (attempted and failed there).

No transcription and no decoding was done.
