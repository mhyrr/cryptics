# Session prompt: the essay (es. 132 write-up for a general reader)

Paste everything below the line into a fresh session, from the repo root `/Users/mhyrr/work/cryptics`.

---

/focus vargas-mexia-es132

**Goal.** Write the one piece of finished prose this dive ends with: an essay for a general, curious reader about Philip
II's cipher letters to his ambassador in Paris, Juan de Vargas Mexía (BnF Espagnol 132, 1577–1580), and what they show
about the fall of Antonio Pérez. Then publish it. After it is published, the dive closes (`/session-close`, status
"written up").

## Why this piece exists (Greg's framing, keep it)
Greg had no idea this episode existed until we used the published cipher keys to read the letters. That surprise is the
engine of the essay: a file catalogued in 1844 as "imposible descifrar no teniendo la clave" turns out, read with keys
printed in 1950 and matched to it in 2020, to hold the King's own side of one of the great political scandals of Philip
II's reign. So the piece is **as much method as history, with the history in the spotlight**: the reader should come away
with the story *and* with a clear picture of how a locked file was opened, and what it means to be careful about it.

## Reader, form, length
- **Reader:** a general, curious, intelligent adult. Assumes no Spanish, no knowledge of Philip II beyond the name, and no
  cryptography. Think long-form magazine essay, not a paper.
- **Form:** one essay, about 4,000–5,500 words, in sections with short scene-like headings. Short Spanish quotations from
  the letters, each followed at once by an English rendering. Then a separate closing section, **"For historians and
  cryptographers"** (about 800–1,500 words): folios, ciphers, keys, method, reader agreement, external checks, walls,
  third-party readings, and where the data and scripts live. Notes: compact, numbered endnotes or inline folio cites; no
  footnote sprawl.
- **Register:** narrative and vivid, warm, exact. Not dry-direct (Greg's working register) and not flowery. Let scenes
  carry the argument. No agent-speak, no corporate cadence. Read `~/.hive/SOUL.md` (Voice) first; the "Claudish language"
  rules there apply in full.

## Read first (in this order; do not re-derive)
1. `puzzles/vargas-mexia-es132/OVERVIEW.md` — "The story" and §7 especially. This is the reference document and the
   factual backbone. The essay is *not* a rewrite of it; it is a different piece built from the same facts.
2. `canon.md` (what we hold true, with confidence levels), `hypotheses.md` (H3, H5, H6, H7, H16, H17).
3. `analysis/07-after-arrest/README.md` (Result section and Log) and `countersignatures.md`.
4. `analysis/06-premurder/README.md` (Result) and `teulet-check.md`.
5. `sources/paz-1579-1580.md`, `sources/history-2026-10-04.md`, `sources/context-research-2026-10-03.md`.
6. Greg's writing tools: `~/work/writing/.claude/commands/editor.md`, `~/work/writing/.claude/commands/slopwriting.md`,
   and the skill `deslopify` (`~/.claude/skills/deslopify/SKILL.md`). Read all three before drafting, so the draft is
   written to their standard instead of being repaired afterwards.

## The story beats (facts are in the files above; cite folios)
Use these as raw material, not as a fixed outline. Find the best order; a cold open is encouraged.
1. **The locked file.** Ochoa 1844: "imposible descifrar". Devos 1950 prints keys without knowing this volume; Tomokiyo
   2020 matches the four ciphers to it. A model-assisted project (cabinet-noir) posted readings in late Sept 2026; we found
   it only afterwards, and our readings are independent replications. Say so plainly; it is part of the method story.
2. **How a cipher like this works**, shown with one real line (OVERVIEW specimen: f. 81 "y por todas he visto lo que…":
   numbers for letters, marks for vowels and consonants, code signs for words). One short, concrete demonstration beats a
   paragraph of explanation.
3. **The secretary in the middle.** Pérez countersigns the King's letters; on 13 Jul 1579 the King writes "Antonio Perez me
   ha mostrado la carta…" (f. 215) and on 8 Jun Pérez receives Vargas's despatches (f. 206, cipher). Pérez's private
   channel: "solo venga en la [carta] particular … y con esta forma no avrá peligro" (f. 179, Jan 1579).
4. **Escobedo, 31 March 1578.** The murder, the suspicion, Pérez's later excuse (a Don John–Guise "confederation"
   denounced by Vargas). What the pre-murder letters actually show (24 Jan 1578, f. 12v: the Guises' dealings with Don John's
   envoy, "cosas que tienen mucha consideración"; no league or union before the murder). Mignet's verdict and where it
   holds.
