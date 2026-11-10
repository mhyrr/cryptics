"""H22: which desk did Saint-Goard's copies of Spanish state papers come from?

Builds papers.tsv (one row per copied Spanish/Portuguese paper in BnF fr. 16106, views 218-390) and prints
the counts used in README.md.

Inputs : ../10-saint-goard/index-{196-260,261-325,326-391}.tsv (one row per spread; the descriptive source)
         DOCS below: the document segmentation (start view, writer, addressee, date) transcribed from those
         index rows, plus IMAGE readings of dorses made on the images 2026-11-10 (see README "Image readings").
Output : papers.tsv, counts on stdout.
Run    : python3 build.py      (standard library only)

The script checks that every view cited in DOCS exists in the index, copies the index's own dorse wording for
the dorse view (so the reader can audit the transcription), parses received/answered dates from the dorse text,
and does all counting. Nothing is counted by hand.
"""
import csv, os, re, sys
from collections import Counter
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
IDX = os.path.join(HERE, "..", "10-saint-goard")
ARREST = date(1579, 7, 28)            # arrest of Antonio Pérez
FRENCH_DISPATCHES = [date(1579, 11, 12), date(1579, 12, 23)]   # Saint-Goard dispatches present in the volume

def load_index():
    rows = {}
    for fn in ("index-196-260.tsv", "index-261-325.tsv", "index-326-391.tsv"):
        with open(os.path.join(IDX, fn), encoding="utf-8") as f:
            for r in csv.DictReader(f, delimiter="\t"):
                try:
                    rows.setdefault(int(r["view"]), r)
                except ValueError:
                    pass
    return rows

