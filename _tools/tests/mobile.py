import os
import sys;sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import *
with sync_playwright() as p:
    srv=serve(8795)
    b,ctx=setup(p,{'width':390,'height':800})
    for u in ['/care/','/care/neon-tetra/','/care/tetras/','/labels/','/service/','/embed/']:
        pg=ctx.new_page();pg.goto('http://127.0.0.1:8795'+u);pg.wait_for_timeout(500)
        w=pg.evaluate("[document.documentElement.scrollWidth,document.documentElement.clientWidth]")
        wide=pg.evaluate("[...document.querySelectorAll('body *')].filter(e=>e.getBoundingClientRect().right>392&&!e.closest('pre,.lab-table-wrap,.stbl-wrap,table')).slice(0,3).map(e=>e.tagName+'.'+e.className)")
        print(u,w,wide);pg.close()
