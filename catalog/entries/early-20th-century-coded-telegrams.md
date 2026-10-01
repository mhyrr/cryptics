+++
title = "Unread coded telegrams, 1911–1937: Lüderitz consulate (1911), a Japanese telegram printed by Yardley (c. 1920), and the 'BLUME SALAMANCA' telegrams from Zurich (1937)"
slug = "early-20th-century-coded-telegrams"
kind = "cipher"
era = "1911–1937"
origin = "Lüderitz (German South-West Africa) to London; Tokyo (Japanese Foreign Ministry); Zurich to Salamanca via London"
language = "English (Lüderitz, presumed); Japanese (Yardley specimen); Spanish (Zurich, inferred from letter statistics)"
status = "unsolved"
confidence = "medium"
digitized = "https://cryptiana.web.fc2.com/code/unsolved.htm"
tags = ["telegram", "codebook", "transposition", "diplomatic", "20th-century", "Yardley", "Spanish-Civil-War", "Cryptiana", "Cipherbrain"]

[scores]
mystery = 2
material = 4
solvable = 5
compute = 4
verifiable = 5
crowding = 4
+++

# Unread coded telegrams, 1911–1937

## What it is
Three unrelated telegrams, or pairs of telegrams, from Satoshi Tomokiyo's Cryptiana list ("Telegraphic Age"). They are grouped here because each is a single short telegraphic text whose system is unknown or only partly known.

1. **Diplomatic telegram from the British consulate at Lüderitz (1911).** A coded telegram of 9 October 1911 from the British consul at Lüderitz, then in German South-West Africa, to the Foreign Office in London (telegraphic address "Prodrome"). Tomokiyo counts **43 five-figure groups** ("68195 71235 …"). Klaus Schmeh's post, which publishes the image, gives 47 chargeable words. The two counts are not reconciled; the difference may be address and signature words.
2. **Japanese coded telegram printed by Yardley (c. 1920).** Herbert Yardley printed it in *The American Black Chamber* (1931), p. 251, as a typical Japanese diplomatic code message. The sender appears to be Foreign Minister Uchida Kōsai (in office 29 September 1918 – 2 September 1923). Tomokiyo notes that calling it "unsolved" may be inaccurate: Yardley's Cipher Bureau, which broke Japanese codes Ja, Jb, Jc… from December 1919, probably read it at the time. What is open is only that no decode of *this* message has been published.
3. **"BLUME SALAMANCA" telegrams from Zurich (8 January 1937).** Two telegrams sent from Zurich via London (one marked *via Angleterre Eastern*) to "Blume, Salamanca". Salamanca was Franco's headquarters in January 1937. The historian Regula Bochsler found them in Swiss Federal Police files on Werner Oswald, founder of the Emser Werke (*Nylon und Napalm*, 2022). Oswald told police they concerned "wool business" in Spain, and Bochsler doubts it. Schmeh posted them on Facebook. Daniel Bourdeau reports that telegram 1 has 123 five-letter groups (615 letters) and telegram 2 has 32 groups (160 letters). Cryptiana's summary says "from Switzerland to London"; the address shows Spain as the destination and London as a relay.

## What is unsolved
- Lüderitz: the plaintext and the code used. It is presumably a Foreign Office or consular figure code, possibly superenciphered. A Cipherbrain commenter argued that group 99251 rules out a standard commercial codebook.
- Yardley specimen: a published plaintext for this specific message. The code family is known.
- Zurich: the plaintext, and the transposition keys. Tomokiyo notes that the index of coincidence matches a natural language and suggests transposition. Bourdeau's measurements (IC ≈ 0.070, no q, k, w or x) point to transposed Spanish.

## What survives
- Lüderitz: a photograph of the telegram form published on Cipherbrain (2016). The National Archives file reference was not found.
- Yardley: the printed specimen in *The American Black Chamber* (1931; reprinted 2004). Tomokiyo has reconstructed parts of the Japanese codes of the period from Yardley's working sheets and from Japanese archival plaintexts, in a separate Cryptiana article.
- Zurich: images of both telegram forms from Schmeh's Facebook post. One of them was reachable only by a time-limited image-server URL. Bourdeau and Richard Bean have independent transcriptions that agree letter for letter (SHA-256 published).

## Prior attempts and current consensus
- Lüderitz: Cipherbrain readers discussed it in 2016 (Karsten Hansky, Tobias Schrödel); no solution.
- Yardley: no modern attempt known. Tomokiyo's work on Yardley's Jp code (1921) is the closest.
- Zurich: Tomokiyo's blog (2023) ruled out the British Government Telegraph Code. Bourdeau (September 2026), working on telegram 1, excluded every single transposition and every double columnar transposition whose second key is ten letters or fewer, with planted controls. He left double columnar with two long keys open, and as of 30 September 2026 a joint attack on both telegrams was under way. Lasry, Kopal and Wacker broke a published double-transposition challenge with long keys by divide-and-conquer hill-climbing (*Cryptologia* 2014). That method exists, and nobody has yet reported applying it here.

