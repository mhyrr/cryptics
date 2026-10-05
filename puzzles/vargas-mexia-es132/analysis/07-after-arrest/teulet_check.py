"""External check (README criterion 6, exp 07 step 6): the Simancas minute of the King's reply on the Scottish matter,
printed by Teulet vol. 5 (1862) pp. 213-214 (archive.org relationspolitiq05teul_0, leaves n238-n239, read on the page
images 2026-10-05; Teulet dates it "Février", B. 51 n. 69, "minute annexée à la dépêche précédente" of 21 Feb 1580).
Cabinet-noir reports it as the minute of f. 255/261 (28 Mar 1580). Scored with exp 06's in-order letter match
(mignet_check.norm/best). Pass >= 75% (as in exp 06). Controls: decodes of other letters.
    python3 teulet_check.py f255_dec.txt f261_dec.txt [controls ...]"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "06-premurder"))
from mignet_check import decoded_text, best  # noqa: E402

PASSAGES = {
    "t213": "En lo que ha tratado el embaxador de Escocia de parte de su Reyna y sobre la salida de su Rey, le puede "
            "assegurar muy de veras que Su Majestad le tiene la misma buena voluntad que siempre ha podido conoscer, "
            "y que acudira a sus cosas y las favorescera con mucho amor, y recibira y acogera con el mismo al dicho "
            "Rey, ora sea en España (que seria lo mejor), o en qualquier otro de sus Estados, haziendole el mismo "
            "tratamiento que si le fuesse hijo proprio.",
    "t213b": "Pero, para que todo esto se pueda mejor effectuar, conviene que la misma Reyna piense bien los medios "
             "para executallo, y que se sepan dar maña a poner en execucion lo de la salida una vez, assegurandoles "
             "del secreto desta parte, y que St Goart ni hombre del mundo no lo podra entender.",
    "t214": "Que es todo lo que agora se puede hazer de parte de Su Majestad; y abraçar despues la causa y asistilla y "
            "favorescella, pues si antes de tiempo se oliesse algo desto, seria estragar el negocio y impossibilitallo; "
            "finalmente que el los esfuerce de parte de Su Majestad, y conserve y promueva la platica, y vaya avisando "
            "lo que uviere, y procure que se fabrique sobre buen fondamento y no se tome a la ligera ni con liviandad.",
}

for path in sys.argv[1:]:
    text = decoded_text(path)
    print(f"# {path} ({len(text)} normalised letters)")
    for k, v in PASSAGES.items():
        r, at = best(v, text)
        print(f"{k:6s} {r:.0%}  at char {at}")
