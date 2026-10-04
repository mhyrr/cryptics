# Cipher 4 readings, v2 (2026-10-04)

**Basis.** Reconciled two-reader transcriptions (`sources/transcription/v2/`) for ff. 87, 123, 157, 179, 198;
one blind reader for f. 154 (held-out). Decoder `decode_v2.py` (frozen `8fafd88`). Outputs: `f*_v2.txt`.
Syllable values come from code. Word division, accents, punctuation and the bracketed suggestions are
interpretation (an LLM reading) and are marked as such.

**Conventions.** Plain = clear text in the letter. *Italic* = deciphered. [word?] = a suggested reading of an
undecoded or garbled span (not a decipherment). [ … ] = unresolved; every one is listed under its letter with
its line in the `_v2.txt` output. Spelling is the decoder's, normalised only by joining syllables.

---

## f. 87r–v · Antonio Pérez · Madrid, 13 Sept 1578
Cipher runs (≈ 100 tokens):
- l. 12: Hizo me V.m. mucha merced en avisarme de todo lo que toca a *don Alonso de Sotomayor*. (Name in
  clear on f. 88r: an independent check of the base key.)
- l. 19: En lo de Nazareth [ … ] *pl[ … ]* / *y la lain* [ … ].
- l. 22–23: …creo lo que V.m. cerca desto me escrive de que no [ … ] *a[…]ca do a recoge[…] me* [ … ] como deviera.
- l. 40–44: Al Rey he mostrado todo lo que V.m. me ha escrito *de cómo no quiere [ … ] sino puesto de [ … ]*,
  *y lo que* le haze mal *visto en aquellas partes* [ … ], y la poca consideración y muestra de malavoluntad en
  *honrrar a Arcauti[a]* [ … ], *curaz desacreditar* [ … ].
Unresolved: l. 19 two loop-H signs and "pl"; l. 22 "S." and "c"; l. 40 ⟨mo⟩ and the gutter; l. 41 "QUI sto"
(21_ gives "quisto"; "visto" fits); l. 43–44 the S-with-tick and four-with-loop signs.

## f. 123r · Philip II · Madrid, 20 Oct 1578 (all cipher after the address)
*Vuestras cartas de [ … ] del passado que [ … ] tan de aquella materia se [ … ] se han recebido, y yo os
agradezco [qua] la buena intelligencia que [a]veys tenido en lo que allí dezís, y el cuydado de avisarme dello,
y de lo demás que entendeys que es de mi [servicio?]. Y aunque con este último successo ha[n] cessado aquellas
[ … ], todavía será bien que vos procureys de entender diestramente lo que en el negocio huviere passado, y hasta
dónde se llegó en él, y las personas que en él intervenían, y las [prendas?] que cada uno tenía metidas; y aun
si pudiéssedes aver algunos papeles o cartas del teatino o de otras personas, sería conveniente.*
Unresolved: l. 2 "na uu" before "vuestras" and the dates ("de s y r"); l. 3 the ε-with-dash sign and "se cle ta"
(trata?); l. 4 "qua" (clear or cipher); l. 5 the 7-with-tail sign ("aveys" with it read as a?); l. 7 the Y-like
sign before "u" (servicio?); l. 9 ⟨du⟩ after "aquellas" (pláticas? diligencias?); l. 11 ⟨S^⟩ before "viere"
(huviere); l. 12 the f/p-like sign + "n das" (prendas, if the sign is p = pr); l. 14–15 "del teatino": read
"te a ti no" by v2 (reader B "se a ti no"); a Theatine cleric, unidentified.

## f. 154r–155v · Philip II · El Pardo, 4 Dec 1578 (held-out; one reader; nearly all cipher)
In outline (≈ 2,060 tokens; read continuously, not every span checked):
- Thanks for "el cuydado y diligencia de que usays en procurar de saber lo que se entiende assí de las [cosas] de
  mis [hermano]s … como de las de esse reyno y de otras partes".
- "Fue muy bien embiarme la relación de lo succedido en Arras y Dua[y]". "El aver agora tanta confusión en
  aquellos [Estado]s es muy a propósito para reduzirlos a mi [obediencia]": orders sent to "el Príncipe mi sobrino"
  (Parma) to do good offices, with "cartas y [firma]s".
- Vargas to work "particularmente para lo del Conde de Lalaing … pues podría ser que, viéndose cansado, se
  desengañasse y holgasse de bolver a su obligación". Approval of what Vargas sent to say to Mos de la Mota through
  an Italian captain, "sobre el reduzir al [conde] de Lalaing, [y] Egmont, y a la demás nobleza y [gente] cathólica,
  y que se procurassen apoderar del de Alanson".
