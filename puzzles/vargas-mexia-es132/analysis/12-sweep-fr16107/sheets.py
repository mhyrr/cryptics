"""Contact sheets: N spreads per sheet, labelled with view number.
Usage: uv run --with pillow python3 sheets.py FIRST LAST PER COLS WIDTH OUTDIR"""
import sys
from PIL import Image, ImageDraw
a, b, per, cols, W, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
for s in range(a, b+1, per):
    vs = list(range(s, min(s+per, b+1))); rows = -(-len(vs)//cols); H = int(W*.71)
    sheet = Image.new("L", (cols*W, rows*H), 255); d = ImageDraw.Draw(sheet)
    for k, v in enumerate(vs):
        im = Image.open(f"../../sources/cache/fr16107/v{v}.jpg").convert("L").resize((W, H))
        x, y = (k % cols)*W, (k//cols)*H; sheet.paste(im, (x, y))
        d.rectangle((x, y, x+44, y+22), fill=0); d.text((x+4, y+5), f"v{v}", fill=255)
    sheet.save(f"{out}/sheet_{s:03d}.jpg", quality=80)
