#!/usr/bin/env python3
"""Turn Daniel's real Klabunde Media Co. files into site assets (replaces the placeholders).
Usage: python3 _tools/import_kmc_assets.py HERO_16x9.png WORDMARK_BLACK_ON_WHITE.png [VERTICAL_9x16.png]
 - HERO -> assets/kmc-hero.jpg (media-co hero + landing panel background)
 - WORDMARK -> assets/kmc-logo.png (inverted to white, alpha from luminance, trimmed)
 - VERTICAL -> assets/kmc-vertical.jpg (optional alternate background)
Then re-sample the navy/teal accent and update body.side-media-co in assets/style.css."""
import sys
from PIL import Image, ImageOps
hero, wm = sys.argv[1], sys.argv[2]
im = Image.open(hero).convert('RGB'); im.thumbnail((2400, 2400)); im.save('assets/kmc-hero.jpg', quality=88)
g = ImageOps.grayscale(Image.open(wm).convert('RGB'))
a = ImageOps.invert(g).point(lambda v: 0 if v < 16 else v)
out = Image.new('RGBA', g.size, (239, 240, 235, 0)); out.putalpha(a)
out = out.crop(out.getbbox()); out.thumbnail((1400, 1400)); out.save('assets/kmc-logo.png')
if len(sys.argv) > 3:
    v = Image.open(sys.argv[3]).convert('RGB'); v.thumbnail((1600, 1600)); v.save('assets/kmc-vertical.jpg', quality=88)
print('done')