- Andrés de Ayala, sent by Mos de la Mota, has arrived with "particular relación". Mota proposed through him
  "que por aquella parte huviesse algún buen golpe de exército" with "muy buenos efectos"; the King "no he querido
  tomar resolución en ello, sino responderle con buenas palabras, remitiéndole al Príncipe de Parma mi sobrino".
- "Lo que Mos de Guisa os escrivió, y de lo demás que el embaxador de Escocia os avía [dicho] de parte del [duque]
  de Guisa sobre lo de la cifra que tenía con mi hermano, y lo que el mismo embaxador discurrió con vos de la unión
  que avía entre ellos, y el de Lorrena, y de los 800 mil ducados que tenían juntos": Vargas is to find out "el
  fundamento que tiene lo de los 800 mill ducados, y dónde y cómo los tienen, y si mi hermano avía recibido alguna
  parte dellos; mas esto conviene que sea con mucho [tien]to y recato, y sin que persona ninguna pueda entender que
  vos hazeys esta diligencia por orden mía".
- The commission of "aquellos embaxadores de [los Estados?]"; "Mos de Manor[ … ]"; "el aviso … de que el de
  Alanson tenía inteligencias en Filipevila", rightly passed at once to "el Príncipe mi sobrino"; the couriers of
  the Prince; "la buena correspondencia que ha de tener con vos".
Unresolved (selection; full list = every ⟨…⟩ in `f154_v2.txt`): code signs ⟨dn⟩, ⟨hu⟩, ⟨Jo⟩, ⟨te⟩, ⟨Va⟩, ⟨fi⟩,
⟨fu⟩, ⟨ru⟩, ⟨ro⟩, ⟨ci⟩, ⟨Se⟩, ⟨S.⟩, ⟨100?⟩; the 800 numeral with bar; "es gi ca ros" (l. 84). Bracketed words above
are suggestions for these code slots, not decipherments.

## f. 157r–159r · Antonio Pérez · Madrid, 8 Dec 1578
- l. 12: Lo *del [qui]tar la [ … ] de las a[r]mas* se ha considerado y se desseara, pero no se puede assí de golpe…
- l. 14–15: …y según *pl[ … ] tr-da-e-ren tomará [ … ] la [ … ] que más convenga*.
- l. 16: En lo del *[que]-tr-m-ui-ra-to* no ay que dezir sino que al todo tomará mejor término con la nueva orden que
  se ha dado de que no *[ … ] Arcauti [ … ]* sino solo xe.
- l. 19–21: Lo qual se le escrive agora *al Príncipe de Parma*, y con cessar *el manejo del dinero* en los de ay
  *cessarán todos los* [ … ].
- l. 22–25: También cessará agora *la [nu]eva correspondencia que se avía començado en [ … ] Arcauti, y el correo
  mayor, porque con [ … ] los de ay, es [ … ] todo*.
- l. 43–48 (interlinear, partly): …tengo buena esperança de que se ha de coger [ … ] *Arcauti, y a los demás se les
  mandarán las [ … ]*, y crea V.m. que no se quedan entre ringlones *los doze mill [ … ]s*; con[se]*-quería al
  car[ … ] capelo*.
- l. 49–50: Viose la copia de carta *del Príncipe de Parma* para *esse*…
- l. 54–58: …y V.m. crea que no ganaron *d[ … ] Arcauti y capelo en despachar sabiduría de* xe porque pareció
  *a ca mu y m* y fueron avemarías que rezaron contra sí *par[ … ] que se ha tomado*.
- l. 61–66: Su Mag.d vio la carta que V.m. le escrivió a 2 de noviembre *sobre lo de la [lega?]*, y dize que todavía
  procure V.m. de *[en]tender en todo lo que se pudiere, y si fuesse [posible] aver a las manos algunos papeles,
  pero que esto sea con el mayor recato que se[r] [pueda?]*.
- l. 68–70: Muy bueno fue el advertimiento que V.m. escrivió en lo de *Mos de la Mota, de que se [ple]ndasse con*
  encomienda o cosa semejante antes que [ … ] por *con dinero puro* por todo respecto.
Unresolved: l. 12 "le cle"; l. 14 "pl g n ⟨0⟩ tr"; l. 15 ⟨V⟩ and I-curl sign; l. 16 "QUE tr m ui ra to"; l. 18
"a ya a y a r"; l. 22 ⟨i⟩; l. 23 "e n ge a r"; l. 25 "e cla r los de au y", "es re QUE da"; l. 44 caret and triangle
signs; l. 46 ⟨fa⟩; l. 47 f-like sign and ⟨ho?⟩; l. 48 "car ca pe lo"; l. 54 loop-H sign; l. 56 "a ca mu y m";
l. 58 I-curl sign; l. 61 "la la ga"; l. 63 ⟨si⟩; l. 66 ⟨si⟩; l. 68 "ple n da sse"; l. 70 t-like looped sign.
"Arcauti": a Pedro de Arcauti is the addressee of a royal letter in this volume (no. 87, f. 193, 18 Mar 1579,
Tomokiyo's TOC). "capelo" (a cardinal's hat) is a reading of syllables, not an identification.

