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
  numbers (e.g. 88, 196, 223, 152). `established`: image. Counts are pending the
  blind transcription (`sources/transcription/`).

## Dating, provenance, authorship
- Joyeuse to Villars, admiral of France, Rome, 15 February 1594. `established`:
  clear frame and signature; Tomokiyo, Cryptiana viete.htm (SECONDARY).

## Structure and statistics (from `analysis/`, never from impression)
- Pending. The only measurement so far is Bourdeau's single-reader transcription:
  358 tokens, 147 distinct; 234 unmarked tokens over 81 signs; 95 marked tokens over
  48 signs; 29 number tokens over 18 values. `likely` (one reader; he states it is
  unchecked).

## Prior scholarship: settled points
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
