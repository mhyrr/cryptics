+++
title = "Encoded letter to General Marmont, March 1809 (listed as 1807; solved 2026) — calibration case"
slug = "marmont-letter-1809"
kind = "cipher"
era = "March 1809 (long misdated 1807); solved September 2026"
origin = "French Empire: Eugène de Beauharnais's headquarters (Army of Italy) to Marmont in Dalmatia"
language = "French"
status = "solved"
confidence = "medium"
digitized = "https://carter.church/writeups/the-letter-to-marmont/"
tags = ["calibration", "solved", "homophonic", "Napoleonic", "letters", "simulated-annealing", "AI-assisted", "Cryptiana"]

[scores]
mystery = 1
material = 4
solvable = 5
compute = 5
verifiable = 5
crowding = 4
+++

# Encoded letter to General Marmont, March 1809 (listed as 1807; solved 2026) — calibration case

## What it is
A single letter to Auguste de Marmont, then commanding the isolated French corps in Dalmatia. Only its opening line is in clear: "Vous avez du recevoir Monsieur le General Marmont mes lettres des 8.14 et 20 courant." The rest is a cipher of two-digit figures, letters and arbitrary signs. It was known only from a plate in J. Vilcoq, "Le Chiffre sous le Premier Empire," *Revue historique de l'Armée* no. 4 (1969). Cryptiana listed it as "Encoded Letter to Marshal Marmont (1807)." Tomokiyo noted that Marmont used "a relatively simple code of 150 entries in 1811," so this "would not be a very complex system." On 20 September 2026 Carter Church reported a solution to Tomokiyo, and Cryptiana now marks it Solved. Church redates the letter to March 1809, in the weeks before Austria invaded Bavaria on 10 April.

## What is unsolved
Nothing in substance. Church lists five signs as still ambiguous, all affecting wording rather than sense: "Sa Majesté" vs "l'Empereur", "de" vs "dans", whether "canailles" is singular, and two preposition or article variants. The entry is kept as the catalog's first calibration case for an AI-assisted solve. It records exactly which steps the model did and which the earlier human work had already done.

## What survives
One witness: the 1969 plate. The writeup says Persée has digitized the plate and serves it at 1,202 × 1,836 pixels. No archive shelfmark for the manuscript (presumably at the SHD, Vincennes) is given in any source read here. Church's figures: about 1,300 cipher units drawn from 155 distinct signs. The transcription started with 175 provisional sign labels, which were then reconciled down.

## Prior attempts and current consensus
**What prior human work supplied:**
- Vilcoq (1969) published the plate, the only ciphertext anyone has.
- Daniel Tant (via ARCSI) published 33 letter values. Church says these cover about 435 units, roughly 33% of the text. Every word-sign was still blank. The brief's "33 symbols" means 33 letter values out of 155 signs, not a 33-symbol cipher.
- Tomokiyo listed the letter and pointed out its likely kinship with Marmont's small 1811 code.

