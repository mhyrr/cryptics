# 01 — gap list from Bourdeau's open catalogue

**Question.** Which unsolved items of 1550–1620 can be worked from a desk, and of what class?
**Method.** `gaps.py` filters `catalogue.json` (fetched 2026-11-16, sha256 3f093d32…): year 1550–1620 and
(`access == "online"` or `needs_archive_scan == "no"`). Sorted by class, then solvability, then difficulty.
Classes and scores are Bourdeau's and unvalidated.
**Run.** `python3 gaps.py ../../sources/cache/bourdeau-catalogue.json > gaps.tsv`
**Result.** 56 rows of 1,388 open entries: 17 class A (sibling deciphered), 22 B (partial key), 17 C (no key).
**Limits.** It lists only what his catalogue holds. His catalogue excludes items on Tomokiyo's list unless they
came through Cryptoole. An item's class is his judgement: no. 2077 is class C, yet H1 says a published key may fit.
