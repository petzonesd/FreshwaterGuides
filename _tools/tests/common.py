import os
import json,subprocess,time,threading,http.server,socketserver,functools,os
from playwright.sync_api import sync_playwright
ROOT=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA=open(ROOT+'/care/data.json').read()
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a):pass
def serve(port):
    h=functools.partial(Q,directory=ROOT)
    socketserver.TCPServer.allow_reuse_address=True
    s=socketserver.TCPServer(('127.0.0.1',port),h)
    threading.Thread(target=s.serve_forever,daemon=True).start();return s
def setup(p,vp=None):
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium',args=['--no-sandbox'])
    ctx=b.new_context(viewport=vp or {'width':1200,'height':900})
    def route(r):
        u=r.request.url
        if u.startswith('https://freshwaterguides.com/care/data.json'):r.fulfill(body=DATA,content_type='application/json')
        elif 'bigcommerce' in u or u.startswith('https://fonts.'):r.abort()
        else:r.continue_()
    ctx.route('**/*',route)
    return b,ctx