# Document segmentation. Fields:
# id, start view, last view, date as written, iso date ('' if undated; YYYY-MM-DD, day 15 if only month known),
# place, writer, addressee, addressee class (KING / ZAYAS / OTHER / NONE), kind, state_paper (Y/N),
# language, dorse view ('' if none recorded), zayas link, royal holograph notes copied (Y/N), route note.
K, Z, O, N = "KING", "ZAYAS", "OTHER", "NONE"
DOCS = [
 ("alava",      218, 223, "Madrid 28 May 1579 (text 25 May)", "1579-05-28", "Madrid", "Francés de Álava", "Philip II", K, "parecer", "Y", "es", 224, "", "N", "advice paper; King asked Vargas 29 Nov 1579 how a Portugal advice paper reached Paris"),
 ("vilareal",   224, 224, "a xj de Junho 1579", "1579-06-11", "Lisbon?", "Marquês de Vila Real", "Henri III", O, "letter to the French king", "N", "pt", 226, "", "N", "addressed to Henri III; French route, not Madrid"),
 ("poder-alba", 226, 227, "San Lorenzo, [blank] Junio 1579", "1579-06-15", "San Lorenzo", "Philip II", "conde de Alba de Liste", O, "royal poder (minute/copy)", "Y", "es", 228, "", "N", "outgoing royal paper"),
 ("miranda",    228, 228, "Junio 1579", "1579-06-15", "", "Philip II", "ciudad de Miranda", O, "royal letter (copy)", "Y", "es", 229, "", "N", "outgoing royal paper"),
 ("capitanes",  229, 230, "en ocho de Julio 1579", "1579-07-08", "", "(secretariat list)", "-", N, "list of captains", "Y", "es", 231, "", "N", "war-side list"),
 ("frailes",    231, 231, "Bayona, 2 agosto 1579", "1579-08-02", "Bayonne", "Fr. Molina and Fr. Pedro Manrique", "Philip II", K, "letter", "Y", "es", 233, "", "N", "dorse 'Al Rey'"),
 ("vm-0808",    233, 234, "Lisboa agosto 8 1579", "1579-08-08", "Lisbon", "Rodrigo Vázquez and Luis de Molina", "Philip II", K, "letter", "Y", "es", 235, "", "N", ""),
 ("guard-0810", 235, 236, "Lisboa a x de agosto 1579", "1579-08-10", "Lisbon", "Licenciado Guardiola", "Gabriel de Zayas", Z, "capítulo of letter", "Y", "es", 237, "addressee", "N", "extract ('capítulo') of a letter to Zayas"),
 ("nuncio-0810",237, 238, "Di x d'Agosto 1579", "1579-08-10", "Rome?", "papal letter / nuncio", "Philip II via nuncio", K, "papal letter (copy)", "Y", "it", 239, "", "N", "dorse 'El officio que ha hecho el Nuncio con su Mag.d'"),
 ("vargas-0824",239, 241, "de Paris a 24 de agosto 1579", "1579-08-24", "Paris", "Juan de Vargas Mexía (deciphered)", "Philip II", K, "deciphered letter", "Y", "es", 241, "", "N", "Paris dispatch, deciphered in Madrid ('Descifrada'); not a Portugal paper"),
 ("rey-mora-0826",241, 243, "26 Aug 1579 (heading); 'De Madrid' no day", "1579-08-26", "San Lorenzo/Madrid", "Philip II", "Cristóbal de Moura", O, "royal letter", "Y", "es", 245, "named-as-handler", "N", "text: Moura's letters received 'como os lo ha avisado Cayas'"),
 ("rey-vm-0826",245, 246, "de Sant Lorenço a 26 de Agosto 1579", "1579-08-26", "San Lorenzo", "Philip II", "Vázquez and Molina", O, "royal letter", "Y", "es", 247, "countersigned", "N", "'Yo el Rey' countersigned 'Cayas' (image)"),
 ("rey-raya",   247, 248, "de St Lorenço a [blank] de Agosto 1579", "1579-08-15", "San Lorenzo", "Philip II", "frontier lords (Cerralbo et al.)", O, "royal circular (copy)", "Y", "es", 249, "", "N", "dorse 'Copia de la carta que su Mag.d escrivio'"),
 ("henrique",   249, 249, "1579", "", "", "King Henrique (copy)", "?", O, "royal letter (copy)", "Y", "pt", "", "", "N", ""),
 ("pina",       250, 251, "Aos [30?] dias de Junho 1579", "1579-06-30", "Lisbon", "Dr Fernão de Pina Marecos", "King Henrique", O, "petition", "Y", "pt", 252, "", "N", ""),
 ("savoy-pet",  251, 251, "1579", "", "Lisbon", "procurator of Savoy", "King Henrique", O, "petition", "Y", "es?", "", "", "N", ""),
 ("escrit",     252, 256, "1579", "", "", "anonymous (for Philip II)", "Philip II", K, "memorial", "Y", "es", 256, "", "N", "dorse 'Presupuesto lo que se resolvio en las cortes de Lisboa'"),
 ("discurso",   256, 260, "1579", "", "", "a Portuguese (anonymous)", "Philip II / Señores", K, "discourse", "N", "es", 260, "", "N", "partisan discourse"),
 ("memoria-pueblo",260, 265, "1579", "", "", "anonymous Portuguese", "'su pueblo'", O, "pamphlet", "N", "es", "", "", "N", "docket: 'publié par un Portugais'"),
 ("platica",    265, 265, "1579", "", "", "four heads of the people", "estados de Portugal", O, "speech", "N", "es", "", "", "N", ""),
 ("nuevas-0828",266, 270, "Lisboa, xxviij de agosto 1579", "1579-08-28", "Lisbon", "unsigned newsletter", "'V.m.' (unnamed), address leaf to Paris", O, "newsletter", "N", "es", 271, "", "N", "address leaf (v271 left, image): 'Al muy mag.co señor ... Paris' — sent to Paris, not via Madrid"),
 ("junta-apunt",271, 272, "1579 ('Para la Junta')", "", "", "Spanish council/junta", "junta / envoys to Portugal", O, "council paper", "Y", "es", 273, "", "N", "dorse 'Apuntamientos para el despacho de los que van a Portugal'"),
 ("rey-camara", 273, 274, "1579", "", "", "Philip II (copy)", "Câmara de Lisboa", O, "royal letter (copy)", "Y", "es", "", "", "N", ""),
 ("peticion-1", 275, 276, "1579", "", "", "Osuna, Moura, Vázquez, Molina (draft)", "King Henrique", O, "draft petition ('Primera forma')", "Y", "es", 277, "", "N", "Madrid draft"),
 ("peticion-2", 277, 278, "1579", "", "", "same (draft)", "King Henrique", O, "draft petition ('Segunda forma')", "Y", "es", 279, "", "N", "Madrid draft"),
 ("molina-0918",279, 283, "Lisboa, 18 de 7bre 1579", "1579-09-18", "Lisbon", "Dr Luis de Molina", "Philip II ('en su mano')", K, "letter", "Y", "es", 285, "", "N", "dorse 'A S.M. en su mano' with abstract"),
 ("medina-0918",284, 285, "De Sevilla xviij de 7bre 1579", "1579-09-18", "Seville", "Duque de Medina Sidonia", "Philip II", K, "letter", "Y", "es", 287, "", "N", ""),
 ("medina-sosa",285, 286, "bosque de las Rocinas, ? agosto 1579", "1579-08-15", "Rocinas", "Duque de Medina Sidonia", "Francisco de Sosa", O, "memorial (enclosure)", "Y", "es", "", "", "N", ""),
 ("vm-0922",    287, 288, "De Lisboa 22 [7bre] 1579", "1579-09-22", "Lisbon", "Vázquez and Molina", "Philip II", K, "letter", "Y", "es", 289, "named-as-handler", "N", "French docket mentions 'Secretaire Çayas'"),
 ("porto",      289, 289, "22 de septiembre 1579", "1579-09-22", "Porto", "ayuntamiento of Porto (copy)", "Câmara de Lisboa", O, "letter (enclosure)", "Y", "es", 290, "", "N", ""),
 ("vazquez-0922",290, 292, "de Lisboa 7bre 22 1579", "1579-09-22", "Lisbon", "Rodrigo Vázquez", "Philip II", K, "letter", "Y", "es", 292, "named-as-handler", "N", "text names 'Gabriel de Çayas'"),
 ("mora-0923a", 292, 294, "De Lisboa a 23 de 7bre 1579", "1579-09-23", "Lisbon", "Cristóbal de Moura", "Philip II", K, "letter", "Y", "es", 296, "", "N", ""),
 ("abstract-mora",295, 295, "23 Sept 1579 (docket)", "1579-09-23", "Madrid", "(secretariat abstract of Moura)", "-", N, "secretariat abstract", "Y", "es", "", "", "N", "point-by-point abstract made for the King"),
 ("mora-0923b", 296, 297, "de Lisboa a 23 de 7bre 1579", "1579-09-23", "Lisbon", "Cristóbal de Moura", "Philip II", K, "letter", "Y", "es", 298, "", "N", ""),
 ("osuna-dem",  298, 305, "En Lisboa a [blank] de Septiembre 1579", "1579-09-15", "Lisbon", "Duque de Osuna", "King Henrique", O, "demands (copy)", "Y", "es", 306, "", "N", "dorse refers to S.M. letter of 24 Aug 1579"),
 ("guard-0923", 305, 306, "De Lisboa a 23 de 7bre 1579", "1579-09-23", "Lisbon", "Licenciado Guardiola", "Gabriel de Zayas", Z, "capítulos of letter", "Y", "es", 307, "addressee", "N", ""),
 ("autos",      307, 313, "Feb-Sep 1579", "1579-09-26", "Lisbon", "Roque Vieira (escrivão); Zayas certification", "-", N, "judicial acts (copy)", "Y", "es/pt", 315, "certifies", "N", "includes certification by Gabriel de Çayas, Madrid 8 Mar 1579"),
 ("puntos",     315, 315, "1579", "", "", "Spanish council", "junta", O, "council paper", "Y", "es", 317, "", "N", "dorse 'Los puntos que se han de ver en la Junta'"),
 ("vazquez-mem",317, 326, "1579 (answers S.M. letter 'de 26 del passado')", "1579-09-15", "Lisbon", "Licenciado Rodrigo Vázquez", "Philip II", K, "legal memorial", "Y", "es", 327, "", "N", ""),
 ("guard-mem",  326, 332, "1579", "", "", "Licenciado Guardiola", "-", N, "legal memorial", "Y", "es", 333, "", "N", ""),
 ("razones",    333, 333, "1579", "", "", "anonymous Spanish", "-", N, "memoria", "Y", "es", "", "", "N", ""),
 ("pro-antonio",338, 339, "1579", "", "", "anonymous pro-Antonio", "-", N, "memorial", "N", "es", 340, "", "N", "Spanish dorse 'Las razones con que el Señor Don Anthonio'"),
 ("vm-1009",    343, 344, "De Lisboa 9 [octubre] 1579", "1579-10-09", "Lisbon", "Vázquez and Molina", "Philip II", K, "letter", "Y", "es", 345, "", "N", ""),
 ("osuna-1010", 345, 346, "En Lisboa a 10 de octubre 1579", "1579-10-10", "Lisbon", "Duque de Osuna", "Philip II", K, "letter", "Y", "es", 347, "named-as-handler", "N", "acts sent to 'Secretario Cayas'"),
 ("mora-1010",  347, 348, "De Lisboa a 10 de octubre 1579", "1579-10-10", "Lisbon", "Cristóbal de Moura", "Philip II", K, "letter", "Y", "es", 349, "named-as-handler", "N", "text names 'Secretario Cayas'"),
 ("osuna-1014k",349, 349, "De Lisboa a 14 de octubre 1579", "1579-10-14", "Lisbon", "Duque de Osuna", "Philip II", K, "letter", "Y", "es", 351, "named-as-handler", "N", "text names 'Secretario Cayas'"),
 ("osuna-1014z",350, 352, "Lisboa 14 octubre 1579", "1579-10-14", "Lisbon", "Duque de Osuna", "Gabriel de Zayas", Z, "capítulos of letter", "Y", "es", "", "addressee", "N", ""),
 ("parecer-1014",353, 354, "14 oct. 1579", "1579-10-14", "Lisbon", "Osuna and other ministers", "Philip II", K, "parecer", "Y", "es", 355, "", "N", ""),
 ("abstract-1014",355, 355, "Don Xpoval de Mora de 14 de octubre 1579 (dorse)", "1579-10-14", "Madrid", "(secretariat summary of a Moura letter)", "-", N, "secretariat abstract", "Y", "es", 355, "", "N", "dorse on the summary itself"),
 ("mora-1014z", 356, 358, "de Lisboa a 14 de octubre 1579", "1579-10-14", "Lisbon", "Cristóbal de Moura", "Gabriel de Zayas", Z, "letter", "Y", "es", "", "addressee", "N", ""),
 ("vazquez-1014z",358, 358, "De Lisboa octubre 14 1579", "1579-10-14", "Lisbon", "Rodrigo Vázquez", "Gabriel de Zayas", Z, "letter", "Y", "es", 359, "addressee", "N", ""),
 ("osuna-1018", 359, 360, "De Lisboa a 18 de octubre 1579", "1579-10-18", "Lisbon", "Duque de Osuna", "Philip II", K, "letter", "Y", "es", 361, "named-as-handler", "N", "text names 'Secretario Cayas'"),
 ("mora-1018",  361, 362, "De Lisboa a 18 [8bre] 1579", "1579-10-18", "Lisbon", "Cristóbal de Moura", "Philip II", K, "letter", "Y", "es", 363, "", "N", ""),
 ("guard-1018", 363, 363, "Lisboa 18 de oct de 79", "1579-10-18", "Lisbon", "Licenciado Guardiola", "Gabriel de Zayas", Z, "letter", "Y", "es", "", "addressee", "N", ""),
 ("mora-1019",  364, 367, "De Lixa a 20(?) de octubre 1579", "1579-10-19", "Lisbon", "Cristóbal de Moura", "Philip II", K, "letter", "Y", "es", 368, "", "N", ""),
 ("vm-1025",    368, 368, "De Lisboa obtubre 25 1579", "1579-10-25", "Lisbon", "Vázquez and Molina", "Philip II", K, "letter", "Y", "es", 369, "", "N", ""),
 ("mora-781229",379, 383, "de Lisboa 29 de [dic]bre (1578 per heading)", "1578-12-29", "Lisbon", "Cristóbal de Moura", "Philip II", K, "letter", "Y", "es", 384, "", "Y", "copy carries 'De mano del Rey' / 'De mano de Su Md.' marginal notes (image)"),
 ("sentencia",  385, 386, "decemb. 1579 (archival margin)", "1579-12-15", "Lisbon", "King Henrique", "-", N, "sentence (copy)", "Y", "pt", 387, "", "N", "public sentence; Spanish dorse 'Copia de la sente[ncia]'"),
 ("nuncio-turk",387, 390, "1579", "", "", "papal nuncio", "Philip II", K, "memorial (Italian)", "Y", "it", 391, "", "N", "dorse at v391 is French"),
]

