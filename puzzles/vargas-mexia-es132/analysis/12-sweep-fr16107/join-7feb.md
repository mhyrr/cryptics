# Join test: which 7 Feb 1580 cipher letter owns the decipherment at fr. 16107 ff. 48r–50v?

Known-plaintext check, done by eye against Mousset 1912 pp. lviii–lix (SCHOLARLY) and the Reader C sign list in
`analysis/10-saint-goard/GUIDE.md`. Bar, fixed before reading: a match needs at least 15 consecutive plaintext
letters that agree with the key values, nulls aside. Crops: `sources/cache/fr16107/feb7/{a,b,m,d55}*.jpg`, cut from
`full/vNN.jpg` with a variant of `bands.py` (page fraction crop). Tokens follow `readerC/*.txt`: `·` = null, `?` = unread.
These readings are by eye, from a single pass. Nothing here was computed (rule 6): this is a join test, not a statistic.

Sign values this test fixed or confirmed:
- curl with a tail (`ϱ`, Mousset's s with the small loop on top) = **s**
- linked `oo` = **d** (Mousset's d), not l
- `∂` (d with a flourish) = **z**
- `δb` double loop = null

## Decipherment sheet: opening (main thread) and last six lines (view 55 L, f. 50v, upper 40%)

Opening (v52R-1): "Ilz sont [Sire?] bien estonnez d'entendre que le peuple de Portugal se soye si fort [..] …"
("They are, [Sire,] much astonished to hear that the people of Portugal should have so [..] …")

Last six lines. My reading is poor: the hand is fast, and `[?]` marks words I could not read.
1. "domassile(?) comme [?] que [?] toute(?) il le pourroit(?) avoir luy en Portugal" ("… as … that … he could have him in Portugal")
2. "ou il s'establiroit facilement les [?] que V[ost]re Ma[jes]te verra(?) que la" ("where he would easily establish himself … that Your Majesty will see that the")
3. "chose a bon escient et la [?] … ce que luy coustera(?)" ("matter in earnest, and the … what it will cost him")
4. "une grandissime(?) raison(?) de ne [?] moins s'il ne luy coste(?)" ("a very great reason … not less if it does not cost him")
5. "que la [?] de [?] allé a ce voyage que [?] pour [?] fut" ("that the … of … gone on this journey which … for … was")
6. "gaigner une grande [?] Quant a noz [?] deffendu &c." ("to gain a great … As for our … forbidden, etc.")

Closing words to look for in cipher: "… Quant a noz … deffendu".

## A — au Roy, ff. 40r–43v (cipher view 45 L to view 47 R)

Start (v45 L; cipher begins after "…donner mauvaise reputation a ses subjectz"):
- l.0 tail: `‡ oo? ϱ x ϱ? ∂z ·(Ƶ)` → y [l/d] ? e s a ·
- l.1: `∂z ʒ ε α ϱ π ʒ ε x · ### ∂z ε oo x ⊥ §§ ?` → a i r o s [qui] i r e · s a r d e n t ?
- l.2: `· §§ ʒ ơ̇ ⊥ ∂z ɪɪ ơ̇ ɥ 3 4 …` → · t i o n a g? o m e r …

Decoded: "y.. esa / airos [qui] ire sardent … / tion a gomer …". No coherent French, and nothing like "ilz sont bien estonnez".
End (v47 R, last two lines before the clear "Je supplie tres humblement…"):
- `x 7 ơ̇ ⊥ ∂o H ʒ ⊥ ∂z x ε ∂z q ∂z = · Δ 10 ơ̇ 8 ∂z ϱ ʒ ơ̇ ⊥ ϱ §§ π ϱ x Ψ ε x ϱ` → e c o n d t i n a e r a n a u · l x o [cc/m] a s i o n s t [qui] s e c r e s
- `x ⊥ · H x · ε ơ̇ ⊥ §§ · · ·` → e n · t e · r o n t
Decoded tail: "…[se]cond … ion s t qui secre[t]s … enteront." ("…second … which … secrets … will [pres]ent(?)"). It does not end "deffendu".
**Verdict: no match** at the start or the end. Confidence medium-high.

## B — au Roy, ff. 44r–47r (cipher view 48 R to view 51 R)

Start (v48 R l.1, after the clear "…loisir de fere ceste"):
- l.1: `· · F · Δ ∂z · ay = x ∂o ∂ x` → · · [par] · l a · q?/a? u e d z? e
- l.2: `ʒ ʒ̄ ∂o ʒ · ε ∂z q ∂z ∂o ϱ · H ε 3 …` → i ? · i · r a n a · s · t r e …
Decoded: "[par] la [q]ue d… / … rana… stre …" ("by the … "). It does not read "ilz sont bien estonnez".
End (v51 R, about 52% down):
- penult.: `Ƶ ʒ x = x · ∂z ε ∂z q … · = x · ⊥ ʒ ε ∂z Δ ∂z ∴ ʒ · H ⊥ ʒ ·` (not decoded in full)
- last: `H x §§ oo x · ϱ ↑ · ⊥ ϱ x · ε = ʒ · 6 x §§ · · qe? ∂o · ϱ` → t e t d e · s ? · n s e · r u i c e t · · [que?] d · s
Decoded tail: "… [?] n service t… [que] d.s" ("… service …"). It does not end "deffendu".
**Verdict: no match** at the start or the end. Confidence medium-high.

## M — au Roy "sur la mort du Roy de Portugal", ff. 51r–56v (cipher view 55 R to view 61 L)

Start (v55 R mid-page, after the clear "…nous n'en ayons la nouvelle certaine"):
- l.1: `A Δ · ∂ ϱ α · ⊥ §§ · # 6 q` → **i l · z s o · n t** · ? ? ?
- l.2: `‡ ⊟b ʒ δb x ⊥ x ϱ δb H ơ̇ · · ⊥ x ∂ · oo x ⊥ · H x ⊥ oo ε ϱ? x …` → ? b i · e n e s · t o · · n e z · d e n · t e n d r [?] e …
Decoded: "**Ilz sont [? Sire?] bien estonez d'entendre …**" ("They are [Sire?] much astonished to hear …").
That is 27 consecutive plaintext letters (ilzsont … bienestonezdentendre) that agree with the key values, nulls aside.
There is one spelling difference: the cipher has a single n in "estonez", the sheet "estonnez". Doubtful: `‡`
and the boxed sign before "bien" (`?` above, perhaps "Sire" or a b); the `ϱ?` before the final e of "entendre"
(null or mis-read); `# 6 q` at the end of l.1.
The cipher also settles the sheet's first word: it reads "Ilz **sont**", not "seroient".
**Verdict: match start.** Confidence high.
End (view 61 L, 8 lines): **not checked**. The budget ran out.

## R — a la Reyne, ff. 59r–61v (cipher view 65 L to view 66 R)
**Not checked** (budget). Since M matches the opening, the decipherment cannot also begin R's cipher. R could own
the sheet only if it were a composite, which the continuous hand of 48v–49r argues against.

## Result
The sheet at ff. 48r–50v is the decipherment of **M** (the "sur la mort du Roy de Portugal" letter, ff. 51r–56v),
not of B. That leaves **A, B and R without a decipherment** in views 1–215. Open check: M's last cipher lines
(v61 L) should decode to "…Quant a noz … deffendu".
