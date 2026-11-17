# No. 2351 — Roberto Acciaiuoli, Amiens, 23 October 1513

**Verdict 2026-11-17: queued, scan access blocked.** First choice when the
Florence images are reachable.

## Evidence for the choice

Bourdeau's latest catalogue entry and [PR 531](https://github.com/dbourdeau/cyphersolver/pull/531)
identify a cipher original, a separate clear copy, and a same-day bare
letter in Archivio di Stato di Firenze, Mediceo avanti il Principato,
filza LXXII. The PR records a check of the clear copy and bare recto.
This is the vetter's identification. We have not seen any of the pages.

| Role | Document | Archive viewer IDs |
|---|---|---|
| Build, cipher | 190, c. 232 | 79570 and 79571 |
| Build, plain | 191, c. 233 | 79572 and 79573 |
| Transfer, held out | 192, c. 234 | 79574 and 79575 |

PRIMARY · [Archive's filza 72 viewer](https://archiviodistatofirenze.cultura.gov.it/map/ricerca/ricerca-su-filza/?f=72&d=190&c=).
The [bare recto](https://archiviodistatofirenze.cultura.gov.it/map/riproduzione/?id=79574)
and the direct IIIF info probe timed out from this environment, including
outside the sandbox. The old archive domain ended the TLS connection.
The script for no. 2345 failed on the same archive host. A public mirror
of the requested folios did not surface.

Fresh catalogue JSON lists 2351 without a reservation, write-up or outcome.
A search of public issues and pull requests for Amiens 1513 found the
vetting PR and no recovery. Searches on Acciaiuoli and Amiens 1513 did
not surface a key. The neighboring Pandolfini correspondence has a
published table with a similar sign style. Its applicability is open.
Before claiming a missing key, screen the transcription against that
table and other plausible published tables.

## First run after access

1. Fetch and visually verify all three documents and their folio labels.
   Establish whether doc. 191 follows doc. 190 across the opening,
   interior and close. Check for omission and estimate the token count.
2. Freeze a sign guide and the transcription assignments. Keep the
   superscript marks and base shapes distinct in the raw transcription.
3. Register the matched control and holdout before fitting. Use doc. 190
   and 191 to recover values, with a held-out portion of 191 as a test.
   Keep doc. 192 entirely outside derivation and use it for transfer.
4. Keep only values with independent support. Compare held-out
   accuracy and coverage with the registered bars and a shuffled-key
   control. Leave unsupported signs open.
