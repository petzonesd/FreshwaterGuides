import os
import re,json,os,sys,glob
from html.parser import HTMLParser
root='.'
sm=open('sitemap.xml').read()
smurls=set(re.findall(r'<loc>https://freshwaterguides.com(/[^<]*)</loc>',sm))
probs=[]
class P(HTMLParser):
    def __init__(s):
        super().__init__();s.h1=0;s.title='';s.in_t=False;s.desc='';s.links=[];s.ld=[];s.in_ld=False;s.canon=None
    def handle_starttag(s,t,a):
        a=dict(a)
        if t=='h1':s.h1+=1
        if t=='title':s.in_t=True
        if t=='meta' and a.get('name')=='description':s.desc=a.get('content','')
        if t=='link' and a.get('rel')=='canonical':s.canon=a.get('href')
        if t in('a','link') and a.get('href'):s.links.append(a['href'])
        if t in('img','script','source') and a.get('src'):s.links.append(a['src'])
        if t=='script' and a.get('type')=='application/ld+json':s.in_ld=True;s.ld.append('')
    def handle_endtag(s,t):
        if t=='title':s.in_t=False
        if t=='script':s.in_ld=False
    def handle_data(s,d):
        if s.in_t:s.title+=d
        if s.in_ld:s.ld[-1]+=d
for f in glob.glob('**/index.html',recursive=True):
    if f.startswith('_'):continue
    p=P();p.feed(open(f).read())
    url='/'+f[:-10] if f!='index.html' else '/'
    if p.h1!=1:probs.append((f,'h1',p.h1))
    if len(p.title.strip())>60:probs.append((f,'title',len(p.title.strip())))
    if len(p.desc)>160:probs.append((f,'desc',len(p.desc)))
    if not p.desc:probs.append((f,'nodesc'))
    for j in p.ld:
        try:json.loads(j)
        except Exception as e:probs.append((f,'jsonld',str(e)[:50]))
    if url not in smurls and not f.startswith('service/view'):probs.append((f,'notinsitemap'))
    for l in p.links:
        if re.match(r'(https?:|mailto:|tel:|#|data:|javascript:)',l):
            if l.startswith('https://freshwaterguides.com/'):l=l[len('https://freshwaterguides.com'):]
            else:continue
        l=l.split('#')[0].split('?')[0]
        if not l:continue
        t=os.path.normpath(os.path.join(os.path.dirname(f),l)) if not l.startswith('/') else (l[1:] or '.')
        if os.path.isdir(t):t=os.path.join(t,'index.html')
        if not os.path.exists(t):probs.append((f,'broken',l))
from collections import Counter
print(Counter(p[1] for p in probs))
for p in probs[:40]:print(p)