5. **Don John's papers.** After Don John's death the King orders a secret inquiry: the papers, Guise's cipher "con mi
   hermano", "los 800 mill ducados", "sin que persona ninguna pueda entender que … es por orden mía" (ff. 123, 154).
6. **April 1579.** Pérez's ciphered self-defence to his friend (f. 198: "la demanda que Escovedo me puso", "el falso
   testimonio", the refused leave, the Archbishop and the Princess of Éboli), set against the King's own note of the same
   month ("os aquieteis y sosegueis", Mignet p. 120 n. 2). Two independent texts, the same words.
7. **28 July 1579, and after.** The arrest. The next letter (24 Aug, f. 218, clear): no countersignature; Vargas's letters
   "han venido a mis manos"; wait in Paris for "don Juan [de Idiáquez]". Three weeks later Idiáquez countersigns as
   Pérez's successor. By October letters go "a mis manos, como a las de Çayas". Pérez is never named again, in a run of
   letters read in full by two blind readers each.
8. **The leaks.** 13 Sep 1579: where does Saint-Goard get his news "de las cosas de acá", and if the informant "le huviere
   nombrado o dado más señal". 29 Nov: a paper passing in Paris as the Council of War's opinion on seizing Portugal is "del
   consejo no lo es" but one of the private opinions written for the King — "por qué vía y medio ha ido a parar allá este
   papel". The paper itself is listed in Simancas (K 1554–55). Vargas, Pérez's friend, cuts him from his will in 1580 and
   dies that year; his executors are told to keep the embassy papers "sin comunicarlos a nadie" (Paz).
9. **What the letters cannot tell us.** Who killed Escobedo is not really in doubt (Pérez's men, on an order the King
   later admitted); why is the contested part, and these letters do not reach it. Silence is a finding about what the King
   chose to write, not proof of what Vargas knew.

## Honesty rules (non-negotiable; this is AGENTS.md rules 1–3 in prose form)
- Every factual claim traces to `canon.md`, the OVERVIEW, or a cited source. Do not add history from memory. If a fact the
  story needs is not in the files, verify it with a fetch and cite it, or leave it out.
- Keep confidence visible without hedging every line: say once, early and plainly, that the readings are model
  transcriptions not yet checked by a human paleographer, and that duplicates and printed drafts were used as checks
  (Teulet minute 77–82%; Mignet passages; Paz's summaries; cabinet-noir 76–95%). After that, write with confidence and mark
  only the genuinely uncertain points.
- **Candidates stay candidates.** "Consejo" as the unread word of the 13 Sep leak passage is a candidate (one spelled
  duplicate). The Quiroga–Éboli episode rests on our f. 198 reading alone. "Arcauti", "the Theatine", who has "mucha
  occupación" in f. 179: open. Say so where they appear, or leave them out.
- Known corrections, do not reintroduce: the archbishop of 13 Sep 1579 is Cambrai (not Embrun); "milord Bretón" is milord
  Hamilton; f. 275 was sent *to* Vargas; the countersignature is Idiáquez (readers' "Eraso" was a misreading); f. 273 is a
  Savoy memorial copy.
- Do not imply a decipherment "first". The readings are independent replications with published keys; cabinet-noir read
  some of these letters first. What is new here is the synthesis (the pre-murder chronology, the April 1579 pairing, the
  after-arrest record) and the method's discipline.
- Do not speculate that Pérez was the leaker. You may note that the King hunted leaks in the months after Pérez's fall and
  that the letters name no one; let the reader feel the question without an answer the evidence does not give.

## Voice: what to avoid (from SOUL.md, editor.md, slopwriting.md)
No "it's not X, it's Y" antitheses; no punchline em-dashes; no three-item rhythm by reflex; no closing tautologies; no
announced significance ("importantly", "the key insight"); no "load-bearing", "robust", "comprehensive", "delve", "tapestry",
"testament to"; no mechanical sentence rhythm; no section that ends by summarizing itself. Vary sentence length on purpose.
Prefer the concrete noun and the scene to the abstraction. Let quotations do work.

## Process (do it in this order; each step is a checkpoint)
1. **Outline first, then stop.** Write `puzzles/vargas-mexia-es132/essay/OUTLINE.md`: working title (2–3 options), the
   cold open in two sentences, section list with the one scene and the one quotation each section turns on, and the
   specialist section's headings. **Show Greg the outline and wait for his approval** before drafting. (He approves
   section by section; take his notes literally.)
2. **Draft** `essay/DRAFT.md` in one pass, section by section, with folio cites inline as `(f. 218)` and a short notes
   list at the end. Keep a sidecar `essay/CLAIMS.md`: every factual sentence's source (canon line, OVERVIEW section,
   file:line, or URL). A claim without a source is cut.
