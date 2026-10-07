"""Original cartoon-style placeholder illustrations for care guides without a real photo.
Run before build_care.py. Output: care/art/<slug>.svg. Not photos; pages label them 'Illustration'."""
import os, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# slug: (shape, body, belly, mark, markcolor, fin)
S = {
 "cardinal-tetra":("tetra","#8fb5c9","#f3d9d0","stripe2","#2f8fe0","#d6453a"),
 "ember-tetra":("tetra","#f08a2c","#f6b36a","none","","#f6a24a"),
 "black-skirt-tetra":("deep","#9aa0a6","#c9cdd1","bands","#2a2d31","#2a2d31"),
 "lemon-tetra":("tetra","#f3e36a","#fbf3b0","none","","#f0c93a"),
 "rummy-nose-tetra":("tetra","#c9b9a5","#e6dccf","tailbars","#222","#e24a3a"),
 "congo-tetra":("tetra","#9a7fd0","#e8b36a","none","","#e3a24b"),
 "harlequin-rasbora":("tetra","#f0a27a","#f7c9b0","triangle","#2a2d3a","#f0a27a"),
 "chili-rasbora":("tiny","#e8452f","#f08a70","none","","#e8452f"),
 "white-cloud-mountain-minnow":("tetra","#9bb0a0","#e8efe6","stripe","#35b0c8","#e24a3a"),
 "cherry-barb":("tetra","#d0382f","#e9806f","stripe","#4a2a22","#e24a3a"),
 "boesemani-rainbowfish":("deep","#3f7fd0","#f08a2c","half","#f08a2c","#f0b03a"),
 "guppy":("guppy","#5aa7d8","#cfe6f3","spots","#f08a2c","#e8672f"),
 "endlers-livebearer":("guppy","#f08a2c","#f6c37a","spots","#2fb0c8","#35c0a0"),
 "platy":("deep","#f0702c","#f6a76a","none","","#f0702c"),
 "molly":("deep","#2a2d31","#55595e","none","","#2a2d31"),
 "swordtail":("tetra","#e8452f","#f08a70","stripe","#8a1f18","#e8452f"),
 "panda-corydoras":("cory","#f1ebe0","#fff8ee","panda","#2a2d31","#e8e0d0"),
 "bronze-corydoras":("cory","#9a7a4a","#d8c49a","none","","#8a6a3a"),
 "kuhli-loach":("eel","#d8a85a","#f0d9a8","bands","#4a2f1c","#c89a4a"),
 "clown-loach":("long","#f08a2c","#f6b36a","bands","#1f2226","#e24a3a"),
 "bristlenose-pleco":("pleco","#8a7a5a","#b8a98a","spots","#d8d0b8","#6f6248"),
 "otocinclus":("long","#a8a88a","#dcdcc4","stripe","#3a3a30","#a8a88a"),
 "siamese-algae-eater":("long","#c9b98a","#ece4c8","stripe","#2a2d31","#d8c898"),
 "dwarf-gourami":("deep","#2f9fd8","#e8613a","bands","#e8613a","#2f9fd8"),
 "honey-gourami":("deep","#f2b13a","#f8d27a","none","","#f2b13a"),
 "pearl-gourami":("deep","#a8967a","#e6d9c0","spots","#fff8e8","#b8a88a"),
 "blue-gourami":("deep","#4f8fd8","#9cc0ec","none","","#4f8fd8"),
 "bolivian-ram":("deep","#d8c07a","#f0e0a8","half","#2f8fd8","#e8672f"),
 "cockatoo-apistogramma":("deep","#e8b13a","#f6d77a","stripe","#2a2d31","#e8452f"),
 "angelfish":("angel","#d9d4c8","#f2efe6","bands","#2a2d31","#c9c4b8"),
 "oscar":("deep","#2f2f33","#4a4a50","spots","#e8672f","#2f2f33"),
 "convict-cichlid":("deep","#c8d0d8","#e8ecf0","bands","#2a2d31","#b8c0c8"),
 "electric-yellow-lab":("long","#f6d83a","#fbeb8a","stripe","#2a2d31","#f6d83a"),
 "kribensis":("long","#d8896a","#f0a07a","none","","#e8452f"),
 "jack-dempsey":("deep","#4a4f7a","#7a80b0","spots","#35c0e0","#4a4f7a"),
 "pea-puffer":("puffer","#9ac84a","#f3efc0","spots","#3a4a22","#9ac84a"),
 "silver-arowana":("arowana","#c9d3da","#eef2f5","none","","#aab6bf"),
 "neocaridina-shrimp":("shrimp","#e8452f","#f08a70","none","",""),
 "bucephalandra":("plant","#2f6a4a","#4f9a6a","none","",""),
}
def fish(shape, body, belly, mark, mc, fin):
    # canvas 400x400, fish faces right, centered
    W = {"tetra":(120,48),"deep":(105,78),"guppy":(95,42),"cory":(100,60),"eel":(170,16),"long":(135,34),"pleco":(120,48),"tiny":(85,30),"angel":(70,95),"puffer":(90,85),"arowana":(160,38)}[shape]
    rx, ry = W; cx, cy = 190, 215
    o = []
    # tail
    tx = cx - rx
    th = ry*0.9+8
    tail = {"guppy":f"M{tx+10},{cy} C{tx-60},{cy-70} {tx-70},{cy+70} {tx+10},{cy}Z",
            "eel":f"M{tx+10},{cy} L{tx-25},{cy-14} L{tx-25},{cy+14}Z"}.get(shape,
            f"M{tx+14},{cy} L{tx-48},{cy-th:.0f} Q{tx-30},{cy} {tx-48},{cy+th:.0f}Z")
    o.append(f'<path d="{tail}" fill="{fin}" opacity=".9"/>')
    if shape == "angel":
        o.append(f'<path d="M{cx-10},{cy-ry+8} L{cx+5},{cy-ry-70} L{cx+30},{cy-ry+14}Z" fill="{fin}"/><path d="M{cx-10},{cy+ry-8} L{cx+5},{cy+ry+70} L{cx+30},{cy+ry-14}Z" fill="{fin}"/>')
    elif shape == "arowana":
        o.append(f'<path d="M{cx-rx+20},{cy+ry-8} L{cx+rx-30},{cy+ry-6} L{cx+rx-60},{cy+ry+16}Z" fill="{fin}"/>')
    else:
        o.append(f'<path d="M{cx-20},{cy-ry+6} Q{cx+10},{cy-ry-36} {cx+40},{cy-ry+8}Z" fill="{fin}"/>')
    if shape == "pleco":
        o.append(f'<path d="M{cx-20},{cy-ry+6} Q{cx+10},{cy-ry-60} {cx+45},{cy-ry+8}Z" fill="{fin}"/>')
    o.append(f'<path d="M{cx-10},{cy+ry-8} Q{cx+10},{cy+ry+30} {cx+30},{cy+ry-8}Z" fill="{fin}" opacity=".85"/>')
    o.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{body}"/>')
    o.append(f'<clipPath id="b"><ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}"/></clipPath><g clip-path="url(#b)">')
    o.append(f'<ellipse cx="{cx+10}" cy="{cy+ry*0.65:.0f}" rx="{rx}" ry="{ry*0.6:.0f}" fill="{belly}" opacity=".75"/>')
    if mark == "stripe": o.append(f'<rect x="{cx-rx}" y="{cy-6}" width="{rx*2}" height="12" fill="{mc}"/>')
    if mark == "stripe2": o.append(f'<rect x="{cx-rx*0.2}" y="{cy-8}" width="{rx*1.3}" height="10" fill="{mc}"/>')
    if mark == "bands":
        for i in range(4): o.append(f'<rect x="{cx-rx*0.55+i*rx*0.42:.0f}" y="{cy-ry}" width="{max(8,rx*0.1):.0f}" height="{ry*2}" fill="{mc}"/>')
    if mark == "tailbars":
        for i in range(3): o.append(f'<rect x="{cx-rx+8+i*13}" y="{cy-ry}" width="7" height="{ry*2}" fill="{mc}"/>')
    if mark == "half": o.append(f'<rect x="{cx-rx}" y="{cy}" width="{rx*2}" height="{ry}" fill="{mc}" opacity=".85"/>')
    if mark == "panda":
        o.append(f'<circle cx="{cx+rx*0.55:.0f}" cy="{cy-6}" r="18" fill="{mc}"/><circle cx="{cx-rx*0.7:.0f}" cy="{cy-ry*0.45:.0f}" r="22" fill="{mc}"/><rect x="{cx-rx}" y="{cy-4}" width="26" height="10" fill="{mc}"/>')
    if mark == "triangle": o.append(f'<path d="M{cx},{cy-ry*0.5:.0f} L{cx-rx*0.9:.0f},{cy} L{cx},{cy+ry*0.6:.0f}Z" fill="{mc}"/>')
    if mark == "spots":
        for i,(dx,dy) in enumerate([(-.5,-.2),(-.2,.25),(.1,-.35),(.3,.2),(-.65,.3),(.5,-.1)]): o.append(f'<circle cx="{cx+dx*rx:.0f}" cy="{cy+dy*ry:.0f}" r="{7 if shape!="tiny" else 4}" fill="{mc}"/>')
    o.append('</g>')
    ex = cx + rx*0.62; ey = cy - ry*0.18
    o.append(f'<circle cx="{ex:.0f}" cy="{ey:.0f}" r="11" fill="#fff"/><circle cx="{ex+2:.0f}" cy="{ey:.0f}" r="6" fill="#10343b"/><circle cx="{ex+4:.0f}" cy="{ey-2:.0f}" r="2" fill="#fff"/>')
    o.append(f'<path d="M{cx+rx*0.82:.0f},{cy+ry*0.22:.0f} q10,6 18,-2" stroke="#10343b" stroke-width="3" fill="none" stroke-linecap="round" opacity=".6"/>')
    if shape == "cory":
        o.append(f'<path d="M{cx+rx-6},{cy+10} l22,10 M{cx+rx-6},{cy+16} l20,16" stroke="#10343b" stroke-width="2" opacity=".5"/>')
    return "".join(o)
