+++
title = "Man'yōshū poem 9 (Nukata no Ōkimi) — the unread opening in man'yōgana"
slug = "manyoshu-poem-9"
kind = "fragment"
era = "7th century CE (poem); anthology compiled after 759 CE"
origin = "Japan (Asuka/Nara)"
language = "Old Japanese written in man'yōgana"
status = "unsolved"
confidence = "medium"
digitized = "https://jti.lib.virginia.edu/japanese/manyoshu/"
tags = ["japanese", "old-japanese", "manyogana", "orthography", "nankunka", "textual-crux"]

[scores]
mystery = 3
material = 2
solvable = 5
compute = 5
verifiable = 3
crowding = 2
+++

# Man'yōshū poem 9 (Nukata no Ōkimi) — the unread opening in man'yōgana

## What it is
Poem 9 of book 1 of the *Man'yōshū*, the first Japanese poetry anthology, compiled after 759 CE in twenty books with more than 4,500 poems, its final shaping usually credited to Ōtomo no Yakamochi. Poem 9 is attributed to Princess Nukata (Nukata no Ōkimi, active c. 630–690). Its opening is written 莫器圓隣之大相七兄爪湯氣 — twelve Chinese characters — and nobody knows how to read them. It is the most celebrated of the *Man'yōshū*'s *nankunka*, the poems whose graphs resist reduction to Old Japanese.

## What is unsolved
The phonetic and lexical value of those twelve graphs, and therefore what the poem's first line or two say. *Man'yōgana* uses Chinese characters in several incompatible ways at once — for their Chinese sound, for a Japanese word's sound, for the meaning of the Japanese word they gloss, and occasionally as rebus or as playful *gisho* spellings. A reading has to assign each of the twelve graphs to one of those functions, produce Old Japanese that is grammatical, and fit the metrical shape of the poem and its headnote context. Roughly fourteen distinct reconstructions are on record and some twenty scholars have proposed or argued about them, from the thirteenth-century monk Sengaku and the Edo philologists Keichū, Kada no Azumamaro, Kamochi Masazumi and Tachibana Chikage, through Omodaka Hisataka, Saitō Mokichi and Tsuchiya Bunmei, to Alexander Vovin in the present. None has been accepted.

## What survives
The anthology, complete, in a large medieval manuscript tradition; twelve graphs is all the primary evidence for the crux itself, but the surrounding evidence is unusually rich. Manuscript images are available from Waseda University Library, and the University of Virginia's Japanese Text Initiative hosts an electronic edition of the *Man'yōshū* with an interactive search over the text. What makes the problem tractable in principle is the corpus: more than 4,500 poems (265 *chōka*, 4,207 *tanka*, and other forms) written in the same orthography, which between them give an empirical distribution over the phonographic and logographic values of every graph the anthology uses. Alexander Vovin's complete annotated translation and commentary (2009–2022) is the most philologically explicit English treatment; Ian Hideo Levy's and Edwin Cranston's translations, and the 1940 Nippon Gakujutsu Shinkokai version, are the accessible ones.

## Prior attempts and current consensus
Every reading is a proposal about which graphs are phonographic and which logographic, and the field has cycled through the possibilities for 350 years without converging. Keichū's Edo-period work established the philological method; Omodaka's *Jidaibetsu kokugo daijiten: Jōdai-hen* and his *Man'yōshū* scholarship set the modern standard for what counts as an attested graph value; Vovin's commentary states the constraints most explicitly and, characteristically, declines to force a reading where the evidence does not support one. The consensus is that the line is unread, that some of the graphs are probably being used in a way not otherwise attested in the anthology, and that manuscript corruption cannot be ruled out for at least one or two of them. A newcomer reads the Nukata entry's tabulated proposals, then Vovin's commentary on book 1, then Omodaka for the graph values.