# Dorses read on the images 2026-11-10 (override/extend the index wording). Keyed by doc id.
IMAGE = {
 "vm-0808":    "Lisboa. A Su Mag.d. R° Vasquez y Molina a viij de agosto. Recebida en xvj [or xv] del mismo. Sacada en relacion.",
 "vargas-0824":"Descifrada. Paris. Juan de Vargas Mexia a xxiiij de Agosto 1579. Recibida en iiij de sept.e",
 "molina-0918":"Lisboa. A Su Mag.d en su mano. Del doctor Luys de Molina a 18 de 7bre 1579 + abstract (no received date seen)",
 "vm-1025":    "Lisboa. A Su Mag.d. R° Vazquez y Molina de 25 de octubre 1579. Rda a 28 del mismo + abstract",
 "mora-781229":"(v384 left: no dorse legible; only mirror show-through and a strip of another letter)",
 "parecer-1014":"(index) Parecer del Duque de Ossuna, 14 de oct 1579 [no received date noted; the received note on v355 belongs to the Moura summary]",
 "abstract-1014":"(index) Don Xpoval de Mora de 14 de octubre 1579, Rda a 18 del mismo",
 "mora-1019":  "(index) Don Xpoval de Mora de 2?[0] de octubre ... Rda a 25",
 "nuevas-0828":"(v271 left, upside down) 'Al muy mag.co señor ... [name not read] ... Paris', seal trace",
}