**What the model (OpenAI's GPT-6 "Astra") did, according to Church, in about six hours of model run time:**
- Cut the plate image into row crops.
- Transcribed the signs and reconciled handwritten variants into one sign inventory.
- Started from Tant's 33 values and ran a simulated-annealing solver, scored on French 3- to 5-gram statistics, to assign the other ~122 signs. This step is ordinary homophonic cryptanalysis; it is the model running a classical algorithm, not the model reading French.
- Identified 29 whole-word signs, the nomenclator part.
- Checked every sign against the plate images.

**What Church says he did:** research design, the historical context and redating, and verification against outside sources.

**Verification offered:**
- The plaintext reports French and allied army positions across Europe and names commanders by title (Duke of Danzig, Prince of Ponte-Corvo).
- It matches Napoleon's order of 16 March 1809 to Eugène, printed in *Correspondance de Napoléon Ier* vol. 18 (1865). That order tells Eugène to send Marmont, in cipher, the positions of seven armies, and the decipherment gives the same armies with the same force figures in the same order.
- Marmont's *Mémoires* vol. 3 print Eugène's letters of 8, 14 and 20 March, the ones the opening line refers to.

**Independent verification:** the only outside check found is that Tomokiyo reviewed the solution and marked the entry Solved (RuntimeWire, 1 Oct 2026, citing Church). Nobody has published a re-decryption from the plate, and no peer-reviewed treatment exists. RuntimeWire itself calls the result "a worked example of AI-assisted archival research, not evidence that a model independently authenticated the document."

Consensus: accepted as solved by the list's maintainer. The match to the 16 March 1809 order is strong external evidence.

## What a solution would have to do
1. Give one sign-to-value table that reads all ~1,300 units as continuous French, and that someone else can reproduce from the plate.
2. Agree with the 33 values Tant published independently.
3. Explain the opening line's "8, 14 et 20 courant" with a date the content supports.
4. Match surviving outside documents.

Church's claim meets points 1 to 4 as he states them. What has not been done is point 1 by a second party: no independent re-transcription and re-solve from the plate has been published. The 29 whole-word signs and the 5 ambiguous signs are where judgment enters, and judgment is where a model's knowledge of the 16 March order could leak into the reading. The letter-level annealing result is the mechanically checkable part.

## Why the scores
Scored as the letter stood before September 2026, except mystery.
- mystery 1 today. Before the solve it would have been 2: one military dispatch whose general content (army positions passed to Marmont) can be inferred from Napoleon's surviving order.
- material 4: one complete witness, digitized, but only as a 1969 journal plate. The manuscript itself has not been located.
- solvable 5: a period army cipher with a 150-entry relative in use two years later, and a third of its values already published.
- compute 5: a homophonic cipher of ~155 signs and ~1,300 units in known French is exactly what n-gram hill-climbing is for. Tant's partial key made it easier.
- verifiable 5: continuous French plus a match to an independently printed order. Mechanical.
- crowding 4: not untouched, since Tant had a partial key and Cryptiana listed it, but no full attempt had been published.
- compute mode (retrospective): ENUMERATE (homophonic annealing seeded with a partial key) · verifier MECHANICAL plus an external-document match · space SAMPLABLE · signal YES · fit HIGH.
- Calibration point: the rubric's compute = 5 called this right. The genuinely new step was not the cryptanalysis, which is a 1990s-era method, but having a model do the image segmentation and sign transcription from a poor plate. That is the step that has kept short Cryptiana-list items unsolved. Many other Cryptiana entries share this shape (one plate, a small cipher, partial values published), so the catalog should expect more solves of this kind.

## Sources
- CLAIMANT — Carter Church, "Breaking the Marmont Cipher, 1809" (Sept 2026). Source of the 1,300 units, 155 signs, Tant's 33 values covering 435 units, the AI/human split, annealing on 3–5-grams, the 29 word-signs, the five ambiguous signs, the 1809 redating, and the matches to the *Correspondance* and Marmont's *Mémoires*. https://carter.church/writeups/the-letter-to-marmont/ (Cryptiana links the same writeup at https://carter.church/signals/the-letter-to-marmont/)
- SECONDARY — Satoshi Tomokiyo, Cryptiana, "Unsolved Historical Ciphers," entry "Encoded Letter to Marshal Marmont (1807) — Solved" (the Vilcoq citation, the opening line, the 150-entry 1811 code, Church's notification of 20 Sept 2026 and the 1809 correction). https://cryptiana.web.fc2.com/code/unsolved.htm
- SECONDARY — Tomokiyo, Cryptiana, "Napoleonic ciphers" (Marmont's 150-entry code of 1811 and the 1812 PARES decipherment). https://cryptiana.web.fc2.com/code/napoleon2.htm
- POPULAR — RuntimeWire, "GPT-6 Astra helped decode a 217-year-old cipher letter to Napoleon's marshal" (1 Oct 2026; Tomokiyo's review; "not evidence that a model independently authenticated the document"). https://runtimewire.com/article/gpt-6-astra-marmont-cipher-carter-church
- POPULAR — AOL, "Napoleon's 217-year-old coded message 'cracked by AI'." https://www.aol.com/articles/napoleon-217-old-coded-message-131452000.html
- PRIMARY (not opened) — J. Vilcoq, "Le Chiffre sous le Premier Empire," *Revue historique des Armées* 25 (4) (1969), pp. 22–27, with a plate after p. 24; reported to be on Persée.

## Unverified claims
- That Persée has the Vilcoq plate: from Church's writeup only, not opened here.
- Whether Church has published his transcription, sign table and solver code so that someone else can rerun them. Not established here.
- Daniel Tant's 33 values: the ARCSI publication was not read. The figures come through Church.
- The archive shelfmark of the original letter.
- The "155 distinct signs" reported against the "175 provisional labels": reported by Church, not reconciled here.
- The model's name and version ("GPT-6 Astra") come from Church and the press. Whether the model also had the historical sources in its context during the 29 word-sign assignments is not stated in what was read.