def shrimp(c):
    return (f'<path d="M110,235 Q130,150 215,150 Q290,150 300,215 Q305,260 270,270 L255,250 Q270,215 235,200 Q170,185 150,250Z" fill="{c}"/>'
            '<path d="M110,235 L70,205 M110,240 L65,250 M118,246 L80,282" stroke="%s" stroke-width="5" stroke-linecap="round" fill="none"/>'
            '<circle cx="288" cy="196" r="9" fill="#fff"/><circle cx="290" cy="196" r="5" fill="#10343b"/>'
            '<path d="M300,190 Q345,150 372,118 M300,200 Q355,185 380,160" stroke="#10343b" stroke-width="2" fill="none" opacity=".6"/>'
            '<path d="M170,200 q-15,45 5,80 M200,200 q-8,45 12,78 M230,205 q0,40 15,66" stroke="%s" stroke-width="6" stroke-linecap="round" fill="none"/>') % (c, c)
def snail(c, c2):
    return (f'<path d="M110,300 Q120,268 170,268 L290,268 Q330,268 335,292 Q336,306 300,306 L120,306Z" fill="{c2}"/>'
            f'<path d="M318,272 q18,-34 30,-58 M328,276 q26,-24 46,-40" stroke="{c2}" stroke-width="6" stroke-linecap="round" fill="none"/>'
            '<circle cx="349" cy="214" r="6" fill="#10343b"/><circle cx="375" cy="236" r="6" fill="#10343b"/>'
            f'<circle cx="205" cy="225" r="70" fill="{c}"/><circle cx="205" cy="225" r="46" fill="none" stroke="#fff" stroke-opacity=".45" stroke-width="6"/><circle cx="205" cy="225" r="22" fill="none" stroke="#fff" stroke-opacity=".45" stroke-width="6"/>')