ROMAN = {"i": 1, "v": 5, "x": 10, "l": 50}
def roman(s):
    s = s.lower().replace("j", "i").replace("°", "").replace("º", "")
    tot = prev = 0
    for ch in reversed(s):
        v = ROMAN.get(ch, 0)
        tot = tot - v if v < prev else tot + v
        prev = max(prev, v)
    return tot

MONTHS = {"agosto": 8, "ago": 8, "sept": 9, "7bre": 9, "septiembre": 9, "octubre": 10, "oct": 10, "8bre": 10}
RECV = re.compile(r"(?:Recebida|Recibida|Reci\.?da|Rda|R\.|\.\.\.|\ben)\s*(?:en\s+|a\s+)?([0-9]+|[ivxlj°]+)\b\s*(?:\[[^\]]*\])?\s*(?:(?:de|del)\s+(mismo|[a-z0-9]+))?", re.I)
ANSW = re.compile(r"Respondida\s+a\s+los\s+([0-9]+)\s+del\s+mismo", re.I)

def parse_day(tok):
    return int(tok) if tok.isdigit() else roman(tok)

def received(dorse, written):
    m = RECV.search(dorse)
    if not m or not written:
        return ""
    d = parse_day(m.group(1))
    g2 = (m.group(2) or "mismo").lower()
    mon = written.month if g2 == "mismo" else MONTHS.get(g2.rstrip(".e"), 0)
    if not mon or not d:
        return ""
    r = date(written.year, mon, d)
    return r.isoformat() if r > written else ""   # sanity: Lisbon/Paris letters cannot arrive the day written

