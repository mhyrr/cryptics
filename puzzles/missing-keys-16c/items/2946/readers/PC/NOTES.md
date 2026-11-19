# Reader PC — item 2946/2947 plain text and gloss — notes

## Line counts and how they were counted

- **2947-693: 46 letter lines.** I counted on the page image first: a dense block from y about 220 to 1595 at a pitch of about 30 px, and (1595-220)/30 + 1 = 46. Then I counted band by band on the strips b01–b14, using the ruler to drop each repeated line. b14 shows only the bottom of L46 and blank paper. The line above L01 ("ne pareria verisimile ... ge provedera") is in the gloss hand, so I counted it as L01's gloss row, not as a line.
- **2947-694: 21 letter lines.** L01–L16 are the letter block, L17 is the year "1439", L18–L19 are the signature, L20–L21 are the address ("Magnifico Amico ... / Cosme de Medicis"). The strips stop at about y 820, so I read the signature and address from the page image only. Their y values are page-image pixel rows, not ruler readings. Drop L18–L21 if signature and address lines are not wanted.
- **2946-c215: 21 letter lines.** L01–L18 are the letter, L19 is the dateline ("Ex Sablo die xxiiij ... 1439"), L20–L21 are the signature. The signature lies below the strips, so its y comes from the page image.

## The ruler and y values (systematic doubt)

- Each ruler number is printed about 20 strip px **below** its tick. On 2947-693 and 2947-694 I read y from where the numbers sit, so those y values may be about 5–15 px off (mostly low on the upper bands). On 2946-c215 I worked y out from the tick positions (the band starts at 190, 300, 410 ...), so those values should be closer. Line order and numbering are not affected.
- The left (L) and right (R) halves overlap by about 1630 strip px. I checked for gloss words seen in both halves (for example "che" on 694 L04/L11 and "una" on 694 L05) and kept each one once.

## Second pass / enlargements

I made enlargements with `magick` (in `crops/`) of every gloss row I was unsure of. These are 2–4× enlargements of the same pixels: the page JPEG is only 1272 px wide, so enlarging gives no detail the strips lack. Many gloss words stay doubtful for that reason, and I marked them `[?]` or `[...]` rather than guess.

## Conventions I applied

- Number-like signs inside cipher runs (19, 94, 46, 47, 77, 79, "x||", "ʒ" and similar) are counted as cipher signs, not transcribed. Several look like roman numerals: 693 L26 "χ||||" with gloss "ducati" over "ag" next to it, and "⌶⌶|" (xxi?) on 693 L24/L32/L46 and c215 L13. The guide treats signs as signs, so these are not transcribed. The checker may want to look at them.
- **693 L36 ".XII."** is written with dots like a clear roman numeral, so I wrote it as clear text with `[?]`. The ".M." inside 694 L10 and c215 L01 has the same dotted form, but I left it inside the cipher run.
- "dx"/"ch" with an abbreviation stroke is written `ch(e)` (693 L03, L22, L34; 694 L03, L09; c215 L02, L07, L11). 693 L45 "ch(e)l".
- A run is split only where clear words or a very wide gap divide it. A gloss phrase that runs over several sub-stretches of one run goes into that run's braces.

## Gloss placement doubts (2947-693)

- L01: the gloss row above L01 is written over the top line and may be read as a heading. Its wording is doubtful: "ne[?] pareria[?]" could be "die parerna".
- L04/L05: "dimostrarne" sits at the right, level with the end of L04, but it is lighter and smaller, and it lies over the run of L05. I gave it to L05. "lafede et" is in the main hand at the end of L04.
- L05: "li" at the left edge, before "servidori", is in lighter or reddish ink. It may be a later addition or in the gloss hand.
- L06, L08, L09, L10, L12, L13, L29, L34, L43, L44: I recorded words written to the right of where the cipher ends, level with the line, as `{margin: ...}`. 693 L06 "cevario[?] ipropezando[?]" is uncertain both in reading and in hand. It is close to the main-hand size.
- L14/L15: "e che non siamo messi" lies between L14 and L15, beyond the end of L14. I gave it to L15 as gloss. It could be a margin gloss of L14.
- L18: a small "H" stands above the line, roughly over the run at its middle (L-half x about 1370). It looks like a sign written above the line, not a gloss word. I did not transcribe it.
- L20/L21: "ne pare comprendere" lies between L20 ("Ma ad alcun") and L21. I gave it to the last run of L21 ("Et ogni di [cipher]"). It could be L20 margin.
- L23: "q(ue)l[?] <struck>m</struck> la necessitude[?]" lies below "Eben ch(e) al p(rese)nte" (L22) and above the right end of L23. The struck "m" and "ql" may be in the **main hand** (a correction) rather than the gloss hand. I placed them with L23's gloss.
- L29: a small "ph" stands above and right of the last run. It is unexplained and recorded as margin.
- L36: the gloss "a ducati" lies over ".XII." and the run after it. I gave it to the run after ".XII.".
- L39/L40: "coel questo[?]" lies between the lines. I gave it to L40.
- L43: "[...] provedesse" at the right margin. L44: "p(er)che[?]" at the right margin may be main hand.

