"""Cipher 4 decoder v2 = decode_v1 (Tomokiyo's key + frozen extensions) with two changes, frozen
2026-10-04 before any reconciled v2 transcription exists:
1. Tokenizer: "<cross above>" (with a space, as some readers wrote it) is normalised to "<crossabove>"
   before splitting. In v1 the space split it into junk tokens.
2. A cross above a sign doubles its consonant (Devos 1950, as reported by Tomokiyo: "a plus sign (+)
   or a caret (^) over a character doubles the letter"). Caret stays a null, as in v1 (Tomokiyo's
   observation). Each doubling is flagged.
Evidence that motivated (2), in-sample, f. 123 reader B decoded by v1: "a que l[+] ma te ri a"
(aquella), "a l[+] de zis" (allí), "se l[+] go" (llegó). Held-out test: f. 154 (not yet transcribed).
    python3 decode_v2.py <transcription>
"""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "02-key-extensions"))
sys.path.insert(0, str(HERE.parent / "01-decode-f198"))
import decode as d
import decode_v1 as v1

_line = v1.decode_line
_split = d.split_token


def split_token(tok):
    core, marks, unc = _split(tok)
    return core, [m for m in marks if m != "<crossabove>"], unc


def decode_line(line, lno, flags):
    line = line.replace("<cross above>", "<crossabove>")
    out = []
    for chunk in re.split(r"(\[\[.*?\]\])", line):
        if chunk.startswith("[["):
            out.append(chunk); continue
        for tok in chunk.split():
            if "<crossabove>" in tok:
                dec = _line(tok.replace("<crossabove>", ""), lno, flags)
                m = re.match(r"^([^aeiouAEIOU]+)(.*)$", dec)
                if m and dec[0].isalpha():
                    dec = m.group(1)[-1] + dec   # double the consonant
                    flags.append(f"{lno} cross above doubles: '{tok}' -> {dec}")
                else:
                    flags.append(f"{lno} cross above on vowel/unknown '{tok}' -> {dec}")
                out.append(dec)
            else:
                out.append(_line(tok, lno, flags))
    return " ".join(out)


d.decode_line = decode_line
if __name__ == "__main__":
    d.main(sys.argv[1])