## What a solution would have to do
- Lüderitz: identify a codebook that was actually in Foreign Office or consular use in 1911 (and any additive), and decode all 43 groups into an English consular report consistent with October 1911 Lüderitz: the diamond fields, shipping, German colonial administration. The same procedure should then read other telegrams of that code.
- Yardley: decode with a reconstructed Japanese code of 1918–23 into Japanese that is consistent with Uchida's known instructions. Ideally it matches a plaintext in the Japanese Foreign Ministry records (JACAR).
- Zurich: give one pair of keys per telegram, or a shared key, that turns all 615 and 160 letters into continuous Spanish (or the language actually used), without residual unexplained letters. The content must be checkable against Oswald's documented business and the Nationalist side's 1937 procurement. A key that reads only a fragment is not a solution.

## Why the scores
- mystery 2: each is a single unread telegram of specialist interest. The Zurich pair touches a documented historical question, whether a Swiss industrialist supplied Franco's side, and could have gone to 3; it is held at 2 because the question is a footnote, not a known controversy.
- material 4: all three texts are complete and published as images. None has an archival scan with a shelfmark that was verified here.
- solvable 5: state or commercial telegraphic systems in real use.
- compute 4: the Zurich telegrams are a genuine computational problem (double transposition, 775 letters across two messages, an established hill-climbing method), and that member drives the score. The other two would score 2–3 alone: Lüderitz is one short code message (code, not cipher; the codebook must be found, not computed), and Yardley's message needs a partially reconstructed codebook.
- verifiable 5: a continuous decode in the expected language is a mechanical check for all three.
- crowding 4: blog-level attention only, plus Bourdeau's 2026 sessions on the Zurich pair.
- compute mode: HILL-CLIMB (double columnar transposition, Zurich) · CODEBOOK-SEARCH (Lüderitz, Yardley) · verifier MECHANICAL · space SAMPLABLE · signal YES (Zurich), WEAK (others) · fit HIGH (Zurich), LOW (others).

## Sources
- SECONDARY — Satoshi Tomokiyo, Cryptiana, "Unsolved Historical Ciphers," sections "A Diplomatic Telegram from British Consulate in Africa (1911)", "Japanese Coded Telegram Decoded by Yardley (c. 1920)", "A Telegram from Switzerland (1937)". https://cryptiana.web.fc2.com/code/unsolved.htm
- SECONDARY — Satoshi Tomokiyo, Cryptiana, Japanese codes broken by Yardley's Cipher Bureau (Ja, Jb…; December 1919 break). https://cryptiana.web.fc2.com/code/meiji.htm
- SECONDARY — Satoshi Tomokiyo, Cryptiana, "A Specimen of Yardley's Deciphering of Japanese Diplomatic Code Jp (1921)." https://cryptiana.web.fc2.com/code/yardley.htm
- SECONDARY — Satoshi Tomokiyo, "A Telegram from Switzerland (1937)," Cryptiana blog, September 2023 (IC, BABY code ruled out, Bochsler/Oswald background). https://cryptiana.blogspot.com/2023/09/a-telegram-from-switzerland-1937.html
- POPULAR — Klaus Schmeh, "Wer löst dieses verschlüsselte Telegramm aus Deutsch-Südwestafrika?" Cipherbrain, 15 January 2016 (date 9 Oct 1911, image, comments). http://scienceblogs.de/klausis-krypto-kolumne/2016/01/15/wer-loest-dieses-verschluesselte-telegramm-aus-deutsch-suedwestafrika/
- POPULAR — Klaus Schmeh, Facebook post with the two 1937 telegrams. https://www.facebook.com/schmeh/posts/pfbid02Rx2o5U1eUeHimutNMuGrq5zD2eWY7gppKJyVW2DxautiGDnQKMxMfw1hRDCQP6ebl
- CLAIMANT — Daniel Bourdeau, "BLUME SALAMANCA" notes (transcription, 615 + 160 letters, exclusions, destination Salamanca). https://github.com/dbourdeau/cyphersolver/tree/main/targets/blume/
- SCHOLARLY — George Lasry, Nils Kopal and Arno Wacker, "Solving the Double Transposition Challenge with a Divide-and-Conquer Approach," *Cryptologia* 38(3) (2014), 197–214. https://www.ingentaconnect.com/content/tandf/crypt/2014/00000038/00000003/art00001
- POPULAR — Herbert O. Yardley, *The American Black Chamber* (1931), p. 251 (the specimen); not consulted directly.

## Unverified claims
- 43 groups (Tomokiyo) against 47 chargeable words (Schmeh) for the Lüderitz telegram; not reconciled here.
- The National Archives (Kew) file holding the Lüderitz telegram, and whether a Foreign Office codebook of 1911 survives there.
- That Yardley's bureau actually read the p. 251 message (Tomokiyo: "probably"). Also whether a plaintext survives in the Japanese Foreign Ministry records.
- The Zurich telegrams' language (Spanish) is an inference from letter statistics by Bourdeau, not established.
- The length of the 2013 double-transposition challenge and its key lengths, recalled as about 600 letters with keys over 20; not checked in the paper.
- Whether any of the three has been solved since September 2026; Tomokiyo's notice says he is behind in recording solutions.
