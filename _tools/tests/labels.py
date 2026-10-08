import os
import sys;sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import *
import cv2,numpy as np,re
with sync_playwright() as p:
    srv=serve(8793)
    b,ctx=setup(p);pg=ctx.new_page()
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('http://127.0.0.1:8793/labels/');pg.wait_for_function("document.querySelectorAll('#catalog option').length>0")
    pg.click('#sample');pg.click('#match')
    n=pg.evaluate("document.querySelectorAll('#review tbody tr').length");um=pg.evaluate("document.querySelectorAll('#review tr.unmatched').length")
    print('rows',n,'unmatched',um)
    for t in ['large','sheet','sign']:pg.check(f'.ptype[value={t}]')
    pg.click('#build');pg.wait_for_timeout(500)
    print({c:pg.evaluate(f"document.querySelectorAll('.{c}').length") for c in ['p-small','p-large','p-sheet','p-sign']})
    # landscape
    css=pg.evaluate("[...document.styleSheets].flatMap(s=>{try{return [...s.cssRules].map(r=>r.cssText)}catch(e){return []}}).filter(t=>t.includes('@page')).join('|')")
    print('page css',css[:300])
    # QR decode
    svgs=pg.evaluate("[...document.querySelectorAll('#print-root svg')].map(s=>s.outerHTML)")
    d=cv2.QRCodeDetector();got=set()
    for i,sv in enumerate(svgs):
        if 'rect' not in sv and 'path' not in sv: continue
        pg.set_content(f'<body style="margin:0;background:#fff;padding:30px">{sv.replace("<svg","<svg width=300 height=300",1) if "width" not in sv[:80] else sv}</body>')
        png=pg.screenshot(clip={'x':0,'y':0,'width':400,'height':400})
        im=cv2.imdecode(np.frombuffer(png,np.uint8),1)
        v,_,_=d.detectAndDecode(im)
        if v:got.add(v)
        if i>40:break
    print(len(svgs),'svgs; decoded',sorted(got)[:20])
    items={e['slug'] for e in json.loads(DATA)['items']}
    badq=[u for u in got if not (u.startswith('https://freshwaterguides.com/care/') and u.split('/care/')[1].split('/')[0].split('?')[0] in items|{''})]
    print('bad qr',badq,'errs',errs)
