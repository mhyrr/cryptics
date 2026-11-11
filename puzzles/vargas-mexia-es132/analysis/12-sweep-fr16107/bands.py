import sys
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
# usage: bands.py view side(L|R) nbands [width]
v,side,n=sys.argv[1],sys.argv[2],int(sys.argv[3]); w=int(sys.argv[4]) if len(sys.argv)>4 else 1500
im=Image.open(f'full/v{v}.jpg'); W,H=im.size
x0,x1=(int(W*0.03),int(W*0.52)) if side=='L' else (int(W*0.48),int(W*0.97))
p=im.crop((x0,int(H*0.04),x1,int(H*0.97))); pw,ph=p.size
bh=ph/n; ov=bh*0.12
for i in range(n):
    b=p.crop((0,int(max(0,i*bh-ov)),pw,int(min(ph,(i+1)*bh+ov))))
    b=b.resize((w,int(b.size[1]*w/b.size[0])),Image.LANCZOS)
    b.save(f'feb7/v{v}{side}-{i+1}.jpg',quality=85)
print('ok')
