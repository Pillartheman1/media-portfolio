import sys
from playwright.sync_api import sync_playwright
base=sys.argv[1]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--headless=new'])
    pg=b.new_page(viewport={'width':1440,'height':900})
    for path,out in [('index.html','landing'),('daniel/','daniel-home'),('media-co/','media-co-home'),('daniel/projects/color-01.html','daniel-project-color-01')]:
        pg.goto(base+path,wait_until='networkidle'); pg.wait_for_timeout(800)
        pg.screenshot(path=f'screenshots/{out}-1440.png',full_page=True)
    b.close()
