import os
import sys;sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import *
SHOW=["Neon Tetra","Tank-Raised Neon Tetra (Paracheirodon innesi) - 1 in","Java Fern on Bare Root","Panda Cory Catfish","Black Neon Tetra","Ghost Shrimp","Redtail Catfish"]
HIDE=["Betta Fish Food Pellets","Betta Bow 2.5 LED Aquarium Kit","Fluval Betta Heater","Molly Fish Medication","Oscar Fish Food","Neon Tetra Flake Food","Green Neon Tetra Plush","Shrimp Food Mineral Bites","Goldfish Food Pellets","Java Moss Substrate Mat Decor","Aquarium Water Conditioner Betta"]
with sync_playwright() as p:
    srv=serve(8792)
    b,ctx=setup(p)
    # embed script pulls data from BASE; route handles data.json. care.js itself loaded locally.
    pg=ctx.new_page()
    pg.route('https://freshwaterguides.com/embed/care.js',lambda r:r.fulfill(body=open(ROOT+'/embed/care.js').read(),content_type='text/javascript'))
    bad=0
    for t in SHOW+HIDE:
        pg.set_content(f'<h1 id="t">{t}</h1><div id="host" data-fwg-care="auto" data-title="#t"></div><script src="https://freshwaterguides.com/embed/care.js"></script>')
        pg.wait_for_timeout(300)
        shown=pg.evaluate("(()=>{const h=document.getElementById('host');return h.style.display!=='none'&&!!h.querySelector('.fwg-care')})()")
        ok= shown if t in SHOW else not shown
        if not ok: bad+=1;print('BAD',t,shown)
    print('embed BAD',bad)
