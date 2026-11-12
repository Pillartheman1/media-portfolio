# Builds the labeled placeholder assets/header.jpg (only until Daniel's real header image is dropped in).
from PIL import Image, ImageDraw, ImageFont
import math
W,H=1920,900
g=Image.new('RGB',(W,H)); px=g.load()
for y in range(H):
  t=min(1,y/H*1.6); base=[46+(32-46)*t,56+(33-56)*t,70+(35-70)*t]
  for x in range(W):
    glow=max(0,1-math.hypot(x-W*.85,y-H*.05)/900)**2.2
    px[x,y]=tuple(int(base[i]+(c-base[i])*glow) for i,c in enumerate((224,143,62)))
dr=ImageDraw.Draw(g)
mono=Image.open('assets/monogram.png'); s=220; cx,cy=W//2,320
m=mono.resize((s,s)); g.paste(m,(cx-s//2,cy-s//2),m)
f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',26)
t="HEADER IMAGE PLACEHOLDER  ·  replace assets/header.jpg"
w=dr.textlength(t,font=f); dr.text(((W-w)/2,cy+s//2+36),t,fill=(150,152,145),font=f)
g.save('assets/header.jpg',quality=88)
