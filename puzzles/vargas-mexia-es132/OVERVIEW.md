# The Vargas Mexía cipher letters (BnF Espagnol 132): what they say

*Overview of the deep dive as of 2026-10-04. Source of the published Artifact. Everything here is provisional until a
human paleographer has checked the transcriptions (see "Method and limits").*

## In one paragraph
BnF Espagnol 132 is the file that Juan de Vargas Mexía, Philip II's ambassador in Paris, kept of the letters he
received from the King and from the secretary Antonio Pérez between December 1577 and May 1580. Many are partly or
wholly in cipher. In 1844 the cataloguer wrote that they were "imposible descifrar no teniendo la clave". In 2020
Satoshi Tomokiyo identified the four ciphers and published the keys. In late September 2026 a model-assisted project,
`el-descifrador/cabinet-noir`, posted first readings of 30 of the letters; we learned of it only after this work. Using Tomokiyo's keys,
blind transcriptions, frozen decoders and held-out tests, we read eleven letters independently (ff. 87, 103, 105, 113, 123, 154, 157,
165, 167, 179, 198), seven of them wholly in cipher, and then every letter of the weeks before the Escobedo murder
(ff. 3–35). They show four things. First, Pérez's letter of 15 April 1579, three months
before his arrest, is a defence over the Escobedo lawsuit, says the King refused him leave to retire, and says the
Archbishop of Toledo used the Princess of Éboli to make him stay. Second, after Don John of Austria died (1 October 1578),
the King ordered Vargas to investigate, in secret, Don John's dealings in France: papers and letters, a cipher he
shared with the Duke of Guise, and "los 800 mill ducados". Third, Pérez steered sensitive matter into a "private
letter" channel "because [he] cannot look through all the letters". Fourth, before the murder of Escobedo the King heard
from Vargas of the Guises' dealings with Don John's envoy (24 January 1578), but no letter of those weeks speaks of the
Don John–Guise "confederation" that Pérez later gave as a motive. The base keys hold; four of our extensions passed
held-out tests; the readings themselves rest on Sonnet transcriptions not yet checked by a human.

---

## 1. Historical setting
Tiers per the repository's rule 1: PRIMARY, SCHOLARLY, SECONDARY, CLAIMANT (a party's own account), POPULAR.