def crab(c, c2):
    return (f'<ellipse cx="200" cy="250" rx="82" ry="52" fill="{c}"/>'
            f'<path d="M130,230 q-50,-10 -52,-62 q30,10 40,30Z M270,230 q50,-10 52,-62 q-30,10 -40,30Z" fill="{c2}"/>'
            f'<path d="M122,262 l-52,24 M128,282 l-40,38 M278,262 l52,24 M272,282 l40,38" stroke="{c}" stroke-width="9" stroke-linecap="round"/>'
            '<circle cx="172" cy="208" r="10" fill="#fff"/><circle cx="228" cy="208" r="10" fill="#fff"/><circle cx="172" cy="208" r="5" fill="#10343b"/><circle cx="228" cy="208" r="5" fill="#10343b"/>')
def frog(c, c2):
    return (f'<ellipse cx="200" cy="270" rx="86" ry="56" fill="{c}"/><ellipse cx="200" cy="290" rx="60" ry="30" fill="{c2}"/>'
            f'<path d="M120,300 q-34,10 -48,44 q36,-4 62,-20Z M280,300 q34,10 48,44 q-36,-4 -62,-20Z" fill="{c}"/>'
            f'<circle cx="168" cy="220" r="20" fill="{c}"/><circle cx="232" cy="220" r="20" fill="{c}"/>'
            '<circle cx="168" cy="220" r="11" fill="#fff"/><circle cx="232" cy="220" r="11" fill="#fff"/><circle cx="170" cy="221" r="6" fill="#10343b"/><circle cx="234" cy="221" r="6" fill="#10343b"/>'
            '<path d="M170,268 q30,16 60,0" stroke="#10343b" stroke-width="3" fill="none" stroke-linecap="round" opacity=".6"/>')