## What a solution would have to do
This is the tightest falsifiability clause in the catalog's non-Western set, because the constraints are enumerable. A reading must: (1) assign every one of the twelve graphs a function and a value, with each value attested elsewhere in the *Man'yōshū* or in contemporary Old Japanese material (*mokkan*, the *Kojiki* and *Nihon shoki* song passages, the Bussokuseki poems) — an unattested value is allowed only once and must be argued; (2) yield grammatical Old Japanese of the right period, with correct *kō-otsu* vowel distinctions where the graphs bear on them; (3) scan — fit the metrical template of the poem as a whole, which constrains the syllable count of the opening; (4) cohere with the rest of poem 9 and with its headnote, which situates the poem in an imperial progress; (5) explain *why* the poet or scribe chose these graphs, since a reading that is merely phonetically possible does not account for a spelling nobody else in 4,500 poems used; and (6) survive the manuscript variants — if a reading depends on emending a graph, it must say which witness supports the emendation. A probabilistic version of the same bar is what makes this the catalog's best small-scale compute target: enumerate all readings consistent with attested graph values, score them by an Old Japanese language model and by the metrical template, and report the posterior over readings rather than one more confident guess.

## Why the scores
- mystery 3: it is one poem, so a solution would not change a field; but it is *the* crux of Japanese classical philology and a solution would be a celebrated result within it.
- material 2: the object of inquiry is twelve graphs. The manuscript witnesses are many and the surrounding corpus is superb, but the rubric scores the surviving evidence for the thing in question, and that is almost nothing.
- solvable 5: Nukata wrote a determinate Old Japanese line and a Nara-period reader read it. There is no plausible hoax, noise or open-by-design reading.
- compute 5: the core question is combinatorial and the data is ready — a fully digitized corpus of 4,500 poems in the same orthography supplies the graph-value distribution, the metre supplies hard constraints, and nobody has run the systematic probabilistic search. Three and a half centuries of manual search over a small space is exactly the situation where an exhaustive scored enumeration is the obvious undone move.
- verifiable 3: the acceptance criteria are explicit and checkable (attested values, grammar, metre, context, graph-choice motivation), and a reading that met all of them could plausibly win the field within years; not higher because twelve graphs may admit more than one reading that satisfies every constraint.
- crowding 2: roughly fourteen published reconstructions by capable philologists over 350 years, all failed; the computational corner is untouched, which is the whole reason to score `compute` at 5.

## Sources
- PRIMARY — Japanese Text Initiative (University of Virginia Library), *Man'yōshū* electronic text with interactive search. https://jti.lib.virginia.edu/japanese/manyoshu/
- SECONDARY — Wikipedia, "Nukata no Ōkimi": the man'yōgana text of the opening 莫器圓隣之大相七兄爪湯氣, the statement that poem 9 is one of the most difficult in the anthology, the tabulation of roughly fourteen proposed readings, and the list of scholars who proposed or discussed them (Sengaku, Keichū, Kada no Azumamaro, Tachibana Chikage, Kamochi Masazumi, Omodaka Hisataka, Saitō Mokichi, Tsuchiya Bunmei, Vovin and others); Nukata's floruit c. 630–690. https://en.wikipedia.org/wiki/Nukata_no_%C5%8Ckimi
- SECONDARY — Wikipedia, "Man'yōshū": compilation after 759 CE, Ōtomo no Yakamochi as final compiler, twenty books and more than 4,500 poems (265 *chōka*, 4,207 *tanka*), man'yōgana and its difficulty, Waseda University Library manuscript scans, and the major English translations (Pierson 1929–63, Nippon Gakujutsu Shinkokai 1940, Levy from 1981, Cranston 1993, Vovin 2009–2022). https://en.wikipedia.org/wiki/Man%27y%C5%8Dsh%C5%AB

## Unverified claims
- The exact number of published reconstructions. The secondary source tabulates "approximately 14" and names about twenty people; the two figures are not the same thing and neither was checked against a Japanese survey of the *nankunka*.
- The content of the poem's headnote and the identification of the occasion (an imperial progress, often to the hot springs of Ki) were not verified in this pass, nor was the readable remainder of poem 9 — which is itself partly disputed.
- Which manuscripts (Genryaku kōhon, Katsura-bon, Nishi Honganji-bon) carry which variants of the twelve graphs, and whether any witness differs. The Wikipedia article on the anthology does not discuss the manuscript stemma; only that Waseda hosts scans.
- Which translation or text the Japanese Text Initiative edition provides, and whether it is the romanized original, the 1940 translation, or both; the site's editorial note was not read.
- Whether the Oxford Corpus of Old Japanese covers the *Man'yōshū* with graph-level annotation. This would materially affect how ready the data is for the `compute = 5` claim and was not confirmed.