- **Philip II and Antonio Pérez.** Pérez became the King's secretary on 17 July 1567 and Secretary of State on
  8 Dec 1567, inheriting his father Gonzalo's place (Martínez Navas, "Proceso inquisitorial de Antonio Pérez",
  [Dialnet](https://dialnet.unirioja.es/descarga/articulo/157767.pdf), SCHOLARLY). He countersigned many of the King's
  letters in es. 132 (Tomokiyo, [Cryptiana](https://cryptiana.web.fc2.com/code/spanish3D.htm), SECONDARY).
- **The Escobedo murder.** Juan de Escobedo, secretary of Don John of Austria, was killed in Madrid on 31 March 1578
  ([Wikipedia](https://en.wikipedia.org/wiki/Juan_de_Escobedo), SECONDARY; Spanish Army museum,
  [ejercito.defensa.gob.es](https://ejercito.defensa.gob.es/museo/en/HECHOS_HISTORICOS/HECHOS_HISTORICOS/03.31_marzo.-_ASESINATO_DE_JUAN_DE_ESCOBEDO.html),
  SECONDARY). Public accusation fell on Pérez at once (Lafuente, *Historia general de España* XIV ch. 22,
  [filosofia.org](https://filosofia.org/his/laf/p302c22.htm), SECONDARY). Escobedo's family, backed by the secretary
  Mateo Vázquez, pressed the King for justice; Pérez's own account says the King had Antonio Pazos, president of the
  Council of Castile, persuade Pedro de Escobedo to drop the suit (Mignet, *Antonio Perez et Philippe II*, 1846,
  pp. 126–128, [archive.org](https://archive.org/details/antonioperezetph00mign), SCHOLARLY, citing Pérez's
  *Relaciones*, CLAIMANT). The family withdrew from the criminal case only in 1589 (Martínez Navas). Sources disagree on
  how long the suit lasted.
- **April 1579.** Mignet dates to April 1579 a complaint by Pérez that the King avoided giving him audience, and his plea
  that the King stop the Escobedo family's prosecution; the King put it down to Easter devotions, and wrote that he
  would not intervene because that would mean admitting his part in the murder, asking Pérez "os aquieteis y sosegueis"
  (Mignet p. 120 n. 2, quoting the Hague manuscript f. 101, SCHOLARLY/PRIMARY). Pérez asked leave to retire and the King refused (Pérez's *Relaciones* via Mignet and Lafuente:
  CLAIMANT through SECONDARY).
- **Don John of Austria** died of fever near Namur on 1 October 1578; Alexander Farnese, Prince of Parma, his nephew and
  the King's, succeeded him as governor of the Netherlands ([Wikipedia](https://en.wikipedia.org/wiki/John_of_Austria),
  SECONDARY).
- **The Princess of Éboli,** Ana de Mendoza, widow of Ruy Gómez, was Pérez's ally; whether they were lovers is
  contested (asserted by Lafuente; rumour in Martínez Navas; "unclear" in
  [es.wikipedia](https://es.wikipedia.org/wiki/Ana_de_Mendoza_y_de_la_Cerda)). Philip wrote on 29 July 1579 that she was
  arrested because she had obstructed the reconciliation of Pérez and Mateo Vázquez (Mignet, SCHOLARLY).
- **Gaspar de Quiroga** was Archbishop of Toledo from 1577, Inquisitor General, and cardinal from 1578
  ([Wikipedia](https://en.wikipedia.org/wiki/Gaspar_de_Quiroga_y_Vela), SECONDARY). Mignet places him in the party of
  Pérez and the Marqués de los Vélez; Éboli appealed to his testimony against Vázquez in 1579 (Mignet, SCHOLARLY). No
  source we could read describes him urging Pérez to stay through Éboli: our f. 198 reading is the only witness.
- **The Marqués de los Vélez,** Pedro Fajardo, councillor of State, Pérez's ally, died in 1579 before the arrests
  (Mignet; Lafuente; [es.wikipedia](https://es.wikipedia.org/wiki/Marqu%C3%A9s_de_los_V%C3%A9lez), SECONDARY).
- **"La vacante de Vargas."** Pérez sought the secretaryship of the late Diego de Vargas (Italian/Mediterranean affairs)
  "con el apoyo del marqués de los Vélez y del arzobispo Quiroga"; it was split
  ([es.wikipedia, Antonio Pérez del Hierro](https://es.wikipedia.org/wiki/Antonio_P%C3%A9rez_del_Hierro), SECONDARY;
  the article dates the vacancy "1568", which conflicts with Quiroga's 1577 appointment; a RAH entry gives Diego de
  Vargas's death as 26 Sept 1576, unverified).
- **Juan de Vargas Mexía** was ambassador in France 1577–1580
  ([list of ambassadors](https://en.wikipedia.org/wiki/List_of_ambassadors_of_Spain_to_France), SECONDARY). His 1577 will
  named Pérez executor; the 1580 revision dropped him (Rubino 2012, [OSU](https://kb.osu.edu/handle/1811/51582),
  SCHOLARLY-student, from printed will clauses). His death date is disputed: 1580 or 1581.
- **Pérez's fall.** Pérez and Éboli were arrested on the night of 28 July 1579 (Lafuente; Wikipedia); Martínez Navas
  dates the order 26 July. Trials followed from 1584; Pérez fled to Aragon in 1590 and to France in 1591.
- **The Netherlands, 1578–79.** The Catholic "Malcontent" nobles, led by the Lalaing brothers, negotiated with Parma;
  the Union of Arras was declared on 6 January 1579 and the Treaty of Arras signed on 17 May 1579
  ([Wikipedia, Union of Arras](https://en.wikipedia.org/wiki/Union_of_Arras), SECONDARY).
- **Don John and Guise.** Pérez later named Vargas Mexía as the man who informed Philip of an understanding between Don
  John and the Duke of Guise; Mignet doubts its date and weight (Mignet, SCHOLARLY, reporting Pérez, CLAIMANT).

## 2. Timeline: the letters read, against the events
| Date | Event or letter | Cipher |
|---|---|---|
| 16 Dec 1577 | First royal letter to Vargas in the volume (f. 3) | Cipher 1 |
| 31 Mar 1578 | **Escobedo murdered** in Madrid | |
| 13 Sep 1578 | **f. 87**, Pérez → Vargas: Don Alonso de Sotomayor; Nazareth; Arcauti | Cipher 4 (short runs) |
| 1 Oct 1578 | **Don John dies**; Parma succeeds | |
| 13 Oct 1578 | **ff. 103 / 113**, King → Vargas (duplicates): Mos de la Mota's pay and pretensions | Cipher 3 (whole letter) |
| 13 Oct 1578 | **f. 105**, Pérez → Vargas: how to handle Mota | Cipher 3 (whole letter) |
| 20 Oct 1578 | **f. 123**, King → Vargas: find out what passed in "the matter" and get papers | Cipher 4 (whole letter) |
| 4 Dec 1578 | **f. 154**, King → Vargas: Arras, Lalaing, Mota, Guise's cipher with Don John, the 800,000 ducats | Cipher 4 (whole letter) |
| 8 Dec 1578 | **f. 157**, Pérez → Vargas: money dealings and a correspondence to cease; papers "con el mayor recato" | Cipher 4 (runs) |
| 6 Jan 1579 | Union of Arras | |
| 10 Jan 1579 | **ff. 165 / 167**, King → Vargas (duplicates): letters, Mota | Cipher 3 (whole letter; read in part) |
| 26 Jan 1579 | **f. 179**, Pérez → Vargas: the private-letter channel | Cipher 4 (runs) |
| Apr 1579 | Pérez asks the King to stop the Escobedo prosecution (Mignet) | |
| 15 Apr 1579 | **f. 198**, Pérez → Vargas: the Escobedo defence, the refused leave, Quiroga and Éboli | Cipher 4 (runs) |
| 16 May 1579 | Vargas's letter from which Devos (1950) reconstructed Cipher 4 | |
| 17 May 1579 | Treaty of Arras | |
| 1579 | Death of the Marqués de los Vélez | |
| 28 Jul 1579 | **Pérez and Éboli arrested** | |
| 1580 | Vargas revises his will, dropping Pérez | |

## 3. The ciphers
**Cipher 4** (Sept 1578 – Apr 1579; Devos 1950 p. 422, reconstructed from Vargas's letter of 16 May 1579; additions by
Tomokiyo). Each consonant is a number from 1 to 23 (a = 12, b = 11 … o = 23); a mark attached to the number adds the vowel
(dot after = -a, + = -e, dot below = -i, a "6" after = -o, dot above = -u). Letters such as B, C, f, g, p, t stand for
clusters (bl, cl, fr, gr, pr, tr). A few short codes stand for words ("vo" = Vuestra Magestad, "co" = carta).
**Cipher 3** (Mar 1578 – May 1580; Devos Cp.30; also used by Bernardino de Mendoza and Juan de Borgia). Numbers 1–37 for
letters and clusters, with vowel marks after (+ -a, dot -e, a curl -i, a hook -o, a T-bar -u) and consonant marks above
(/ -l, \ -m, ^ -n, v -r, bar -s). A cross above marks a code word.
**Who found the keys.** Devos printed Ciphers 1, 3 and 4 in 1950 without linking them to this volume; Tomokiyo identified
all four in es. 132 in August 2020, cracked Cipher 2 himself, and read a few words of f. 198
([Cryptiana](https://cryptiana.web.fc2.com/code/spanish3D.htm), SECONDARY).

**Our additions, and the evidence for each.** "Held-out" means a letter transcribed after the value was frozen by commit.
| Addition | Cipher | Evidence | Status |
|---|---|---|---|
| 2H = que | 4 | f. 198 in-sample; held-out 83/84 (ff. 87, 154, 157, 179) | established |
| Σ = o | 4 | held-out 37/38 | established |
| A cross above doubles the letter (Devos's rule, reported but unapplied) | 4 | f. 123 7/7 in-sample; held-out 36/36 (aquella, assí, Arras, desengañasse, mill…) | established |
| H = ne | 4 | held-out 14/16 (2 unclear) | passes |
| 21. = que | 4 | f. 198 19/19, but outside it 1 fit, 1 misfit ("qual"), 1 unclear | weakened: local to f. 198 |
| 21_ = qui | 4 | f. 198 7/7 (incl. "Quiroga"); held-out 1/2 | untested |
| "ra" = oficio | 4 | f. 198 4 contexts; the phrase also spelt out once | candidate, in-sample only |
| Tokenization: the -i curl is a joined "6", the -o hook looks like "p", the -u T-bar like "u" | 3 | Tomokiyo's aligned ff. 81/83; calibration reader 68% syllables exact; ff. 103, 105, 113, 165 read as Spanish | supported |
| "u." = que | 3 | frozen from Tomokiyo's f. 81 labels; fits every occurrence on ff. 103, 105, 113 | supported |
| 108⁺ = Su Magestad, 149⁺ = V.m. | 3 | f. 105, frozen on one reader, replicated by the second (6×, 2×) | supported in-letter; no held-out letter exists in es. 132 |
| T⁺ = particulares | 3 | duplicate f. 103 (code) vs f. 113 (spelt out), 3×; f. 105 2×; held-out duplicates ff. 165/167 2/2 | consistent; n < 3 at held-out |
| 35 = pr or pl | 3 | pr in most contexts (primero, propio, principal, pretensiones); pl only in "plaça" | resolved by cabinet-noir: 35 = pr, underlined 35 = pl |

## 4. What each letter says
English translations of our readings. **Deciphered text is in bold**; plain text was written in clear. [word?] is a
suggestion for a span we could not decode; [ … ] is a gap. Spanish readings with line numbers:
`analysis/05-cipher4-v2/readings-v2.md`, `analysis/04-cipher3/*_v2.txt`.

### f. 87, Pérez to Vargas, Madrid, 13 Sept 1578 (mostly clear)
Pérez answers three letters, regrets the miscarriage of Vargas's daughter-in-law, and reports on his own family. "You did
me great kindness in advising me of all that touches **Don Alonso de Sotomayor**; I have dealt with him as you thought
best." On Nazareth (the papal nuncio in Paris) there is a short run we cannot read. Later: "I have shown the King all that
you have written to me **about how [he] does not want [ … ] but a post [ … ], and what** does him harm, **seen in those
parts** [ … ], and the little consideration and show of ill will in **honouring Arcauti** [ … ], **[procurar?] to discredit**
[ … ]." The King is satisfied with Vargas's service; Pérez will speak to Garnica about Vargas's pay from Milan.
*Check:* the name Don Alonso de Sotomayor, in cipher here, is in clear on f. 88r.

### ff. 103 and 113, Philip II to Vargas, Madrid, 13 Oct 1578 (all cipher; two independent encipherments)
**"Juan de Vargas Mexía. You know how Mos de la Mota serves me in the place of Gravelines. He has written to me many times
that he should be paid [ … ] and about his particular pretensions. My brother wrote that I should assign him 300 escudos a
month, and grant him an encomienda. I had my brother told that I was content that he be given the said 300 escudos a month,
and that in the rest account would be taken of him; I do not remember that an encomienda in these kingdoms was offered him.
Mos de la Mota has now written to me again, asking with insistence, for the great need he suffers, that I settle his
particular affairs. Since he wrote to me in French, answering others of his and referring me in his particular affairs to
my brother or to the Prince of Parma, I have thought fit to write him another in Spanish, of the tenor you will see by the
copy, which you will send him by way of Alonso de Curiel together with the one in French. You will write to him what I wrote
to my brother: that I was content that he be given the 300 escudos a month, that he may be certain they will be added, and
that they will continue to be paid until he is granted an equivalent encomienda; and, besides this, that since there is no
occasion now to grant him the favour I wish, [ … ] help with costs [ … ]."**
*Checks:* the volume contains the companion letters of the same day: to M. de la Mota in French and in Spanish (ff. 107,
111) and to Alonso de Curiel (f. 109). The duplicate f. 113 spells out "particulares" where f. 103 uses a code.

### f. 105, Antonio Pérez to Vargas, Madrid, 13 Oct 1578 (all cipher; two readers reconciled)
**"Your Worship will see from His Majesty's letter what he writes to you about Mos de la Mota's particular affairs. His
Majesty has ordered me to advise you whether it would be good, before giving him what the letter contains, to find out
first what his pretensions are, since he might not be content with being told that the 300 [escudos] a month will be
continued until His Majesty grants him an equivalent favour in some encomienda; and that it would be well to tell him about
the 300 escudos, and besides that, that His Majesty will keep in mind his person and services to grant him favour when an
occasion offers; and that with this and the help with costs he should be satisfied for now. In short, His Majesty [asks]
that you see how best to write to Mos de la Mota what touches his particular affairs, taking from the letter [what you
judge fit] and leaving [the rest], as is most convenient, since it matters to keep him content and satisfied; [this] is
left to Your Worship's discretion, to see to it as you think best for [His Majesty's] service, [ … ] so that he remains satisfied, or at least not slighted."** Signed Antonio Pérez.
*Note:* we earlier followed Tomokiyo's table of contents in calling this a royal letter; the text shows Pérez writing.

### f. 123, Philip II to Vargas, Madrid, 20 Oct 1578 (all cipher)
**"Your letters of [ … ] of last month, [about] that matter, have been received, and I thank you for the good intelligence you
have shown in what you say there, and for the care to advise me of it, and of the rest you understand to be of my [service].
And although with this last event those [ … ] have ceased, it will still be well that you try to find out, skilfully, what
passed in the business, and how far it went, and the persons who took part in it, and the [stakes?] each one had put in it;
and even, if you could get hold of some papers or letters of the Theatine, or of other persons, it would be convenient."**
Signed by the King, countersigned Antonio Pérez. "This last event", nineteen days after 1 October, is Don John's death.

### f. 154, Philip II to Vargas, El Pardo, 4 Dec 1578 (all cipher; one reader; held-out)
Read in outline (2,060 signs). **The King thanks Vargas for "the care and diligence you use in trying to learn what is
understood of the [affairs] of my [brother]s [ … ] as of those of that kingdom". The account of what happened at Arras and
Douai was welcome. "The present confusion in those [States] is very much to the purpose for bringing them back to my
[obedience]": he has ordered "the Prince my nephew" to do all good offices, and sent him the needed letters and [signature]s.
Vargas is to work for the same from Paris, "and particularly in the matter of the Count of Lalaing … for it could be that,
finding himself weary, he would be undeceived and glad to return to his obligation". The King approves what Vargas sent
to say to Mos de la Mota through an Italian captain, about bringing back Lalaing, Egmont and the rest of the Catholic
nobility, and about seizing [the Duke] of Alençon. Andrés de Ayala, sent by Mota, has arrived; Mota proposed "some good
blow of an army" on that side, but the King "did not want to resolve on it, only to answer him with good words, referring
him to the Prince of Parma my nephew". Then the core passage: Vargas reported what Guise wrote to him, and what the
ambassador of Scotland told him on Guise's behalf "about the cipher he had with my brother", and of "the union there was
between them, and the [Duke] of Lorraine, and the 800,000 ducats they had together". Vargas is to find out "the foundation
of the matter of the 800,000 ducats, and where and how they hold them, and whether my brother had received any part of
them; but this must be done with great tact and secrecy, and without any person being able to understand that you do this
by my order." Also: the warning that Alençon had intelligences in Philippeville was rightly passed at once to the Prince
my nephew; couriers from the Prince passing through Paris; "the good correspondence he must keep with you".**

### f. 157, Pérez to Vargas, Madrid, 8 Dec 1578 (clear with cipher runs)
"The matter **of removing the [ … ] of the arms** has been considered and is wished for, but cannot be done all at once…
On the matter of [ … ] there is nothing to say except that everything will take a better course with the new order given
that **[ … ] Arcauti [ … ]** only… This is now being written **to the Prince of Parma**, and with the ending of **the handling
of money** among those there, **all the [ … ] will cease**. Also **the new correspondence that had been begun [with?] Arcauti,
and the chief courier,** will cease now…" In an interlinear passage: "**to Arcauti and the others the [ … ] will be sent**, and
believe me they are not left between the lines: **the twelve thousand [ … ]**". "The copy of the letter **of the Prince of
Parma** was seen." "His Majesty saw the letter you wrote him on 2 November **about the [ … ]**, and says that you should still
try **to look into everything possible, and if it were [possible] to get hold of some papers, but that this be with the
greatest secrecy possible**." "Very good was your warning in the matter of **Mos de la Mota, that he should be [rewarded?]
with** an encomienda or something similar rather than **with pure money**, for every reason." The rest is clear: Vargas's
pay from Milan, 400 [escudos] a month, credit through Garnica.

### ff. 165 and 167, Philip II to Vargas, San Lorenzo, 10 Jan 1579 (duplicates; all cipher; one reader each; read in part)
**"After [the arrival] of Don Alonso de Sotomayor, all your letters [ … ] have been received … the letter I have received
from Mos de la Mota … what he has sent to Pedro [ … ] … the towns and particular persons … by a courier of his own, with
diligence …"** A first decode: readable in stretches, with many reader errors; not yet reconciled. Where f. 165 spells "personas particulares" and "particular", f. 167 uses cross-marked codes, which tests the code for "particulares".

### f. 179, Pérez to Vargas, Madrid, 26 Jan 1579 (clear with cipher runs)
"As to what you say, that in specie or in genere **[ … ]** something of what **[ … ] has written about** [ … ]: [I say] that although
he was given to understand **in general that there was some knowledge** of what has passed (because it was so fitting),
**[it was] with such secrecy that not even in imagination** could he understand **that there had been [ … ]**. And with this you
may be certain that there is every care with papers. Keeping on guard, **what I have to say [ … ] should come only in the
private [letter]**, because **[he?]** has much business and **cannot** look through all **the letters**, and in this way there
will be no danger." Later: "I am warned about **[ … ]** by what you **tell** me of him… and I **will guard myself against him**,
as you advise." "The affair of **García de Arze** [ … ] is very different **from what [ … ] suspected**…" The rest is clear:
Don Lorenzo de Vargas and Vargas's own affairs.

### f. 198, Pérez to Vargas, Madrid, 15 April 1579 (clear with cipher runs; two readers reconciled)
"Since I do not doubt that the outcry and lies that have run here these days about my affairs will have reached you, I will
tell you briefly the truth of what is happening, for your satisfaction. **Know that some days ago His Majesty was pleased,
intending to give me the [office] of Vargas** — and he himself gave me to understand it — **and by order that the Marqués de
los Vélez, Quiroga and [ … ]** should meet and see what order could be given in **the matter of the Chancery of [ … ]. It was
done, and they sent him the consultation**; and from the consultants themselves it was understood, **and it was said for
certain here and everywhere, that the [office] was being given to me, [but] His Majesty [held back]** from declaring it then,
on the occasion **of a certain paper that he said he had come upon, which** he said could help **the good settlement of the
business: about a lawsuit that Escovedo brought against me; and although** in the end **my innocence** was seen, **and the
other party was undeceived about its claim, seeing the weak** foundations it had, **with which the business ended, still the
false testimony they raised against me, and the time spent** in finding out the truth, did me harm. For meanwhile **His
Majesty changed his mind about the office of Vargas, and wants to dismember it and divide it** in a certain way, and he has
come to say that they will join **all that of the [ … ] and give it to me, and that I should go with him** wherever he went,
and that this should be **for the [office] of Vargas. I have felt** [ … ] **this blow**, being as public as it was **in all the
world, and the dishonour and loss of reputation** that follows for me, **at a time when I have suffered so much without
fault**, and when it would have been right **to honour and advance me in repair of my honour and as witness of my innocence**.
And joining to this the knowing of **the age**, and being by nature a philosopher, as you know, I have wished earnestly to
withdraw and live a quiet, Christian life; **and I have begged His Majesty to allow it, since it was not just** to live in one
place and town, **I and my [children], with those who** with such envy, rage and falsehood **have tried to take away my honour
and my life**. From having [ … ] **the wish [to retire] and the Escovedo lawsuit having preceded it, the devil** and his
ministers **have invented and spread the lies of exile** and the rest you will have heard. But **the truth is that His Majesty
has not wanted to give me leave; rather he wishes that I calm myself and stay still**. And through **the Archbishop of Toledo
he has had the Princess of Éboli told to persuade me** to calm myself, remain, and **[continue] in his service**, under great
oaths **that the Archbishop made that His Majesty** would greatly regret **my leaving here; and that if I, wishing** to continue
in service, **put myself in His Majesty's hands, he would grant me [favour] and favours and honours, giving me his [ … ]. And
this is being negotiated and taken up now.** I do not know where the business will end, but I will advise you of whatever
happens. Doña Juana and our children are well…" Postscript by Hernando de Escobar.

## 5. What is new, and what is not
| Before | Now |
|---|---|
| Ochoa (1844): the cipher letters "imposible descifrar no teniendo la clave" | Read, with published keys |
| Rubino (2012), a Parker student, transcribed the clear text of eight Pérez letters and marked every cipher passage [CIFRA]; one word decoded | Her gaps on ff. 157, 179, 198 filled; her clear text agrees with ours at the joins |
| Tomokiyo (2020): keys for all four ciphers; words of f. 198 | – |
| **cabinet-noir (GitHub, 29 Sep – 1 Oct 2026):** model-produced first readings of 30 letters (incl. ff. 11, 17–25, 32, 105, 113, 123, 154, 165, 198), each checked by an independent agent, no paleographer; Cp.30 nomenclature from Alcocer (1921) | **Our readings are independent replications.** Our f. 198 matches theirs nearly word for word |
| pangoleen/cipher-readings (4 Oct 2026): ff. 26r, 87, 157, 179, 273 | Compared by script: our f. 26r and Cipher 4 runs of ff. 87, 157, 179 agree at medians of 91–95% (controls 41–58%) |
| Mignet (1846) printed two passages of the 8 Mar 1578 letter; we found no work that sets the pre-murder letters against Pérez's "confederation" | Experiment 06: every window letter read blind (incl. f. 3, Cipher 1, not among the third-party readings); the 24 Jan 1578 Sotomayor–Guise report (f. 12v) predates the murder and Mignet's May 1578 date for Sotomayor's mission |

**What this dive adds** beyond those readings: two blind readers per Cipher 4 letter reconciled against the images; held-out
tests of the Cipher 4 extensions (2H, Σ, H, and Devos's cross-doubling rule, 36/36); a scored Cipher 3 transcription guide;
the Rubino joins; and the synthesis in section 7 (the King's April 1579 note against f. 198; the Guise chronology).
**Established**: the keys read these letters; 2H, Σ, cross-doubling and H; the general content of ff. 103/113, 123, 154 and
198, now read by two independent projects.
**Provisional**: every exact wording; all bracketed suggestions; f. 154, 165 and 167 on one reader each; our code values
(108, 149, T⁺) until checked against Alcocer's printed nomenclature; "Arcauti"; "teatino".

## 6. What it is about
- **The Escobedo defence (f. 198; H3).** Pérez's cipher account blames the loss of "the office of Vargas" on "a lawsuit that
  Escovedo brought against me" and "the false testimony". Mignet independently dates to April 1579 Pérez's plea that the King
  stop the Escobedo prosecution. Rubino asked whether this "tell-all" letter made Vargas cut Pérez from his will; the cipher
  reads as a defence, not a confession.
- **The refused leave (f. 198).** "His Majesty has not wanted to give me leave; rather he wishes that I calm myself and stay
  still." Pérez's *Relaciones* make the same claim years later; here it is in a private letter written at the time. Philip's own
  note of the same month asks Pérez to "aquietar" and "sosegar" (see section 7).
- **Éboli and the Archbishop (f. 198; H5).** The Archbishop of Toledo, through the Princess of Éboli, urged Pérez to stay,
  "under great oaths". No historian we could read reports this. Quiroga's alliance with Pérez and Vélez is documented
  (Mignet), and the cipher's "Marqués de los Vélez, Quiroga" fits the Spanish Wikipedia account of who backed Pérez for
  the Vargas office.
- **"The matter" (H6).** After Don John's death the King wanted to know what had passed, who took part, the stakes each had,
  and any papers "of the Theatine or of other persons" (f. 123, 20 Oct). On 4 Dec he names it: Guise's cipher with Don John,
  their "union" with Lorraine, and 800,000 ducats, to be investigated "without any person being able to understand that you
  do this by my order" (f. 154). On 8 Dec Pérez passes on the same order, "with the greatest secrecy", and says the handling
  of money and a correspondence will cease (f. 157). Pérez later claimed it was Vargas who told the King of a Don John–Guise
  understanding (Mignet): f. 154 shows that report arriving.
- **The private-letter channel (f. 179; H7).** Pérez tells Vargas that what he has to say on this should come "only in the
  private [letter]", because someone "has much business and cannot look through all the letters; in this way there will
  be no danger." Who that someone is (the King? another secretary?) is the open point; the word before it is undecoded.

## 7. The letters and the Escobedo murder
The standard short account (Wikipedia's article on Juan de Escobedo, which reprints the 1911 *Encyclopædia Britannica*,
[Wikipedia](https://en.wikipedia.org/wiki/Juan_de_Escobedo), SECONDARY) says the King ordered Pérez to have Escobedo
"put out of the way", that two attempts at poison failed, and that bravos killed him on Easter Monday 1578. The letters
read here say nothing about the order, the poison or the killers, or about Pérez and Éboli as lovers. They add three
things, each tied to a dated letter.

### 1. Pérez's own account, a year later
In the cipher of f. 198 (15 April 1579), writing to an ally, Pérez calls it
"la demanda que Escovedo me puso": the family's lawsuit, since Juan was dead. He says the suit ended, "con que se acabó el
negocio", with "mi inocencia" seen and the other side's claim resting on "los flacos fundamentos", and he blames "el falso
testimonio que le levantaron". He does not mention the King's part. This is a party's account (CLAIMANT), and his silence
proves little: on f. 179 he routes sensitive matter into a separate private letter because other people read the
ordinary ones.

### 2. The King's side, the same month
Mignet prints a note from Philip to Pérez of April 1579 (from the Hague
manuscript, f. 101), refusing to order the Escobedo prosecution stopped, because that would have meant admitting his own
part in the murder: "mientras se pueda escusar que lo que se ha hecho de la muerte de Escobedo no a sido con interbencion
mia, bien sera que se escuse … y assi os ruego mucho que os aquieteis y sosegueis" (Mignet 1846, p. 120 n. 2,
[archive.org](https://archive.org/details/antonioperezetph00mign), SCHOLARLY quoting a PRIMARY note). Our cipher of
f. 198, decoded without reference to Mignet, reports the same wish in Pérez's words: **"la verdad es que V.Magd no me ha
querido dar licencia; antes dessea que yo me sossiegue y esté quedo"**, and has the Archbishop of Toledo, through the
Princess of Éboli, press Pérez to stay "debaxo de grandes juramentos". So two texts written independently in April
1579 agree on the King's stance and on his words, "sosegar" and "aquietar". What the letters add is Pérez's side of
that exchange as he told it to a friend: he presents the King's refusal of leave as a sign of favour, not as a
King who needed him quiet and close. Three months later the King had him arrested. One tension stays open: Pérez tells
Vargas the suit is over, while Mignet's note has him asking the King, that same month, to stop it.

### 3. The "confederation" with the Guises
Among the reasons that, in his later account, decided the King on Escobedo's death, Pérez named a secret confederation
between Don John and the Guises "sous le titre de défense des deux couronnes", which, he said, Vargas Mexía had denounced
around spring 1577 (Pérez's claim reported by Mignet, pp. 68–69, CLAIMANT via SCHOLARLY). Mignet rejected it: Vargas
reached Paris only on 10 December 1577, and his reports on the two princes are "presque toutes postérieures au meurtre
d'Escovedo" (pp. 71–73). We read every letter of es. 132 from the window 16 December 1577 – 17 March 1578: the cipher
letters ff. 3, 11–12, 17–25, 26r, 32 and 34, two blind readers each, and the clear letters on the image (experiment 06).
We also checked Teulet's printed decipherments of Vargas's own dispatches on the page. The record is more precise than
either Pérez or Mignet:
- *Before the murder, the King knew of direct dealings between the Guises and Don John's envoy, and took them
  seriously.* The King's letter of 24 January 1578 (f. 12v, Cipher 2, two blind readers, and the same words in
  cabinet-noir's reading) answers Vargas: **"Assimismo he visto todo lo que me escriuís sobre la llegada ay de don Alonso
  de Sotomayor y de su commissión, y de todo lo [que] los Guysas trataron con él cerca del proceder de mi hermano y con
  Alanson, y haveis hecho muy bien en avisarme tan particularmente de todo, porque cierto son cosas que tienen mucha
  consideración."** Sotomayor was Don John's envoy. The Simancas finding aid lists, among the 1577 papers, a "Conferencia
  entre D. Alonso de Sotomayor y los Guisas sobre el resentimiento que en la Corte de Francia tenían con D. Juan de
  Austria por su manera de escribirles" (Paz, *Catálogo IV*, 1914, p. 382, K 1543). Mignet dates Sotomayor's mission
  to the Guises to May 1578, after the murder (p. 436). That was the second mission (K 1544, April–June 1578). The first
  was in Paris by January.
- *But no letter of the window speaks of a league, a confederation or a union between Don John and the Guises.* What
  the letters show is Guise loyalty and friction. On 28 January Vargas visits Guise with the King's letters (Teulet
  pp. 134–136). On 16 February Vargas passes on the Venetian ambassador's report that the Scottish ambassador, through
  the Guises, wanted Don John to marry Mary Stuart and take England "con la assistencia que le diesen los de Guisa", and
  calls it "grandes quimeras" (Teulet p. 137, B. 45 n° 30). The King's answer of 8 March (ff. 17–20 and duplicate ff. 22–25,
  Cipher 2; four blind readers; the decode contains both passages that Mignet printed from the Simancas minute) calls the
  marriage talk "de poco fundamento". It tells Vargas to keep Guise and his house "en mi devoción … con la dissimulación y
  cordura", forbids sending money out of France to Don John "sin que primero preceda licencia" of the French King, and
  reports a "liga" being arranged by the Duke of Brunswick. On 17 March (f. 32, Cipher 3) the King asks about a league
  through the Duke of Lorraine "con algunos príncipes del Imperio" against help for the Huguenots, and has Vargas visit
  the Cardinal and Duke of Guise "para los confirmar" in their goodwill. Don John has no part in either league.
- *The "union of the two crowns" is later and about something else.* "La union destas dos coronas … podrian dar ley al
  mundo" is Vargas's report of 13 April 1578 (Teulet p. 145, B. 44 n. 57), two weeks after the murder: Guise wanted Spain
  and France allied. Don John is not named.
- *Eight months later the King still did not know.* f. 154 (4 Dec 1578) asks for **"el fundamento que tiene lo de los 800
  mill ducados … y si mi hermano avía recibido alguna parte dellos"**, after reports of **"la cifra que tenía con mi
  hermano"** and **"la unión que avía"** with Guise and Lorraine.
So Pérez's story has a true core with the wrong label. Before the murder the King did hear, from Vargas, of Guise
dealings with Don John's envoy, and he called them "cosas que tienen mucha consideración". In the finding aid's summary
those dealings were French complaints about Don John's manner, not a pact "de défense des deux couronnes". The union of
crowns, a Guise idea for Spain and France, came after the murder. Mignet's verdict ("presque toutes postérieures") holds for
the confederation as Pérez framed it, but not for every Don John–Guise report: the January Sotomayor report is earlier,
and Mignet does not mention it. Pérez countersigned the 24 January letter himself, so he knew of it.

*Limits.* The window letters rest on Sonnet transcriptions (two readers each, no human paleographer). ff. 26v–31r (the rest of a
March letter and its duplicate) are not in the Gallica scan. Vargas's own dispatches are known only through Teulet's
Scotland-centred excerpts and Mignet's quotations. Mignet's "grande confidence" between Don John and the Guises (Série B,
liasse 44, n° 89) has no date in print. The Simancas originals were not seen. The letters do not test what Pérez told the
King about Escobedo's designs for Don John.

## 8. Method and limits
- **Transcription.** Every transcription is by Claude Sonnet 5.5 agents working blind: no key, no decodes, no other reader.
  Five Cipher 4 letters have two readers, reconciled sign by sign against the Gallica images by a third agent that also
  never saw a decode. f. 154, f. 165 and f. 167 have one reader. Spot-checks found 0–10% shared errors among tokens both readers
  agreed on.
- **Decoding.** Each decoder was frozen by commit before the transcriptions it read; each new value was frozen before the
  letter that tested it was transcribed. Statistics come from scripts in `analysis/` with checked-in outputs.
- **Calibration.** On Cipher 3, a blind reader matched 68% of Tomokiyo's labelled syllables on f. 83; the two blind readers
  of f. 105 agree on 72% of decoded syllables. These figures bound how exact any single wording can be.
- **What is not done.** No human paleographer has checked any transcription. Word division, accents and every bracketed
  suggestion are an LLM's reading. Before citation: a reader of sixteenth-century Spanish secretary hands should check the
  v2 transcriptions of ff. 198, 123 and 154 sign by sign against the images, and a historian of Pérez should check the
  identifications (Arcauti, the Theatine, the Vargas office, "Quiroga").

## 9. Open questions and next steps
- **Simancas.** Paz's catalogue puts Vargas Mexía's cipher originals "y algunas minutas de respuestas de Felipe II" in
  Archivo General de Simancas, Estado K 1550–51, and his 1579 correspondence with the King and Pérez in K 1554–55
  ([archive.org](https://archive.org/details/catlogo4secret01spai), SECONDARY). A clear draft (minuta) of any letter read here
  would test the reading completely. PARES item-level search needs a human or a browser.
- **Parker.** Whether Geoffrey Parker's *Imprudent King* (Yale 2014) or *Felipe II* (2010) uses these letters is unchecked.
- **Who is Arcauti, the Theatine, and the third name after "Quiroga"?** Who has "mucha occupación" in f. 179?
- **Cipher 3 codes.** 21⁺ (5×) unvalued; T⁺ needs a third held-out occurrence; 7⁺ = personas seen once; 35 = pr, underlined 35 = pl (cabinet-noir, proved in context).
- **The rest of the volume.** cabinet-noir has read 30 letters; we compared the window letters and Pérez's Cipher 4 runs
  (medians 82–95% agreement, `analysis/06-premurder/thirdparty-compare.md`). Our Cipher 3 codes u., T⁺ agree with theirs;
  108⁺ falls in a gap of Alcocer's printed table.
- **Pre-murder letters: done** (experiment 06). Open: Mignet's undated "grande confidence" report (Série B, liasse 44,
  n° 89) and the Sotomayor–Guise conference papers in Simancas K 1543; ff. 26v–31r, missing from the Gallica scan.