def newt(c, c2):
    return (f'<path d="M80,300 C120,250 170,280 220,260 C270,240 300,240 330,210" stroke="{c}" stroke-width="46" stroke-linecap="round" fill="none"/>'
            f'<path d="M80,306 C120,262 170,290 220,272" stroke="{c2}" stroke-width="18" stroke-linecap="round" fill="none"/>'
            f'<path d="M290,238 l-12,38 M240,258 l-8,38 M150,276 l-14,34" stroke="{c}" stroke-width="12" stroke-linecap="round"/>'
            '<circle cx="338" cy="206" r="7" fill="#fff"/><circle cx="340" cy="206" r="4" fill="#10343b"/>')
def plant(c, c2):
    o=[]
    for i,(x,a) in enumerate([(150,-24),(185,-10),(215,6),(245,20),(170,-38),(230,34)]):
        o.append(f'<g transform="rotate({a} {x} 330)"><path d="M{x},330 C{x-48},250 {x-30},170 {x},130 C{x+30},170 {x+48},250 {x},330Z" fill="{c if i%2 else c2}"/><path d="M{x},325 L{x},150" stroke="#fff" stroke-width="2" opacity=".35"/></g>')
    o.append('<rect x="120" y="318" width="170" height="26" rx="8" fill="#6b5a46"/><path d="M135,332 h140" stroke="#8a7458" stroke-width="3"/>')
    return "".join(o)
