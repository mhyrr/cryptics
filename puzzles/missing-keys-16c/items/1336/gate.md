# No. 1336 — Speciano and Borromeo cipher passages

**Verdict 2026-11-17: proceed to the transcription gate.** The scans are
reachable. Check legibility and the connection between the witnesses before
running a key recovery.

## Public prior art

Bourdeau lists the item as open. The local taken list, current public
repository target paths, a GitHub issue search for Speciano, and web
searches for Speciano/Spetiano and Borromeo ciphers returned no recovery
for this pair. The Milan sweep reports no DECODE record. These are
bounded checks. A usable key could still exist under a different name.
Some variants of the surname are catalogued as Spetiano.

- CLAIMANT · [Catalogue no. 1336](https://dbourdeau.github.io/cyphersolver/solve/1336.html)
- CLAIMANT · [Milan archive sweep](https://github.com/dbourdeau/cyphersolver/tree/main/research/milan_archives)
- PRIMARY · [Ambrosiana record for the pair](https://ambrosiana.comperio.it/opac/detail/view/ambro:catalog:594280)
- PRIMARY · [Speciano to Borromeo](https://ambrosiana.comperio.it/opac/detail/view/ambro:catalog:614986)
- PRIMARY · [Borromeo to Speciano](https://ambrosiana.comperio.it/opac/detail/view/ambro:catalog:594432)

## Inspected evidence

- **Build pair, F 47 inf. no. 131.** C. 269r is a dense pasted cipher
  slip followed by an instruction to see the next folio. C. 270r
  holds a separate running Italian text. The OPAC identifies it as
  the translation of the cipher. The layout supports that relationship.
  Exact coverage and omissions await alignment. The item has no date
  or named correspondents in its OPAC title and imprint. The
  catalogue indexes it under Speciano. Check the attribution in
  Rivolta before relying on it.
- **Possible transfer, F 131 inf. no. 7, 4 July 1574.** C. 14r has a
  short cipher passage inside clear text. It is attributed to Speciano
  writing to Borromeo. The remaining leaves are available.
- **Possible transfer, F 49 inf. no. 18, 2 March 1575.** C. 44r
  holds a small cipher slip and separate clear notes. The notes
  could provide independent context. Their relation to the cipher has
  yet to be established. The record names Borromeo as writer and
  Speciano as recipient.

The slips share several visible sign shapes. A shape match cannot
establish a shared table. On the build folio, the signs are cramped
and several stretches are smudged at the served resolution. The
smaller transfer slip is visually clearer. This is a reason to test
the reading agreement before fitting any values.

The OPAC detail requests returned a script challenge. The separately
documented public image links served JPEGs directly. The older data
list sorts image IDs numerically, so it cannot establish reading
order. The visible page numbers and orientation establish that image
12041 is c. 269r and 12040 is the reverse with show-through. The
clear copy is 12042. See [provenance](PROVENANCE.md).

## First run

1. Freeze a guide from c. 269r that records shapes only. Cut windows at
   native resolution. Ask two isolated readers to transcribe the same
   cipher sample. Send the clear c. 270r to separate readers. Use the
   pipeline's agreement threshold and one guide revision.
2. If the sample passes, complete and reconcile both transcriptions.
   Check whether the clear copy is continuous and measure the matched
   sign count. Screen plausible published tables and calibrate on a
   comparable known-key pair. Freeze the split and score before fitting.
3. Build on the matched segments of the F 47 pair, with bounded
   anchors and support per value. Keep unresolved or damaged signs
   open. Require the registered held-out score against the clear
   copy and the shuffled table before freezing a key.
4. Decode the two other letters with the frozen table. Compare
   independently transcribed sign sequences and see whether each
   result reads in its letter's clear context. Keep the clear notes
   under the c. 44r slip out of key derivation.

Model routing is pending. The repository names Opus for independent
transcription and Fable for recovery. Neither is available in the
active harness.