## Doubtful words (2947-693), by line

L01 ne pareria; L02 pecha (pratica?), danari, a tanto; L03 passione, altre, magiore, il a despacele, alcuno; L04 venire, fusse, el fiate; L05 forsi; L06 first gloss word unread, voole; L07 ele, Di cittadi (cittadini?), dele venture, "[...]quali" (s- or li-quali); L08 Bologna, a [...], anne, atrabuirecelo; L09 ardimento, o posse, con rasone; L10 oltra, malitia, "[...]duramento"; L12 "et" before honestamente (a tironian sign or a cipher sign?), falso, p(er) securezze; L13 tracti, the word after multe, da loro, forma de [...]; L14 dello; L15 vostri, externamente; L16 the last word "re[...]are" (remunerare / renunciare?); L17 "la [...]tione", p(ro)missione; L18 the end of the gloss "de [...]"; L19 merchi, tel; L22 sig(nore), disfacto; L23 almost every word; L25 a, siamo, vuoleno, altro; L27 principio; L28 ducati, nonche, suxo; L30 vostre; L32 two words unread; L33 "ca[...]", p(er)le tempo; L35 in fatto, possibile, vuxia, de me; L36 ricatarne, non in, a; L37 la; L38 tanti, signi, cavamo; L40 vacuo, questo; L41 p; L42 la informatione; L43 anchora; L44 si par[...]; L45 prexio, ch(e)l fine; L46 sene, vigniria, quello.

## Doubtful words (2947-694)

- L01: the first gloss word is unread (something like "cefarui"). "Cossi dui[?]" is main hand. "arditamente ve possemo" is doubtful.
- L02 tentatione, vostre, ella; L03 the first gloss word "[...]ndo", trovaresti; L04 se vedera; L05 gita, extima, a small word at the right "[...]"; L06 videla.
- L07 "dexe[?] le" (deze/dize?); L08 "possia[?]", the gloss "sper[...]"; L09 "s(i)[?] le terre"; L10 altri, nostri; L11 "be(n)", the gloss mostly unread ("che [...] e della cura"); L12 "ch(e)[?] vogliati" (ce?), chavezza; L13 di, dio; L14 "m(er)ita[?]".
- L16: "Ad grata parat(a)" (parati?). "Ex sito felia" (the place name is doubtful). L19 "et c(etera)".
- Hand: the gloss on 694 L14 "no ce porria fare cosa de" runs past the end of the cipher into the margin.

## 2946-c215

- **No gloss found.** I saw no small interlinear words on any band.
- Doubts: L05 and L06 "Spect(abi)le" (written with a suspension); L06 "cotta[?]" (costa?), "hav(er)e[?]"; L09 "c(om)p(re)hende[?]", "tutavia[?]"; L11 "c(on)ductieri[?]", "Acio[?]" (written something like "Aao"); L14 "la .[...]. vostra" (a dotted abbreviation that might be M(agnificentia) or S(ignoria), not resolved); L19 "Januarij[?]".
- L07 "et" is the tironian sign (like a "2"). L12 "Et" at the end of the line is main hand.

## Hand and ink

- On 2947-693 and 2947-694 the gloss is in one smaller, lighter brown, cursive hand throughout. Places where it might be a different hand or the main hand: 693 L05 "li" (reddish ink at the margin); 693 L06 margin "cevario ipropezando" (larger, closer to the main hand); 693 L23 "ql" and the struck "m"; 693 L44 margin "p(er)che". I saw no clear second gloss hand. On 693 L32/L33 (right half, around x 1500–1750) there are purple-tinted marks, possibly a later stain or ink, near "e la [...]" and "p(er)le tempo".
