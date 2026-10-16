# f. 202–203: Philip II to Juan de Vargas Mexía, Aranjuez, 17 (or 27) May 1579 — first reading

Witnesses: `f202_A_dec.txt`, `f202_B_dec.txt` (blind readers A and B, guide v2.3, decoder v2.2 frozen `9e0bb0c`).
Agreement on decoded text 97% of A / 97% of B (`compare_decoded.py`, clear text included). Expected decode accuracy
from exp 08: about 86% of decoded letters right. Signed "Yo el Rey", countersigned "Çayas" (both readers).
Date: A "xvij", B "xxvij de Mayo M.D.lxxix"; Tomokiyo's TOC: 17 May. Answers Vargas's letters of 25 and 27 April.

Notation: plain = A and B agree; [word] = supplied for a code or gap (my reading, not decoded); [?] = not resolved.
Code values marked † come from the exp 08 crib (`../08-borja-crib/code_candidates.tsv`), applied here as a reading
aid only; ‡ from context in this letter alone.

## Cipher ¶1 (f. 202r, after the acknowledgement)
"…y [d c?] holgué de entender lo que contienen. No ay que responder a ello más de que sabéis [?] dando [aviso] del
proceder del [Duque]‡ de Alançon con [?] y de lo [que] toca a su casamiento con la [Reyna]‡ de [Inglaterra]‡, que por
más que [se] diga, creo es todo ficción y entretenimiento [para] [?] …"

## Clear (f. 202r–v)
The Franciscan friars sailing to their general chapter; the King has written to the chapter asking for a Minister
General and Commissary General "personas benemeritas"; the General "ha de ser esta vez Italia[no]" by the order's rule;
Vargas is to visit him on the King's behalf.

## Cipher ¶2 (f. 202r)
"…mostrando primero la [carta] de la [?] a fray Antonio de A[gui]lar, [Provincial?]‡ de Santiago, y comunicando con él
lo que será bien que les digáis: que el [Comissario]† que al presente es destos [Reynos]‡ le escrive una [carta] suya
que irá [con esta], para que se entienda con vos y os advierta de lo que conviene, que somos ciertos lo hará con
[mucho] buen zelo; y la comunicación que con él avéis de tener ha de ser dissimulada por todos [respetos] …"

## Cipher ¶3 (f. 202v – 203r)
"[Si] el [Comissario]† [General]‡ … destos [Reynos] … haréis con él el cumplimiento que os paresciere … sin que él lo
entienda, pidáis de mi [parte] al [General] … de una [carta] mía que irá [con esta] … que tenía por bien de confirmar y
proveer de [nuevo] al [Comissario]† que es destos [Reynos], llamado **fray Buenaventura de Santi[báñez?]**, [porque]
demás de ser un religioso [tan] exemplar, tiene todas las otras buenas [partes] que requieren [para] este ministerio,
y ásele de dar la [?] y [facultad] tan cumplida [como] la tiene el [?] [Comissario]; y embiaréisme la [respuesta]. Y si
acaso no le quisiesse confirmar sino que se nombre [otro], daréis [a entender] … que se mire el que será más a
propósito, que … **ni yo consentiré que entre ni sea admitido en estos [Reynos]** … siendo … el exemplo de lo
passado. Dad bien a entender los [inconvenientes] que dello se seguirían, y en esto avéis de insistir de [manera] que o
se quede el Buenaventura … o que el [General] os dé la palabra de que porná en este cargo al religioso que yo le
nombrare; y siendo menester le diréis … que **en [estos Reynos] nunca admiten [Comissario] estrangero** … y que no se
intente lo contrario, [pues] sabéis que no se dará [lugar] a ello, y que conviene complazernos en esto por ser tan
justo y evitar que no se aya de llegar a semejantes términos, procediendo en ello y en todo con el parescer y
comunicación del dicho fray Antonio de A[gui]lar, que lo tiene bien entendido y os advertirá de lo que conviene."

## What is new
- No published or repository reading of this letter was found (inventory in `README.md`).
- The King's secret instruction for the 1579 Franciscan general chapter: keep the current Spanish commissary
  (fray Buenaventura de Santi[báñez?]) confirmed or have the King name his successor, and refuse any foreign
  commissary "en estos Reynos", working through fray Antonio de A[gui]lar and keeping the contact hidden.
- A one-line royal verdict on the Alençon–Elizabeth marriage: "creo es todo ficción y entretenimiento".
- "co" = comissario, a letter-group code first valued on the Borja crib (exp 08), fits here three times.

## Unverified / to check
- Names: "a-i-i-lar" (Aguilar? the decoder's "ii" also stands where "gi" belongs in "reli-ii-oso"); "santiuane…"
  (Santibáñez? Santiváñez?). Who held the Spanish Observant commissariat in 1579 is not checked.
- Context check only: the 1579 chapter elected the Italian Francesco Gonzaga (Wikipedia; Catholic-Hierarchy,
  SECONDARY), consistent with "esta vez Italia[no]". Paris as the chapter's seat is not checked.
- Date xvij vs xxvij: needs the image.
