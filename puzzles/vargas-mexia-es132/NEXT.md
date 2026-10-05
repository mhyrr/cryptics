# NEXT — handoff for the next session

**Last session:** 2026-10-04 (session 4, experiment 06)
**Where it stopped:** H16 judged. Every es. 132 letter of 16 Dec 1577 – 17 Mar 1578 is read: cipher letters ff. 3 (Cipher 1),
11–12, 17–20 + dup 22–25, 26r, 34 (Cipher 2) and 32 (Cipher 3), two blind readers each; clear letters ff. 5–7, 9, 14–15
on the image; Teulet pp. 132–146 on the page. **H16a refuted**: no window letter speaks of a Don John–Guise league,
confederation or unión. **H16b weakened**: on 24 Jan 1578 (f. 12v) the King acknowledges Vargas's report of "todo lo [que]
los Guysas trataron con [Sotomayor] cerca del proceder de mi hermano y con Alanson" and calls it "cosas que tienen mucha
consideración". Mignet dates Sotomayor's Guise mission to May 1578 only. OVERVIEW §7.3 rewritten and republished
(https://claude.ai/artifact/BSsgyjHHehAd9nA3zLWBi2, v5). Third-party comparison done (medians 82–95%).

## Do first
1. **Date Mignet's "grande confidence" report** (Série B, liasse 44, n° 89; Mignet p. 439 n. 1). If it predates 31 Mar
   1578, H16 moves. Needs PARES/AGS (Estado K 1546) or a Simancas request. Also the Sotomayor–Guise conference papers
   (Paz p. 382, K 1543).
2. **Human review request** (unchanged): a reader of 16th-century Spanish secretary hands to check f. 12v lines 2–4
   (the Sotomayor–Guise run) and the v2 texts of ff. 198, 123, 154 against the images. Ask Greg who.
3. Reconciled texts (blind reconciler) for ff. 11–12 and 17–25 if any wording from them is to be quoted beyond f. 12v
   and the Mignet passages.
4. Then the older queue: second reader for f. 154; the rest of the Cipher 3 volume (duplicate pairs first).

## Open questions
- Is B.44 n° 89 (Don John–Guise "grande confidence") before or after 31 Mar 1578?
- The missing letter of 4 Jan 1578 "con correo propio" (f. 14r) — never arrived, or lost from the volume?
- ff. 26v–31r: not in the Gallica scan. Does the BnF hold images, or are the leaves unphotographed?
- f. 34's date: 16 Mar (cabinet-noir, BnF) or 17 Mar (our reader A)? The line is cut at the gutter.
- Cipher 2 candidate: the long swash = ll (f. 26, in-sample; pangoleen agrees). Test on f. 273.
- Earlier open points (Arcauti, the Theatine, 21. = que, "ra" = oficio, Parker) stand.

## Named wall
For H16: Vargas's own dispatches of Dec 1577 – Mar 1578 (AGS Estado K 1543–1547) are known only through Teulet's
Scotland-centred excerpts and Mignet's quotations. For all readings: Sonnet transcriptions, no human paleographer.
Breach: Simancas images (PARES) and a paleographer.

## Operational lesson
Never let parallel readers fetch from Gallica: 13 at once got the machine rate-limited for about an hour. Fetch whole
pages once, serially (`sources/cache/pages/fetch_pages.py`, 20 s apart), and have readers crop locally.
