import os,sys;sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import *
with sync_playwright() as p:
    srv=serve(8795);b,ctx=setup(p);pg=ctx.new_page();errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('http://127.0.0.1:8795/care/compare/');pg.wait_for_function("document.querySelectorAll('#cmp-list option').length>100")
    def add(n):
        pg.fill('#cmp-q',n);pg.click('#cmp-add')
    add('Neon Tetra');add('Betta');t=pg.inner_text('#cmp-out');print(t[:300].replace('\n',' | '))
    assert 'Shared temperature range' in t
    add('Oscar');t=pg.inner_text('#cmp-out');print(t[:500].replace('\n',' | '))
    assert 'Check before' in t and 'Oscar' in t
    pg.goto('about:blank');pg.goto('http://127.0.0.1:8795/care/compare/#s=neon-tetra,cardinal-tetra');pg.wait_for_function("document.querySelectorAll('#cmp-chips li').length==2")
    print(pg.inner_text('#cmp-out')[:200].replace('\n',' | '))
    pg.set_viewport_size({'width':390,'height':800});print('overflow',pg.evaluate("document.documentElement.scrollWidth>390"))
    print('errs',errs)
