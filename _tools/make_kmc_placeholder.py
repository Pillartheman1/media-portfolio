# Builds PLACEHOLDER Klabunde Media Co. assets until Daniel's real files are on the box:
#   assets/kmc-logo.png  (wide white wordmark on transparent; replace with the real white wordmark, same name)
#   assets/kmc-hero.jpg  (16:9 navy background; replace with the real navy bokeh wordmark image, same name)
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
CG='/usr/share/fonts/truetype/sand-box/google/Cormorant Garamond/CormorantGaramond-VariableFont_wght.ttf'
SANS='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
W=(239,240,235,255)
def wordmark(w=1200,h=360,label=True):
  im=Image.new('RGBA',(w,h),(0,0,0,0)); d=ImageDraw.Draw(im)
  # brackets
  for x0,dx in ((20,1),(w-21,-1)):
    d.line((x0,20,x0,h-21),fill=W,width=5); d.line((x0,20,x0+dx*60,20),fill=W,width=5); d.line((x0,h-21,x0+dx*60,h-21),fill=W,width=5)
  f=ImageFont.truetype(SANS,120); t="KLABUNDE"; tw=d.textlength(t,font=f); d.text(((w-tw)/2,60),t,font=f,fill=W)
  f2=ImageFont.truetype(SANS,46); t2="M E D I A   C O M P A N Y"; tw=d.textlength(t2,font=f2); d.text(((w-tw)/2,205),t2,font=f2,fill=W)
  if label:
    f3=ImageFont.truetype(SANS,28); t3="PLACEHOLDER LOGO"; tw=d.textlength(t3,font=f3); d.text(((w-tw)/2,282),t3,font=f3,fill=(120,170,200,255))
  return im
wordmark().save('assets/kmc-logo.png')
# navy hero
random.seed(4); H=Image.new('RGB',(1920,1080),(14,22,38)); d=ImageDraw.Draw(H)
for i in range(70):
  x,y,r=random.randint(0,1920),random.randint(0,1080),random.randint(30,140)
  c=random.choice([(40,70,110),(30,90,120),(60,100,150),(25,50,90)])
  d.ellipse((x-r,y-r,x+r,y+r),fill=c)
H=H.filter(ImageFilter.GaussianBlur(40))
wm=wordmark(900,270,False); H.paste(wm,(510,370),wm)
f=ImageFont.truetype(SANS,26); d=ImageDraw.Draw(H); t="BACKGROUND PLACEHOLDER  ·  replace assets/kmc-hero.jpg"; tw=d.textlength(t,font=f); d.text(((1920-tw)/2,300),t,font=f,fill=(150,170,190))
H.save('assets/kmc-hero.jpg',quality=86)
