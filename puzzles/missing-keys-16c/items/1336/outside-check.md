# No. 1336: outside check of the reading (2026-11-19)

This file checks the names, dates and events in `READING.md` (sections 2 to 4 and "What is new here") and
in the top of `README.md` against outside sources. It checks the setting of the reading. It does not check
the decipherment. Nothing here was read from the cipher. The verdicts are "consistent", "inconsistent" and
"not found".

Sources used. Full texts were fetched with Python urllib and searched locally. Downloads were kept in the
session scratchpad and are not checked in.

- **[Pastor-19]** L. von Pastor, *History of the Popes*, vol. XIX (Gregory XIII), English translation, Internet
  Archive `historyofpopesfr19past`, https://archive.org/details/historyofpopesfr19past. SCHOLARLY.
- **[Sala-II]** A. Sala, *Documenti circa la vita e le gesta di San Carlo Borromeo*, parte II (Milan, 1857–61; IA dates the scan 1857),
  Internet Archive `documenticircal05salagoog`, https://archive.org/details/documenticircal05salagoog. PRIMARY
  (a printed edition of archival documents).
- **[Hinds]** A. B. Hinds, ed., *Calendar of State Papers … Milan 1385–1618* (1912), "Milan: 1575",
  https://www.british-history.ac.uk/cal-state-papers/milan/1385-1618/pp594-595. SCHOLARLY (a calendar of
  Ambrosiana letters).
- **[Sylvain]** Chanoine Sylvain, *Histoire de saint Charles Borromée* (preface dated 1882), parts on diocese.mc:
  https://diocese.mc/storage/documents/itkEtlnXBKxdonNebnvuo7qwXVC85LXOzsxnmMFb.pdf (ch. 20 onward, including
  ch. 24) and https://diocese.mc/storage/documents/qi1hxY5ETrslCGK6B3rIE0iatmUVdSnS6Hdh6bYi.pdf (ch. 38 onward).
  SECONDARY. It is a 19th-century hagiography that quotes the letters. Its facts are used only where Pastor
  or Sala agree with it.

## The correspondents and their roles, 1573–75

| Claim (where) | Verdict | Evidence |
|---|---|---|
| Cesare Speciano was Borromeo's correspondent in Rome, 1573–75 (README) | **consistent** | [Pastor-19] p. 68: "Borromeo, however, by means of Bernardino Carniglia and Cesare Speciani, with whom he remained in constant correspondence, was still able from Milan to give expression in Rome to his wishes". [Sala-II] doc. XII (pp. 49–50; the OCR has "1373" in the heading and "1575" at the foot, but the index places it between 20 June and 17 July 1573) is headed "Lettera di S. Carlo … a Monsignor Speciano in Roma" ("Letter of St Charles … to Monsignor Speciano in Rome"), 2 July 1573. [Hinds] no. 999: "Cesare Spetiano to Cardinal Carlo Borromeo … Rome, the 18th June, 1575". |
| "Monsignor Carniglia", a Roman prelate the Pope confides in (c. 269r, c. 44r) | **consistent** | Bernardino Carniglia. [Pastor-19] p. 26: "The dreaded Bernardino Carniglia too was not sent off to Milan as many had expected, but was confirmed in his office" (May 1572). The footnote gives his death as 1576, so he was alive at the dates of both slips. [Sala-II] doc. XII, 1573: "Tutto questo spazzo sarà commune a Monsignor Carniglia che haverà di riferire il fatto a N. S." ("All this dispatch will be shared with Monsignor Carniglia, who is to report the matter to Our Lord [the Pope]"). [Sylvain] ch. 23 has Borromeo asking Carniglia to hand his letter to the Pope (1572). |
| "Monsignor Frumento", a deputy chosen by the Pope to study the jurisdiction case (c. 269r); "Frumento" in the bare line (c. 14r, 4 July 1574) | **consistent** | Alessandro Frumento. [Pastor-19] p. 28 counts him among the reform prelates in Gregory XIII's circle ("Carniglia and Frumento, and the Datary, Contarelli"). [Pastor-19] p. 353: in the jurisdiction negotiations with Spain from November 1578 the Pope was represented by "Cardinals Santa Croce, Sforza, Orsini and Maffei, and the prelates, Alessandro Frumento and Pirro Taro". p. 355: he was sent to Madrid as nuncio in January 1579. [Hinds] no. 999 (Speciano, 18 June 1575): "Monsig. Frumento continues to dispatch the affairs of your lordship". So a Frumento working on jurisdiction business in 1574–75 fits the record. A deputation of Frumento in 1574 itself was **not found**. |
| "Gratti che andò in Spagna l'anno passato" ("Gratti, who went to Spain last year"), c. 269r | **consistent, if the name is Grassi** | [Pastor-19] p. 349: "the Pope sent a nuncio extraordinary to Madrid in the person of Annibale Grassi … to bring the troubles at Milan to an end. Grassi … reached Madrid on November 14th, 1573". The translation's readers gave "Gratti" with doubt, and the cipher gives `?rapictt?`. Grassi is the only papal envoy to Spain over the Milan dispute in this window that I found. If he is the man, "l'anno passato" dates c. 269r to 1574. That fits the 1574–75 range in the README and the "Frumento" of 4 July 1574. Pastor does not name Grassi among the 1574 deputies. |
| Borromeo was the writer and Speciano the recipient of c. 44r, 2 March 1575 (README, from the OPAC) | not checked outside the OPAC | The OPAC record is the only source. Nothing found contradicts it. |

