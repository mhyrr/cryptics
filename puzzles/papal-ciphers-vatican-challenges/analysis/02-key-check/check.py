"""Apply Tomokiyo's 1628 key (Vatican Challenge Part 1) to the opening of
Barb.lat.6960 image 0005 (Pallotto, Vienna, 4 Aug 1629) and compare with
Kiewning's printed decipherment (Nuntiaturberichte IV/2, Nr. 153).

The digit transcription is a single eye reading (Claude, 2026-10-16) of a
~750 px microfilm image; '?' marks a digit I could not read. The parse into
groups is mine, using 1 and 8 as one-digit word separators (Tomokiyo).
"""
KEY = {  # Tomokiyo, cryptiana.web.fc2.com/code/vatican.htm, "Reconstructed Cipher Key"
    "1": "_", "8": "_", "00": "a", "02": "a", "03": "o", "04": "u", "05": "i",
    "06": "v", "07": "o", "09": "e", "20": "a", "30": "e", "40": "i", "50": "i",
    "60": "u", "70": "o", "90": "e", "22": "p", "23": "s", "24": "b", "25": "t",
    "26": "t", "27": "qu", "29": "n", "32": "c", "33": "d", "34": "b", "35": "t",
    "36": "r", "37": "li", "39": "n", "42": "c", "43": "s", "44": "f", "46": "r",
    "52": "con", "55": "h", "56": "del", "57": "per", "62": "ma", "63": "mi",
    "64": "e", "65": "i", "66": "l", "67": "da", "69": "di", "73": "la",
    "74": "le", "77": "m", "92": "st", "93": "to",
}
# Line 1 as read: 5571 8 365037900693 8 731 13650233770792208 ...
# Parsed (my grouping; alternative readings in comments):
GROUPS = ["55", "7?", "1", "8",              # ho _   (7? read '7', crib wants 70)
          "36", "50", "37", "90", "06", "93",  # r i [37 li; crib c=32] e v [93 to; crib 'uta']
          "8", "73", "1",                     # _ la _
          "1", "36", "50", "23", "37", "70", "79", "22", "0?",  # r i s ? o ? p ?  (crib 'risposta')
          ]
CRIB = "ho ricevuta la risposta"

def dec(g):
    return KEY.get(g, f"[{g}]")

out = "".join(dec(g) for g in GROUPS)
print("groups :", " ".join(GROUPS))
print("decode :", out)
print("crib   :", CRIB.replace(" ", "_"))
known = [g for g in GROUPS if g in KEY]
print(f"groups in key: {len(known)}/{len(GROUPS)}")
