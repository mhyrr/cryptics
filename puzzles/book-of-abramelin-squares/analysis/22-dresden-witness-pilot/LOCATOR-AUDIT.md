# Dresden N 111 locator audit

This is a post hoc source-only locator adjudication. It does not replace the
frozen primary result. The audit used only the PRIMARY manuscript images
`p243.jpg`, `p244.jpg`, and `p245.jpg` plus their hashes in
`image-manifest.json`. It did not consult square transcriptions, predictions,
results, canon, hypotheses, other source images, or other experiments. No
square letters are transcribed here.

## Page traversal

All three pages belong to Book IV. A book number and a chapter number are
different levels: the book stays at IV while the visible chapter headings move
from chapter 1 to chapter 4.

The item sequence runs down each column, then moves to the next column on the
right. Page 243 has one large item per column, so items 1-3 also appear
left-to-right. Page 244 removes the ambiguity: chapter 1 items 4-6 run down
column 1, items 7-10 run down column 2, and item 11 sits at the top of column
3. Chapter 2 starts below item 11 in column 3. Page 245 continues chapter 2 at
the top of column 1, starts chapter 3 below it, continues chapter 3 down column
2, starts chapter 4 below it, and continues chapter 4 down column 3.

Stable IDs use `pPPP-cC-gG`: physical page, column counted left-to-right, and
grid counted top-to-bottom within that column. Bounding boxes in the JSON are
coarse normalized locator regions. They include each heading and grid.

## Chapter headings

- Book IV, chapter 1, physical page 243: “Liber Quartus! Cap: 1. Alle
  Vergangene und Künftige Dinge, so nicht wieder Gott und seinen Willen zu
  wissen.”
- Book IV, chapter 2, physical page 244: “Lib IV Cap 2. Gericht auff aller hand
  zweiffelhaffte Sachen zu haben.”
- Book IV, chapter 3, physical page 245: “Lib: IV. Cap 3. Einen jeden Geist
  erscheinen machen.”
- Book IV, chapter 4, physical page 245: “Lib: IV. Cap: 4. allerley gesichte zu
  haben.”

## Grid locators

| Stable ID | Physical page (label) | Source locator | Page region | Literal short heading |
|---|---:|---|---|---|
| `p243-c1-g1` | 243 (240) | IV.1.1 | column 1, bottom | “1. Vergangene und künftige Dinge zu wissen.” |
| `p243-c2-g1` | 243 (240) | IV.1.2 | column 2, bottom | “2. zukünftige Sachen” |
| `p243-c3-g1` | 243 (240) | IV.1.3 | column 3, bottom | “3. zukünftige Sachen.” |
| `p244-c1-g1` | 244 (241) | IV.1.4 | column 1, top | “4. Zukünftige vom Krieg.” |
| `p244-c1-g2` | 244 (241) | IV.1.5 | column 1, middle | “5. Vergangene Sachen zu wissen.” |
| `p244-c1-g3` | 244 (241) | IV.1.6 | column 1, bottom | “6. zukünftige Dinge von Betrübniß [vor/wor] zu wissen.” |
| `p244-c2-g1` | 244 (241) | IV.1.7 | column 2, top | “7. künftige Dinge.” |
| `p244-c2-g2` | 244 (241) | IV.1.8 | column 2, upper-middle | “8. Vergangene Dinge.” |
| `p244-c2-g3` | 244 (241) | IV.1.9 | column 2, lower-middle | “9. Wunder Zeichen u: Witterung zu wissen.” |
| `p244-c2-g4` | 244 (241) | IV.1.10 | column 2, bottom | “10. zukünftige Dinge.” |
| `p244-c3-g1` | 244 (241) | IV.1.11 | column 3, top | “11. künftige Dinge.” |
| `p244-c3-g2` | 244 (241) | IV.2.1 | column 3, middle | “1.” |
| `p244-c3-g3` | 244 (241) | IV.2.2 | column 3, bottom | “2.” |
| `p245-c1-g1` | 245 (242) | IV.2.3 | column 1, top | “3.” |
| `p245-c1-g2` | 245 (242) | IV.3.1 | column 1, middle | “1. In gestalt eines Drachens.” |
| `p245-c1-g3` | 245 (242) | IV.3.2 | column 1, bottom | “2. In Thieres gestalt.” |
| `p245-c2-g1` | 245 (242) | IV.3.3 | column 2, top | “3. In Menschen gestalt.” |
| `p245-c2-g2` | 245 (242) | IV.3.4 | column 2, middle | “4. In Vogel gestalt.” |
| `p245-c2-g3` | 245 (242) | IV.4.1 | column 2, bottom | “1. In Spiegel glaß und Crystall.” |
| `p245-c3-g1` | 245 (242) | IV.4.2 | column 3, top | “2. In hohen gewölben und gärthen, grüfften der Erden.” |
| `p245-c3-g2` | 245 (242) | IV.4.3 | column 3, middle | “3. In der lufft.” |
| `p245-c3-g3` | 245 (242) | IV.4.4 | column 3, bottom | “4. In Edelgestein und Ringen.” |

The item number is legible for every located grid. Chapter 2 items 1-3 have
only a number as their short heading. One word in IV.1.6 reads as either
“vor” or “wor”; the locator itself is unaffected.
