"""sheet_signs.py - the census of VI/82 units 1-4 as read by the outside-check agent -> sheet-signs.tsv.

    python3 sheet_signs.py

The data below are one agent's reading of the key sheets (HOLDS VALUES). One line per sheet cell:
value | shape on the sheet | reader name it was matched to ("none" = the sign guide has no name for it) | units
it was seen on (u1 = unit 1 writing side c. 2r, u1r = unit 1 reading side c. 3v, u2, u3, u4).
A "?" after a reader name marks a guess. Notes in brackets say when one reader name stands for several cells.
"""
import os, collections
HERE = os.path.dirname(os.path.abspath(__file__))
rows = []


def add(block, typ, cells):
    for c in cells.strip().splitlines():
        p = [x.strip() for x in c.split("|")]
        while len(p) < 4:
            p.append("")
        rows.append((block, p[0], typ, p[1], p[2] or "none", p[3]))


add("alphabet", "letter", """
a|plain p|p [in the pair the name p is the ga sign]|u1 u3
a|cursive r|r|u1 u3
a|w with a bar over it|w^bar|u1 u3
b|plain y|y [in the pair the name y is mostly the pe sign]|u1 u3
c|z|z|u1 u3
d|small triangle|triangle|u1 u3
e|g with a closed lower loop|g|u1 u3 u4
e|u|n [not told apart from the t sign]|u1 u3 u4
e|small ring|o|u1 u3
f|plain b|b|u1 u3 u4
g|angular r, like a capital gamma|gamma [mostly written r]|u1 u3 u4
h|figure 3|3|u1 u3 u4
h|m|m|u1 u4
i|H-like: two stems joined at mid height|tt? [not told apart from the ro sign]|u1 u3 u4
i|d with a looped stem|d|u1 u3 u4
l|e with a rising flourish|e [often written c]|u1 u3 u4
m|h|h|u1 u3 u4
n|s|s|u1 u3 u4
o|q drawn like a 9|q [often written g]|u1 u3 u4
o|i|i|u1 u3 u4
o|t|t|u1 u3
p|3 with a tail and a stroke across|3tail [sometimes 3]|u1 u3 u4
q|figure 4 (a q with a cross-loop)|q|u1 u3 u4
q|tall l with dots|l|u1 u3
r|figure 8|8|u1 u3 u4
r|alpha lying on its side|alpha|u1 u3
s|c with two or three inner strokes|sigma? [not told apart from the re sign]|u1 u3 u4
s|plain c|c|u1 u4
t|n|n|u1 u3 u4
t|T or 7 shape|none|u1
u|6-like b with a curled top|beta, b|u1 u3 u4
u|arch|arch|u1 u3 u4
u|ring, bar, ring|odiv? [not told apart from the z sign]|u1 u3 u4
x|long s|none|u1 u3 u4
z|ring over a bar over a dot|odiv|u1 u3 u4
""")
add("Nulle", "null", """
(null)|reversed c with a dot|none [perhaps written c]|u1 u2 u3 u4
(null)|x with a q-like tail|none|u1 u2 u3 u4
(null)|delta with a stroke through it|delta?|u1 u2 u3 u4
(null)|large x with a bar or flourish|xdots? x?|u1 u2 u3 u4
(null)|8 with a wave above|none|u1 u2 u3 u4
(null)|plain alpha|alpha?|u1 u2 u3 u4
(null)|beta|B|u1 u2 u3 u4
(null)|z with a ring above|none|u1 u2 u3 u4
(null)|f or cross between two rings|none|u1 u2 u4
(null)|lambda with a ring above|none|u1 u2 u4
""")
add("syllables", "syllable", """
ba|capital A with a bar|A|u1 u2 u3
be|capital B|B [in the pair B is the null]|u1 u3 u4
bi|6-like b|beta|u1 u3 u4
bo|c with a ring|c^o|u1 u3 u4
bu|y with a ring|y^o|u1 u3 u4
ca|figure 4 with a ring|q^o [not told apart from do]|u1 u2 u3 u4
ce|two stems under a flat bar|tt? hash?|u1 u2 u3 u4
ci|K with a cross|i x|u1 u2 u3 u4
co|2 with a ring|2^o|u1 u2 u3 u4
cu|omega-like|2|u1 u2 u3 u4
con|two slanted strokes crossed by one bar|hash|u1 u2 u3 u4
da|w|w|u1 u3 u4
de|a with a ring|a^o|u1 u2 u3 u4
di|aa|a a|u1 u2 u3 u4
do|q with a ring|q^o|u1 u2 u3 u4
du|c with a small s|c^s|u1 u2 u3 u4
fa|cross with one dot|xdots [not told apart from me]|u1 u2 u3 u4
fe|delta|delta|u1 u2 u3 u4
fi|ee|c c [not told apart from fo]|u1 u2 u3 u4
fo|cc|c c|u1 u2 u3 u4
fu|b with a crossbar|bbar|u1 u2 u3 u4
ga|p with a stroke through the stem|p|u1 u2 u3 u4
ge|f with a ring|f^o|u1 u2 u3 u4
gi|angular r with a ring|r^o [not told apart from ua]|u1 u2 u3 u4
go|q with a bar across the stem|qbar|u1 u2 u3 u4
gu|m with a slanted stroke through it|none|u1 u2 u3 u4
la|ring with a dot|circdot [mostly written theta]|u1 u2 u3 u4
le|alpha with a crossing tail|alpha|u1 u2 u3 u4
li|s with an upright stroke|dollar|u1 u2 u3 u4
lo|m with a ring|m^o|u1 u2 u3 u4
lu|p with a small s|p^s|u1 u2 u3 u4
ma|y with a bar|ybar [mostly written y or 7]|u1 u2 u3 u4
me|cross with four dots|xdots|u1 u2 u3 u4
mi|oo|o o|u1 u2 u3 u4
mo|y with a wave|y^wave|u1 u2 u3 u4
mu|capital N|none|u1 u2 u3 u4
na|three stems under a bar|ttt|u1 u2 u3 u4
ne|ring with a slanted stroke|phi|u1 u2 u3 u4
ni|p with a ring|p^o|u1 u2 u3 u4
no|3 with a ring|3^o|u1 u2 u3 u4
nu|ff|f f|u1 u2 u3 u4
pa|f|f|u1 u2 u3 u4
pe|2 or z shape with a crossed tail|y|u1 u2 u3 u4
pi|ring on a stem|phi [not told apart from ne]|u1 u2 u3 u4
po|z with an upright stroke|stem2bar|u1 u2 u3 u4
pu|z with a bar over it and a long tail|none|u1 u2 u3 u4
qua|figure 9|g [not told apart from the e sign]|u1 u2 u3 u4
que|i with a ring|i^o|u1 u2 u3 u4
qui|d and b under a double stroke|dbbar|u1 u2 u3 u4
quo|two q-like stems crossed by a double bar|hash?|u1 u2 u3 u4
ra|ss|s s|u1 u2 u3 u4
re|c with a comma tail, G-like|sigma|u1 u2 u3 u4
ri|ring with a bar|theta|u1 u2 u3 u4
ro|tt|tt|u1 u2 u3 u4
ru|pp|p p|u1 u2 u3 u4
sa|two stems under a long bar|hash|u1 u2 u3 u4
se|9 with a cross stroke|g? ex?|u1 u2 u3 u4
si|loop on a cross|ex|u1 u2 u3 u4
so|rr|r r|u1 u2 u3 u4
su|hh|h h, b h [sometimes b b]|u1 u2 u3 u4
sul|g with a small cross|none|u1 u2 u3 u4
sal|f and b in one sign|none|u1 u2 u3 u4
sel|8 on its side with a dot|none|u1 u2 u3 u4
ta|bb|b b|u1 u2 u3 u4
te|barred b with a ring|bbar^o|u1 u2 u3 u4
ti|M-like sign with a cross-tailed stroke|h y|u1 u2 u3 u4
to|C with a dot|moondot|u1 u2 u3 u4
tu|dd|d d|u1 u2 u3 u4
ua|r with a ring|r^o|u1 u2 u3 u4
ue|t with a wave|t^wave|u1 u2 u3 u4
ui|p with a tick|p^tick|u1 u2 u3 u4
uo|8 with a small 3|8^3|u1 u2 u3 u4
uu|3 with a small 3|none|u1r u2 u3 u4
""")
add("Duple", "double", """
bb|ring with a flag|delta?|u1 u2 u3 u4
cc|triangle with a tail|triangle?|u1 u2 u3 u4
dd|C enclosing a c|none|u1 u2 u3 u4
ff|square G|none|u1 u2 u3 u4
gg|two stems with a ring between|none|u1 u2 u3 u4
mm|ooo|none [would be o o o]|u1 u2 u3 u4
nn|qq|none [would be q q]|u1 u2 u3 u4
pp|two tall stems crossed by a double bar|hash?|u1 u2 u4
rr|KK|none|u1 u2 u4
ss|capital A with a small cross|A|u1 u2 u4
tt|z with a curl|none|u1 u4
""")
add("Dictioni", "word", """
che|upright cross with dots|dotcross|u1 u2 u3 u4
come|c running into a looped stem|d [the guide's picture of d]|u1 u2 u3 u4
quando|capital R|R|u1 u2 u3 u4
sempre|capital P|none|u1 u2 u3
et|box with a dot|boxdot|u1 u2 u3 u4
non|ring joined to a t|none|u1 u2 u3 u4
benche|large 8|8 [not told apart from the r sign]|u1 u2 u3 u4
perche|large ring (u1: with a stroke and a dot)|O|u1 u2 u3 u4
anchora|L with a small cross|Lx|u1 u2 u3 u4
quanto|ring on a stem with a flag|none|u1 u2 u4
uostro|ring joined to a b|none|u1 u2
nostro|large ring with a bar|theta?|u1 u2
piu|m with a small s|m^s|u1
ogni|8 with a bar through it|none|u1 u2
tanto|N with a cross-tailed stroke|none|u1 u2
assai|cross with a top bar|none|u1 u2
nondimeno|C and K|none|u1 u2
amore|delta joined to an s|none|u1 u2
scripto|f with two bars|stem2bar?|u1
parere|2 with a ring and a long tail|none|u1 u2
tempo|f or x with a small c|none|u1 u2
fine [reading of the heading word uncertain]|v with a wave|v?|u1 u2
huomo|large ring on a long stem|phi?|u1 u2
effecto|c joined to a t|none|u1 u2
importantia|three stems under a flat bar|ttt?|u1 u2
sapere|ring, slash, ring|none|u1 u2
siamo|b with a cross on top|none|u1 u2
uogliamo|two rings under a bar|none|u1 u2
""")
add("names (two-figure numbers)", "name", """
Re di Francia|32|3 2|u3 u4
Papa|43|q 3, q 3tail|u3 u4
Viniziani|22|2 2|u3 u4
Sanesi|23|none|u3 u4
Genovesi|72|none|u3 u4
Lucchesi|2|none|u3 u4
Pisani|39|none|u4
Roano|86|none|u4
Re di Spagna|42|none|u3 u4
Fiorentini|21|none|u3 u4
Ciamonte|3|none|u3 u4
Imperatore|31|3 i, 3tail i?|u3 u4
Orsini|8|none|u4
Vitelli|9|none|u4
Colonnesi|7|none|u4
Pandolfo|15|none|u3 u4
Giampaulo|26|none|u4
Duca d'Urbino|18|none|u3 u4
M. Giovanni|92|none|u4
Consalvo|41|none|u3 u4
Pavia [reading uncertain]|71|none|u3 u4
La Trimolle|40|none|u3
[..] d'Inghilterra (torn)|98|none|u3
[..] di Savoia (torn)|90|none|u3
[..]inghilterra? (torn)|83|none|u3
[..] di Angolem (torn)|87|none|u3
""")

with open(os.path.join(HERE, "sheet-signs.tsv"), "w", encoding="utf-8") as f:
    f.write("block\tvalue\ttype\tshape_on_sheet\treader_name\tseen_on\n")
    for r in rows:
        f.write("\t".join(r) + "\n")
by = collections.Counter(r[0] for r in rows)
unnamed = collections.Counter(r[0] for r in rows if r[4].startswith("none"))
print("cells read: %d" % len(rows))
for b in by:
    print("  %-28s %3d cells, %3d with no reader name" % (b, by[b], unnamed[b]))
print("no reader name in all: %d" % sum(unnamed.values()))