## The 1573 jurisdiction dispute and the papal handling of it

| Claim | Verdict | Evidence |
|---|---|---|
| A jurisdiction dispute at Milan in 1573 between Borromeo and the governor Requesens | **consistent** | [Pastor-19] p. 348: "In the autumn of 1573 there arose a similar dispute at Milan, where Charles Borromeo … had to offer strong resistance to the interference of the governor, Luis Requesens, with ecclesiastical jurisdiction. Requesens retaliated for the excommunication inflicted on him by acts of violence". p. 95 gives the details: Arona, troops round the palace, opened letters, and a public excommunication. [Sala-II] index: "1573, 10 agosto … Monitorio di scomunica" ("monition of excommunication") served on Requesens, the Grand Chancellor and the President of the Senate. |
| Origin: the Resta case against the nuns of S. Michele, Gallarate | **consistent** (context only, not in the reading) | [Sala-II] doc. XII (2 July 1573) and the protests of 20 June and 17 July 1573. [Sylvain] ch. 24 tells the same story. |
| Papal handling: a congregation of cardinals | **consistent** with "avocare lei propria la causa della giurisdittione" (to take the jurisdiction case to himself) | [Pastor-19] p. 349: Gregory XIII "spoke of the occurrence at the consistory of September 7th, 1573, and entrusted the consideration of it to the congregation which had been established to deal with the question of ecclesiastical jurisdiction … Cardinals Santa Croce, Maffei and Albani, to which Cardinals Bobba, Orsini and Giustiniani were now added". Philip II's envoys Navas and Vera arrived in Rome on 6 October 1574 to treat the Naples and Milan disputes (p. 349–350). A papal resolve to take the case to himself in secret, with Frumento and Gratti/Grassi, was **not found** as such. It fits the 1574 phase. |
| Requesens absolved under a papal brief before leaving for Flanders; Ayamonte succeeds | **consistent** | [Sylvain] ch. 24: "le saint père lui fit adresser la permission de se faire absoudre par qui il voudrait" ("the Holy Father sent him leave to be absolved by whomever he wished"), and Borromeo announced the absolution on 26 October. [Sala-II] index: 2 September and 5 October 1573, mass said before Requesens "atteso il Breve Pontificio di assoluzione" ("on the strength of the papal brief of absolution"). [Pastor-19] p. 349: "the overbearing Marchese Ayamonte, who had succeeded Requesens". Ayamonte governed 1573–1580 (SECONDARY, Wikipedia list of governors of Milan, seen in search results only: https://en.wikipedia.org/wiki/Governor_of_Milan). |

## The c. 652r memorandum (1573)

| Element | Verdict | Evidence |
|---|---|---|
| "Le cause di sospicione" (the grounds of suspicion) against a judge, in a case touching "la mia chiesa" (my church), where "Principe" (a Prince) is concerned | **consistent with the setting**. The case itself was **not identified** | "Sospicione" is the term of art for recusing a judge or tribunal. In [Sala-II] doc. XII (2 July 1573) Borromeo expects the Captain of Justice to "allegare per sospetto questo Tribunale … onde bisognerebbe venire a elettione de arbitri che conoscessero di questa sospicione" ("allege this tribunal as suspect … so that arbiters would have to be chosen to judge this suspicion"). He asks Rome for cover against "oppositione di sospicione" ("an objection of suspicion"). The same letter speaks of "questa mia Chiesa" ("this my Church"). A memorandum of 1573 that sets out why a judge is suspect in a case where the King's interest is engaged fits the year of the Requesens dispute and the congregation of cardinals. I found nothing that names the judge, the vote, or the case. |
| "Litta" (`giuol … litta`: perhaps "[fi]gliuol[o] … Litta", son of Litta) | **not found** | No Litta case of 1573 was found in [Sala-II], [Pastor-19], [Sylvain] or a web search. [Sylvain] names the Litta only as a leading Milanese family ("les Litta, les Bescapé") and a "marquis Litta" who gave alms in the plague of 1576–77. The Littas in [Sala-II] are the 17th-century Cardinal Archbishop Alfonso Litta, who is irrelevant here. |
| "parlamento", "pontificato", "fu fatto sapere", "inordinat…" | not checkable | These are word-level interpretations. No outside source bears on them. |
| Author indexed as Carlo Borromeo (OPAC, per `more-letters.md`) | **consistent** with "mia chiesa" and "a N. S.re" (to Our Lord [the Pope]) | Borromeo, writing as archbishop, calls Milan "mia Chiesa" throughout [Sala-II] doc. XII. |

## Names and dates in sections 2 and 3

- "Sua Santità" in 1573–75 is Gregory XIII, elected May 1572 ([Pastor-19], passim). **Consistent.**
- The jurisdiction case of c. 269r, with its deputies and the Pope's secrecy, fits 1574, after Grassi's mission
  (Nov 1573) and around the Spanish envoys (Oct 1574). See above. **Consistent, inferred.**
- c. 44r: "il castellano di Milano et il presidente del Senato" (the castellan of Milan and the president of
  the Senate). The two officers existed. [Sala-II] has the President of the Senate among those served with the
  1573 monition. The holders in March 1575 are **not found**.
- c. 14r: "Frumento", 4 July 1574. **Consistent** with Frumento handling Borromeo's business in Rome in 1574–75
  ([Hinds] 1575; [Pastor-19]).

## Are the Ambrosiana letters catalogued or printed?

- **Not found in print.** [Sala-II] prints the 1573 dispute documents (pp. 23–69 of part II, as [Pastor-19]
  p. 95 n. 2 cites them). None of them has the c. 652r wording: a full-text search for "propalatione",
  "cause di sospicione" and "voto che" gives no hit. [Pastor-19] p. 95 n. 2 cites Borromeo's 1573 reports
  "sent to Rome to Speciani, Castelli, and Galli" in Sala, *Documenti* **III**, 448–536. That volume is not
  among the Internet Archive scans found (`documenticircal00`–`04` are copies of a different part). It is the
  most likely place for any of these letters, or their decipherments, to be printed. **Unchecked.**
- [Hinds] calendars Ambrosiana letters from F 90–92 inf. that touch England only. It does not cover F 46, F 47,
  F 49 or F 131 inf.
- Rivolta. A search found only A. Rivolta, *Catalogo dei codici pinelliani dell'Ambrosiana* (1933). No Rivolta
  catalogue of Carlo Borromeo's letters was found online. The gate's instruction to "check the attribution in
  Rivolta" stays open.
- An inventory of Borromeo's papers: A. Turchini, *Monumenta borromaica I* (2006), seen in search results only
  (SCHOLARLY, not consulted). The Ambrosiana OPAC (PRIMARY) remains the only catalogue consulted, through
  the records the item already cites.

## Unverified claims
- That Frumento and Grassi (or "Gratti") were deputed by Gregory XIII to study the Milan jurisdiction case in
  secret. The two men and their roles are attested, but the deputation is not.
- That "Gratti" is Annibale Grassi. This is an identification by role and date only.
- The identity of the third deputy, the one who "troubles" the writer. The 11 unread signs after "monsignor"
  on c. 269r are not addressed by any source.
- Any Litta case of 1573, and the judge whose vote was disclosed (c. 652r).
- The holders of the offices of castellan of Milan and president of the Senate in March 1575 (c. 44r).
- Whether Sala, *Documenti* III, Turchini's *Monumenta borromaica*, or the Ambrosiana's own Borromeo
  correspondence inventory prints or calendars F 46 inf. n. 275, F 47 inf. n. 131, F 49 inf. n. 18 or
  F 131 inf. n. 7.
- [Sylvain] gives Requesens's envoy to Rome dying on 3 October and Borromeo's absolution letter as
  26 October 1573. This rests on Sylvain alone.
