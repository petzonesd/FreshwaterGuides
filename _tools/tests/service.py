import os
import sys;sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import *
import datetime
fails=[]
def chk(c,m):
    if not c:fails.append(m);print('FAIL',m)
with sync_playwright() as p:
    srv=serve(8794)
    b,ctx=setup(p);ctx.grant_permissions(['clipboard-read','clipboard-write'],origin='http://127.0.0.1:8794')
    pg=ctx.new_page();errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.on('dialog',lambda d:d.accept())
    pg.goto('http://127.0.0.1:8794/service/')
    tab=lambda n:pg.click(f'#tabs button:has-text("{n}")')
    tab('Settings');pg.get_by_label('Business name').fill('Test Aquatics');pg.get_by_label('Business name').blur()
    pg.get_by_label('Default tax rate (%)').fill('8');pg.get_by_label('Default tax rate (%)').blur()
    tab('Clients and tanks');pg.click('text=+ Add client');pg.get_by_label('Name',exact=True).first.fill('Smith');pg.get_by_label('Name',exact=True).first.blur()
    pg.click('text=+ Add tank');pg.wait_for_timeout(200)
    tab('Dashboard');
    txt=pg.inner_text('#app');chk('Never done' in txt,'dash due tasks')
    n0=pg.locator('text=Done today').count();pg.locator('button:has-text("Done today")').first.click();
    chk(pg.locator('button:has-text("Done today")').count()==n0-1,'Done today removes task')
    # recurring
    tab('Clients and tanks');pg.click('button.sitem:has-text("Smith")');pg.check('text=Bill this client on a schedule >> input') if False else pg.locator('label.scheck input').check()
    today=datetime.date.today().isoformat()
    pg.get_by_label('Amount ($)').fill('50');pg.get_by_label('Amount ($)').blur()
    tab('Dashboard');chk('Recurring invoices ready (1)' in pg.inner_text('#app'),'recurring due')
    pg.click('button:has-text("Create invoice")');pg.wait_for_timeout(300)
    st=json.loads(pg.evaluate("localStorage.getItem('fwg-service-v1')"))
    nxt=st['clients'][0]['rec']['next'];d=datetime.date.today()
    exp_m=(d.month%12)+1
    chk(int(nxt.split('-')[1])==exp_m,f'recurring advanced one month {nxt}')
    chk(len(st['invoices'])==1,'invoice created')
    # visit + share
    tab('Visit report');pg.click('button:has-text("Save only")');pg.wait_for_timeout(200)
    st=json.loads(pg.evaluate("localStorage.getItem('fwg-service-v1')"));chk(len(st['visits'])==1,'visit saved')
    # share link render
    payload=pg.evaluate("""async()=>{ const s=JSON.parse(localStorage.getItem('fwg-service-v1')); return await FWGShare.link({k:'visit',...s.visits[0]}) }""")
    print('link',payload[:70])
    v=ctx.new_page();v.on('pageerror',lambda e:errs.append('view:'+str(e)));v.goto(payload);v.wait_for_timeout(800)
    print('view text:',v.inner_text('body')[:160].replace('\n',' '))
    # persists
    pg.reload();pg.wait_for_timeout(300);tab('Clients and tanks');chk('Smith' in pg.inner_text('#app'),'persist after reload')
    # backup/restore
    tab('Settings')
    with pg.expect_download() as dl:pg.click('button:has-text("Download backup")')
    path=dl.value.path();bk=json.load(open(path));chk(len(bk['clients'])==1,'backup content')
    pg.click('button:has-text("Erase everything")');pg.wait_for_timeout(200)
    chk(json.loads(pg.evaluate("localStorage.getItem('fwg-service-v1')"))['clients']==[],'erased')
    pg.set_input_files('#imp',path);pg.wait_for_timeout(300)
    chk(len(json.loads(pg.evaluate("localStorage.getItem('fwg-service-v1')"))['clients'])==1,'restored')
    print('errs',errs,'fails',fails)
