import os
import sys;sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import *
# (title, expected slug or None) -- expected None means must NOT match anything (supply) ; 'ANY' means unmatched or the slug ok
CASES=[
("Tank-Raised Neon Tetra (Paracheirodon innesi) - 1 in","neon-tetra"),
("Cardinal Tetra","cardinal-tetra"),
("Panda Cory Catfish","panda-corydoras"),
("Albino Cory Catfish","ANY"),
("Bristlenose Pleco","ANY"),
("Betta Fish Food Pellets",None),
("Betta Bow 2.5 LED Aquarium Kit",None),
("Fluval Betta Heater",None),
("Molly Fish Medication",None),
("Oscar Fish Food",None),
("Neon Tetra Flake Food",None),
("Goldfish Food Pellets 5 oz",None),
("Cichlid Pellets Sinking",None),
("Shrimp Food Mineral Bites",None),
("Java Fern on Bare Root","ANY"),
("Anubias Nana Potted","ANY"),
("Amazon Sword Tissue Culture","ANY"),
("Marimo Moss Ball","ANY"),
("Aquarium Gravel Black 5 lb",None),
("Java Moss Substrate Mat Decor",None),
("Fluval Plant Stratum Substrate",None),
("Betta Fish Male Halfmoon Blue","ANY"),
("Cherry Shrimp Red","ANY"),
("Nerite Snail Zebra","ANY"),
("Mystery Snail Gold","ANY"),
("Rummynose Tetra","ANY"),
("Harlequin Rasbora","ANY"),
("Kuhli Loach","ANY"),
("Clown Loach 3 in","ANY"),
("Oscar Tiger Fish","ANY"),
("Fancy Guppy Male Assorted","ANY"),
("Platy Fish Mickey Mouse","ANY"),
("Swordtail Red","ANY"),
("Molly Black","ANY"),
("Angelfish Koi","ANY"),
("Discus Red Turquoise 3 in","ANY"),
("Ram Cichlid German Blue","ANY"),
("African Dwarf Frog","african-dwarf-frog"),
("Ghost Shrimp","ghost-shrimp"),("Black Neon Tetra","black-neon-tetra"),("Green Neon Tetra","green-neon-tetra"),("Redtail Catfish","redtail-catfish"),("Sagittaria Platyphylla",None),
("Amano Shrimp","ANY"),
("Goldfish Comet","ANY"),
("Ryukin Goldfish","ANY"),
("Zebra Danio","ANY"),
("Tiger Barb","ANY"),
("Cherry Barb","ANY"),
("Pearl Gourami","ANY"),
("Dwarf Gourami Powder Blue","ANY"),
("Siamese Algae Eater","ANY"),
("Otocinclus Catfish","ANY"),

("Aquarium Water Conditioner Betta",None),
("Tetra Betta Flakes",None),
("Fish Net Large",None),
("Zoo Med Betta Log Hide",None),
("Neon Tetra Plush Toy",None),
]
with sync_playwright() as p:
    srv=serve(8791)
    b,ctx=setup(p);pg=ctx.new_page()
    pg.goto('http://127.0.0.1:8791/labels/');pg.wait_for_function("document.querySelectorAll('#catalog option').length>0")
    pg.fill('#list','\n'.join(c[0] for c in CASES));pg.click('#match')
    res=pg.evaluate("[...document.querySelectorAll('#review tbody tr')].map(tr=>[tr.children[0].textContent,tr._f.sel.selectedOptions[0].text,tr._f.sel.value])")
    items=json.loads(DATA)['items']
    bad=0
    for (t,exp),(raw,name,idx) in zip(CASES,res):
        idx=int(idx);slug=items[idx]['slug'] if idx>=0 else None
        ok = (slug is None) if exp is None else (slug==exp if exp!='ANY' else True)
        flag='' if ok else '  <-- BAD'
        if exp=='ANY' or not ok: print(f"{t!r:60} -> {name}{flag}")
        bad+= not ok
    print('BAD',bad)