3. **Editor pass (critic, not co-writer).** Spawn one subagent (Opus, no sub-agents of its own) whose instructions are
   `~/work/writing/.claude/commands/editor.md` verbatim, applied to *your* draft: it reads for register, flags the leaks,
   the places that shrank, and the lines worth protecting, and reports — it does not rewrite. (editor.md says "don't draft
   for me"; here you are the writer, so its notes come to you and you make the changes in your own words.) Save its report
   as `essay/EDITOR-NOTES.md`. Revise.
4. **Slop pass.** Run the checks in `~/work/writing/.claude/commands/slopwriting.md` and the `deslopify` skill against
   `essay/DRAFT.md` (deslopify is written for non-essay prose; use its audit and catalogue as a detector, and fix the hits
   yourself so the voice stays one voice). Record what changed in `essay/EDITOR-NOTES.md`. Changes of wording only; no claim
   may change in this pass.
5. **Fact pass.** Walk `CLAIMS.md` against the draft once more: every quotation exact as in the decodes/canon (spelling as
   in our readings), every date and folio right, every candidate marked. Fix or cut.
6. **Show Greg the full draft.** Apply his notes.
7. **Publish.** Ask Greg once whether he wants it as a page (Artifact, alongside the OVERVIEW) or as a doc he can comment
   on; default to a page. For a page: run the Artifact `quickstart` with intent "document" first and follow what it
   returns; build from `essay/DRAFT.md` (a small builder like `overview-build/build.py` is fine, or reuse it with a new
   template); keep the OVERVIEW's palette and typography family so the two read as a pair; link each to the other. The
   OVERVIEW stays the reference; the essay links to it for detail.
8. **Close.** Commit by file. Update `NEXT.md` (dive status: written up; what a future session could still do: Simancas
   K 1554–55/1557 requests, a human paleographer, the f. 273 second reader), `NEXT-SESSION.md`, the HIVE ticket TK-007 note,
   and run `/session-close`.

## Specialist section ("For historians and cryptographers") must contain
- The volume, shelfmark, Gallica ark; the four ciphers, who printed and matched each key (Devos 1950, Alcocer 1921 for the
  Cp.30 nomenclature, Tomokiyo 2020), and our extensions with their held-out results (2H = que, Σ = o, H = ne, cross
  doubles; "u." = que; 35 = pr / underlined 35 = pl).
- The method: blind Sonnet transcriptions from page images, decoders frozen by commit before use, duplicates as second
  witnesses, decoded-text agreement figures, the reader-prompt lesson (second pass enforced).
- External checks: Teulet vol. 5 pp. 213–214 minute (77–82% vs controls 28–41%); Mignet's printed passages; Paz's Simancas
  summaries; third-party comparisons (cabinet-noir medians 76–95%; pangoleen 91–95%).
- The walls: no human paleographer; Vargas's own dispatches (AGS Estado K 1544–1558) seen only through Teulet's excerpts and
  Paz's summaries; ff. 26v–31r unscanned; the candidate "Consejo".
- Where everything is: the repository paths for transcriptions, decoders, outputs, and the OVERVIEW link
  (https://claude.ai/artifact/BSsgyjHHehAd9nA3zLWBi2).

## Rules
AGENTS.md throughout. The essay adds no new findings; if drafting surfaces a question the files cannot answer, note it in
`NEXT.md` and keep writing around it. Do not spawn reader agents. One editor subagent only. Do not publish before Greg has
seen the outline and the full draft.