def answered(dorse, written):
    m = ANSW.search(dorse)
    return date(written.year, written.month, int(m.group(1))).isoformat() if m and written else ""

def iso(s):
    return date.fromisoformat(s) if s else None

def dorse_from_index(row):
    """Return the part of the index notes that quotes a dorse ('dorse ...')."""
    txt = row.get("topic", "") or ""
    m = re.search(r"dorse[^'\"“]*['\"“]([^'\"”]+)['\"”]([^.;]*)", txt)
    return (m.group(1) + m.group(2)).strip() if m else ""

def main():
    idx = load_index()
    out, missing = [], []
    for d in DOCS:
        (did, v0, v1, dw, di, place, writer, addr, acls, kind, sp, lang, dv, zl, hol, note) = d
        for v in (v0, v1) + ((dv,) if dv else ()):
            if v not in idx:
                missing.append((did, v))
        folio = (idx.get(v0, {}).get("folio_right", "") or "").split(" ")[0]
        dsrc, dtxt = "", ""
        if did in IMAGE:
            dtxt = IMAGE[did]
            dsrc = "index:fixed" if dtxt.startswith("(index)") else "image"
        elif dv:
            dtxt = dorse_from_index(idx.get(dv, {}))
            dsrc = "index" if dtxt else "index:not-quoted"
        w = iso(di)
        rec = received(dtxt, w)
        ans = answered(dtxt, w)
        period = "undated" if not w else ("before-arrest" if w < ARREST else "after-arrest")
        out.append(dict(id=did, view=v0, views=f"{v0}-{v1}", folio=folio, date_written=dw, date_iso=di, period=period,
                        place=place, writer=writer, addressee=addr, addressee_class=acls, kind=kind, state_paper=sp,
                        language=lang, dorse_view=dv, dorse_source=dsrc, dorse_text=dtxt, received=rec, answered=ans,
                        zayas_link=zl, royal_holograph=hol, note=note))
    if missing:
        sys.exit(f"views not in index: {missing}")
    cols = list(out[0].keys())
    with open(os.path.join(HERE, "papers.tsv"), "w", encoding="utf-8", newline="") as f:
        wtr = csv.DictWriter(f, fieldnames=cols, delimiter="\t"); wtr.writeheader(); wtr.writerows(out)

    sp = [r for r in out if r["state_paper"] == "Y"]
    print(f"papers: {len(out)} rows; state papers (state_paper=Y): {len(sp)}")
    print("by addressee class (state papers):", dict(Counter(r["addressee_class"] for r in sp)))
    print("by writer (state papers, top):", Counter(r["writer"] for r in sp).most_common(8))
    zl = [r for r in sp if r["zayas_link"]]
    print(f"Zayas link (addressee/countersigned/certifies/named-as-handler): {len(zl)}/{len(sp)} = {len(zl)/len(sp):.0%};",
          dict(Counter(r["zayas_link"] for r in zl)))
    za = [r for r in sp if r["zayas_link"] in ("addressee", "countersigned", "certifies")]
    print(f"addressed to, countersigned or certified by Zayas: {len(za)}/{len(sp)} = {len(za)/len(sp):.0%}")
    print("\nby period (state papers):")
    for p in ("before-arrest", "after-arrest", "undated"):
        g = [r for r in sp if r["period"] == p]
        print(f"  {p}: n={len(g)} addressee={dict(Counter(r['addressee_class'] for r in g))} "
              f"kinds={dict(Counter(r['kind'] for r in g))} holograph={sum(r['royal_holograph']=='Y' for r in g)} "
              f"zayas_link={sum(bool(r['zayas_link']) for r in g)} with_received={sum(bool(r['received']) for r in g)}")
    print("\nlags (written -> received in Madrid -> next French dispatch in the volume):")
    for r in out:
        if r["received"] or r["answered"]:
            w, rc = iso(r["date_iso"]), iso(r["received"] or r["answered"])
            nxt = next((x for x in FRENCH_DISPATCHES if x >= rc), None)
            print(f"  {r['id']:14s} written {w} recv {r['received'] or '-'} answered {r['answered'] or '-'} "
                  f"transit {(rc-w).days}d; next dispatch {nxt} (+{(nxt-rc).days}d)")
    print("\nnot through the same hands (flags):")
    for r in out:
        if r["addressee_class"] == O and ("French" in r["note"] or "Paris" in r["note"]) or r["id"] in ("vargas-0824", "alava", "nuevas-0828"):
            print(f"  {r['id']}: {r['note']}")

if __name__ == "__main__":
    main()
