import re, html, sys
src, tpl, out = sys.argv[1:4]
md = open(src, encoding="utf-8").read()

CI = [False]
def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', t)
    t = re.sub(r"\*\*(.+?)\*\*", (r'<strong class="ci">\1</strong>' if CI[0] else r'<strong>\1</strong>'), t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
    return t

lines = md.split("\n")
outh, toc, i = [], [], 0
def slug(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:40]
while i < len(lines):
    L = lines[i]
    if L.startswith("# "):
        i += 1; continue  # title is in template
    if L.startswith("## "):
        t = L[3:]; sid = slug(t); toc.append((sid, t)); CI[0] = t.startswith(("4.", "7."))
        outh.append(f'<h2 id="{sid}">{inline(t)}</h2>'); i += 1; continue
    if L.startswith("### "):
        outh.append(f'<h3>{inline(L[4:])}</h3>'); i += 1; continue
    if L.strip() == "---":
        i += 1; continue
    if L.startswith("|"):
        rows = []
        while i < len(lines) and lines[i].startswith("|"):
            rows.append(lines[i]); i += 1
        cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
        head, body = cells[0], [r for r in cells[2:]]
        h = '<div class="tw"><table><thead><tr>' + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>"
        h += "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body) + "</tbody></table></div>"
        outh.append(h); continue
    if L.startswith("- "):
        items = []
        while i < len(lines) and (lines[i].startswith("- ") or lines[i].startswith("  ")):
            if lines[i].startswith("- "): items.append(lines[i][2:])
            else: items[-1] += " " + lines[i].strip()
            i += 1
        outh.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>"); continue
    if not L.strip():
        i += 1; continue
    para = [L]; i += 1
    while i < len(lines) and lines[i].strip() and not re.match(r"^(#|\||- |---)", lines[i]):
        para.append(lines[i]); i += 1
    cls = ' class="note"' if para[0].startswith("*") and para[0].rstrip().endswith("*") and len(para) <= 3 and "Overview of" in para[0] else ""
    outh.append(f"<p{cls}>{inline(' '.join(para))}</p>")
tocd = "".join(f'<li><a href="#{s}">{html.escape(re.sub(r"^\\d+\\. ", "", t))}</a></li>' for s, t in toc)
page = open(tpl, encoding="utf-8").read().replace("{{BODY}}", "\n".join(outh)).replace("{{TOC}}", tocd)
open(out, "w", encoding="utf-8").write(page)
print(len(page))
