# 13. The three unpaired cipher letters of 7 Feb 1580 (BnF fr. 16107): duplicates of 31 Jan

**Question.** Three letters of Saint-Goard dated 7 Feb 1580 contain cipher and have no decipherment sheet anywhere in
fr. 16107 (`analysis/12-sweep-fr16107/`). Are they unread text?

**Bar (fixed before reading).** Two independent readers per letter (`BRIEF.md`; protocol of
`analysis/10-saint-goard/GUIDE.md`, show-through subtracted with `unbleed.py`). A letter counts as unread only if its
content matches no decipherment sheet in the volume.

**Result: all three are duplicates of the 31 Jan 1580 dispatch, already deciphered. Nothing here is unread.**
The 7 Feb "sur la mort" letter says so in clear: "Le dernier du passé j'ay escript bien au long a Vostre Majesté, et luy
en envoye les dupplicata avec ceste cy" ("On the last of last month I wrote at length to Your Majesty, and send the
duplicates with this"). Each duplicate has a new clear opening and a closing dated 7 Feb round the old cipher.

| 7 Feb letter | duplicates | sheet | evidence (main thread, on the images) |
|---|---|---|---|
| R, Queen Mother, ff. 59r–61v | 31 Jan to the Queen Mother | ff. 38–39 | Readers X and Y, 59v L01–05, against the sheet's first four lines: "Quant a ce qui touche les affaires de Portugal je diray a Vostre Majesté qu'[hier] il y arriva ung courrier depesché en toutte dilligence des ambassadeurs du Roy catholique qui sont de pardela". The readers' content (the Cortes, Philip against the duchess of Bragança, La Mothe-Fénelon) is January news. |
| A, King, ff. 40r–43v | 31 Jan (2) to the King | ff. 32–33 | Readers X and Y, 40v L08–41r L06, against the sheet's ll. 6–11: Mondéjar arrived at Cartagena with the rest of the army; what kept him at "Gayette"; leave for "une entreprise … de tres grande importance". Middle: both have the present sent to Constantinople and "Jehan de Marian" (f. 33r; reader X 42r). The end was not compared. |
| B, King, ff. 44r–47r | 31 Jan (1) to the King | ff. 24–26 | Opening only: B's clear "Sire, depuis ma dernière escripte j'ay encores eu loisir de fere ceste" plus first cipher words "[par] la [q]ue d…" (`../12-sweep-fr16107/join-7feb.md`) against the sheet's "Sire, depuis ma dernière escripte … je diray a Vostre Majesté". **Weakest of the three; not read by the two readers.** |

So every cipher letter in fr. 16107 is accounted for by a contemporary decipherment in the volume. The one orphan sheet
(6 Dec 1580, ff. 361r–363r) lacks its cipher original.

**Why the earlier check missed it.** The main thread tested for duplicates by closing date and clear text. Both are
new in a duplicate; only the cipher is repeated. Rule: test a suspected duplicate on the cipher's content.

## Files
`BRIEF.md`; `readerX/`, `readerY/` (letters R and A; token rows and French). Images are not in git
(`sources/cache/fr16107/unbleed/`, made with `UNBLEED_CACHE=…/fr16107 unbleed.py <page> <view> <side> <other_view> <other_side>`).

## Limits and not done
- No script scored the readers against the sheets: the 31 Jan sheets are not transcribed. The matches above are
  passages compared by eye, so no agreement figure is claimed (rule 6).
- B rests on its opening. The ends of A and B were not compared.
- Reader X reports `unbleed/60r-01b.jpg` mirrored left to right; `unbleed.py` not yet checked for the cause.
- Readers disagree with the brief on some signs (`∂` = l as well as z; the flat double loop = u/v in places). Their
  lists are in each file's "New or doubtful signs". These would matter for a future key table, not for this result.
- Cost: four Opus readers, about 270–340k tokens each.