## f. 179r–180r · Antonio Pérez · Madrid, 26 Jan 1579
- l. 33–35: Y quanto a lo que V.m. dize de que in specie o in genere *llevo en te[n]sa* algo de lo que *[ … ] ha
  escrito del* [ … ],
- l. 36–41: [digo] que aunque se le dio a entender *en general que se tenía alguna noticia* de lo que ha passado
  (porque assí convino), *[fue] con tanto recato que ni por imaginación* él pudo entender *que hu[viesse] [ … ] de
  [ … ]*. Y con esto puede V.m. estar cierto de que ay todo recato en papeles.
- l. 43–49: Con yr sobre aviso de que lo que [he] *de dezir [ … ] solo* venga en la *[carta] particular*, porque el
  [ti]*-de-ta* tiene mucha occupación y no *p[u]ede* recognoscer todas *las [carta]s*, y con esta forma no avrá
  peligro…
- l. 50–53: Quedo avisado del *[ … ]* por lo que dél V.m. me *dize*… y me *guardaré del*, como V.m. me lo advierte.
- l. 67–70: Lo de *García de Arze [ … ]* muy differente *de lo que [ … ] sospechava*. *Se [ … ]* aquella arremetida y
  después de camino que hizo a *cierta co[mi]sión* que se le dio, de que otro día daré cuenta a V.m.
Unresolved: l. 30 "l" after "Soto m.9"; l. 34 "te sa" (tensa? tenga?); l. 35 and 41 ⟨xe⟩; l. 40–41 "hu e ze sa la do
de … na"; l. 43 ⟨E?⟩; l. 44 ⟨ro⟩ and Z-with-crossbar sign; l. 45–46 "el ti de ta" (who has "mucha occupación":
the King? Zayas? a name?); l. 50 struck word and "pa de a ui l"; l. 51–52 "me le i gi no a"; l. 67 "gru"; l. 68 ⟨du⟩,
⟨xe⟩; l. 69 "au e"; l. 70 Z-with-crossbar sign in "co[mi]sión".

## f. 198r–199r · Antonio Pérez · Madrid, 15 April 1579 (v2 of reading v1)
The v2 decode keeps every element of reading v1 (`../02-key-extensions/reading-f198-v1.md`): the office "de Vargas"
the King meant to give Pérez and then decided "desmembrar y repartir"; "el Marqués de los Vélez, Quiroga y [ … ]"
meeting on "lo de la Cancillería de [ … ]"; "la demanda que Escovedo me puso"; "aunque al cabo [se vio] mi inocencia";
"vistos los flacos fundamentos"; "el falso testimonio que le levantaron"; "honrrarme y acrecentarme para reparo de
mi honrra y testimonio de mi inocencia"; "me han procurado quitar la honrra y la vida"; "las mentiras del destierro";
"la verdad es que V.Magd no me ha querido dar licencia, antes dessea que yo me sossiegue y esté quedo"; "por el
Arçobispo de Toledo [ha hecho] dezir a la Princesa de Éboli que procurasse conmigo que me sossegasse y permaneciesse
y quiete su servicio, debaxo de grandes juramentos que el Arçobispo hizo de que V.Magd sentía mucho que yo huviesse
de faltar de aquí; y que, queriendo yo continuar en servir y dexándome en manos de V.Magd, me haría [merced] y favores
y honores … y en esto se anda tratando y tomando agora".
Changes from v1: "ra" (5×) is a cipher-scale sign, not clear script (reconciler, x-height); in four places it fits
"oficio" ("querer me dar el [ra] de Vargas", "se me dava el [ra]", "por lo del [ra] de Vargas"; l. 31 spells "lo del
oficio de Vargas"). Candidate code, in-sample only. l. 9 reads "Quiroga y cli n cl" (a third name; unresolved).
Unresolved: l. 6 ⟨xe?⟩; l. 7 "pr fr de" ("por orden"?); l. 8–9 "y fra pr"; l. 10 "cli n cl"; l. 11–12 "de aa que l
[ra]" (the Cancillería of where?); l. 16 ⟨tt⟩ "tu u"; l. 21, 52 ⟨~^⟩ marks; l. 34 ⟨hu⟩ ("todo lo del [hu]"); l. 37
"qua"; l. 39 "se me el [ra] pom" (se me [quitó?] el [oficio]); l. 45 "si io" (siglo); l. 50 [[Ha]] s (hijos?); l. 53–56
"de se a r to re ti m mi i y ue r pre ce da ho do la de ma n da" (deseo de retirarme … aver precedido la demanda);
l. 70 ⟨po⟩.
