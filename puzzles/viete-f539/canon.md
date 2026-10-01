# Canon — what we believe now

Facts only. Each item: the claim, a confidence (`established` / `likely` /
`disputed`), and a source pointer. When a claim is refuted, move it to
`research.md` under Dead ends and rewrite here.

## The object
- F. 539 is Gallica canvas 544 (right-hand page, folio number "539" visible). Its
  verso, canvas 545 right-hand page, is foliated 540 and has no cipher. `established`:
  images in `sources/cache/` (see `sources/PROVENANCE.md`); Bourdeau NOTES (below)
  gives the same canvas.
- The full IIIF image is 7580 × 5347 px. `established`: download 2026-10-01.
- F. 555 (Sennecey to the Archbishop of Lyon, the solved control) is canvas 562 right
  page, and it continues on 555v, canvas 563 left page. `established`: images.
- DECODE R2281 records ff. 539–540: "Non-decrypted", graphic signs plus numerical
  groups, entered by Tomokiyo. `likely`: reported by Bourdeau's NOTES; DECODE not
  opened here.

## The text
- A clear French frame. The cipher follows "Ce que je vous puis dire d'icy en
  substance n'est autre chose sinon que" and ends before "Je vous baise les mains de
  l'asseurance que vous me donnez…". Dated "Rome, ce xv fevrier 1594". `established`:
  read on the image.
- The cipher block is 11 lines. The last is short. `established`: image.
- The block mixes three kinds of token: graphic signs without marks, graphic signs
  with marks (dots, crosses, hash bars, and long barred stems below), and Arabic
  numbers (e.g. 88, 196, 223, 152). `established`: image. Counts under Structure below.
- The clear frame says Villars's own letter to Joyeuse was partly in cipher ("tout ce que
  vous m'y mandez en chiffre"). So at least one other letter, Villars to Joyeuse, probably
  used a shared key. `likely`: the frame as read by Bourdeau and checked on the image; that it
  is the *same* key is inference.

## Dating, provenance, authorship
- Joyeuse to Villars, admiral of France, Rome, 15 February 1594. `established`:
  clear frame and signature; Tomokiyo, Cryptiana viete.htm (SECONDARY).

## Structure and statistics (from `analysis/`, never from impression)
- Length: 365 / 367 tokens (blind readers A / B; Bourdeau 358). Of these, 344 / 345 are
  non-numeric signs; the rest are about 19 Arabic numbers and 2 Roman numerals. `established`
  (three readers within 3 tokens per line): `analysis/00-transcription-and-gate/`.
- Distinct signs: 145 / 165 labels (A / B), 127 for Bourdeau. The spread is variant-splitting;
  no reconciled inventory exists yet. Each sign occurs about 2.1–2.6 times, against about 10 for
  f. 555 and about 8 for Marmont. `established` as a range.
- Marked signs: about 80 tokens over about 40 labels in both blind readings. `likely`.
- Arabic numbers in order (A and B agree): 88 196 223 184 152 89 86 30 209 152 30 25 199 174
  152 54 89 128 85. 152 occurs three times; 89 and 30 twice. `likely` (B reads 139? for 199).
- No word breaks are visible. `established` (A, B).
- A homophonic annealer that solves a Marmont-shaped control (1,300 tokens, 155 signs) at 98.6%
  recovers only 6–17% of a key on an f. 539-shaped control (344 tokens, 145 signs), even when
  every sign is assumed to be a letter. It needs between 700 and 1,400 same-key tokens at this
  sign count. `established` for this solver and model: `analysis/01-annealing/`.

## Prior scholarship: settled points
- F. 555, the control, is 858 cipher symbols over 86 distinct signs (about 10 uses per
  sign). Lasry broke it by simulated annealing only with a historical-French 5-gram model
  plus manual work; a generic-French trigram run failed. The paper does not mention f. 539
  or Joyeuse, and gives the key only as an image (Fig. 2, "tentative"). `established`:
  Lasry, HistoCrypt 2022, https://ecp.ep.liu.se/index.php/histocrypt/article/view/402 (SCHOLARLY);
  summary in `sources/breach-research-2026-10-01.md`. Tomokiyo's "79 symbols" disagrees; the paper wins.
- Not solved as of 2026-10-01. Cryptiana's unsolved list still shows the Viète item as
  "One of Two Solved" (f. 555 only). `established`: https://cryptiana.web.fc2.com/code/unsolved.htm (SECONDARY), fetched 2026-10-01.
- Daniel Bourdeau attacked f. 539 on 2026-09-16 and closed it as "not solvable with
  what is online". His homophonic annealer recovered 1–18% of the key on three matched
  controls, and six runs on the target gave unrelated fragments. `established` as a
  report of his result: CLAIMANT/secondary working notes,
  https://github.com/dbourdeau/cyphersolver/tree/9226922ffb0663b1d9b95f4ef898d093efd74ef2/targets/joyeuse
- F. 539 is not in the f. 530 alphabet (Tomokiyo), nor in the Caulet–Joyeuse cipher of
  August 1593 (Tomokiyo; Bourdeau confirms by shape comparison), nor in Lasry's f. 555
  key (Bourdeau: f. 555 has no marked series and no numbers). `likely`.