def svg(slug, spec):
    shape, body, belly, mark, mc, fin = spec
    inner = frog(body, belly) if shape=="frog" else newt(body, belly) if shape=="newt" else snail(body, belly) if shape=="snail" else crab(body, belly) if shape=="crab" else shrimp(body) if shape=="shrimp" else plant(body, belly) if shape=="plant" else fish(*spec)
    bubbles = '<g fill="none" stroke="#fff" stroke-width="3" opacity=".7"><circle cx="330" cy="90" r="9"/><circle cx="350" cy="60" r="6"/><circle cx="318" cy="52" r="4"/></g>'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" role="img"><title>Illustration</title>'
            '<defs><linearGradient id="w" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#bfe9ee"/><stop offset="1" stop-color="#5fb4c4"/></linearGradient></defs>'
            '<rect width="400" height="400" fill="url(#w)"/>'
            '<path d="M0,372 Q60,350 120,372 T240,372 T400,360 V400 H0Z" fill="#d9c9a2"/>'
            '<path d="M30,372 q-10,-55 6,-90 M52,372 q10,-50 -4,-80" stroke="#3f9a6a" stroke-width="7" stroke-linecap="round" fill="none"/>'
            + bubbles + inner + '</svg>')
import sys, hashlib, colorsys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from care_data import ALL
SHAPE = {"Cichlidae":"deep","Loricariidae":"pleco","Callichthyidae":"cory","Cobitidae":"long","Botiidae":"long","Balitoridae":"long","Characidae":"tetra","Alestidae":"tetra","Danionidae":"tetra","Cyprinidae":"tetra","Tetraodontidae":"puffer","Osteoglossidae":"arowana","Osphronemidae":"deep","Poeciliidae":"guppy","Serrasalmidae":"deep","Mochokidae":"pleco","Pimelodidae":"long","Doradidae":"pleco","Notopteridae":"arowana","Polypteridae":"eel","Lepisosteidae":"arowana","Datnioididae":"deep","Aplocheilidae":"tetra","Melanotaeniidae":"tetra","Lebiasinidae":"tiny","Adrianichthyidae":"tiny","Gyrinocheilidae":"long","Mormyridae":"long","Aspredinidae":"pleco","Gasteropelecidae":"deep"}
def hexc(h, sat, val):
    r,g,b = colorsys.hsv_to_rgb(h, sat, val); return "#%02x%02x%02x" % (int(r*255),int(g*255),int(b*255))
def auto(e):
    hv = int(hashlib.md5(e["slug"].encode()).hexdigest()[:6], 16)
    h1 = (hv % 360) / 360.0
    marks = ["none","stripe","bands","spots","half","stripe2"]
    mk = marks[(hv >> 9) % len(marks)]
    if e["kind"] == "plant":
        return ("plant", hexc(0.30+((hv>>3)%12)/100, .62, .50), hexc(0.27+((hv>>5)%10)/100, .55, .62), "none", "", "")
    if e["kind"] == "amphibian":
        return (("newt" if "newt" in e["name"].lower() else "frog"), ("#e8602c" if "fire" in e["name"].lower() else hexc(0.28+(hv%8)/100, .55, .62)), "#f6b13a" if "fire" in e["name"].lower() else hexc(0.2, .3, .92), "none", "", "")
    if e["kind"] == "invert":
        nm = e["name"].lower()
        shp = "snail" if "snail" in nm else "crab" if "crab" in nm or "crayfish" in nm else "shrimp"
        return (shp, hexc(h1, .7, .85), hexc(h1, .4, .95), "none", "", "")
    shape = SHAPE.get(e["family"], "tetra")
    return (shape, hexc(h1, .55, .80), hexc(h1, .20, .97), mk, hexc((h1+.5)%1, .6, .30), hexc((h1+.08)%1, .65, .85))
for e in ALL:
    if e["slug"] not in S:
        S[e["slug"]] = auto(e)
os.makedirs(os.path.join(ROOT,"care/art"), exist_ok=True)
for slug, spec in S.items():
    open(os.path.join(ROOT,f"care/art/{slug}.svg"),"w").write(svg(slug,spec))
json.dump(sorted(S), open(os.path.join(ROOT,"care/art/index.json"),"w"))
print("wrote", len(S))
