"""Fill reader-prompt.md for one job. python3 mkprompt.py LETTER OUT ORDER page1 page2 ..."""
import sys, re
from pathlib import Path
t = Path(__file__).with_name("reader-prompt.md").read_text().split("\n---\n", 1)[1]
letter, out, order, pages = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:]
P = "puzzles/vargas-mexia-es132/sources/cache/pages/exp07/"
if order == "reverse":
    pages = pages[::-1]
note = ("begin with the last page and work back to the first; within each page, read top to bottom"
        if order == "reverse" else "first page to last")
t = (t.replace("{LETTER}", letter).replace("{OUT}", "puzzles/vargas-mexia-es132/sources/transcription/" + out)
      .replace("{ORDER_NOTE}", note).replace("{ORDER}", order)
      .replace("{PAGES}", "\n".join(f"- `{P}{p}.jpg`" for p in pages)))
print(t)
