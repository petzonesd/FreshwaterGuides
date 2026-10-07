#!/usr/bin/env python3
"""Generate /care/ pages, /care/data.json, sitemap + llms.txt entries from care_data.py.
Run from repo root:  python3 _tools/build_care.py
Idempotent. Safe to re-run after editing care_data.py."""
import json, os, re, html, sys
sys.path.insert(0, os.path.dirname(__file__))
from care_data import ALL

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://freshwaterguides.com"
TODAY = "2026-10-07"
E = html.escape

STORES = [
    dict(id="convoy", name="Pet Zone Convoy", addr="4160 Convoy St, San Diego, CA 92111", phone="(858) 987-0309", tel="+18589870309",
         hours="Open daily, 10am-6pm", focus="Aquascaping, planted tanks"),
    dict(id="midcity", name="Pet Zone Mid-City", addr="4266 University Ave, San Diego, CA 92105", phone="(619) 283-1812", tel="+16192831812",
         hours="Closed Monday; Tue-Fri 10:30am-6pm, Sat 11am-6pm, Sun 11am-4pm", focus="Monster fish, koi"),
]

def rng(t, unit=""):
    lo, hi = t
    f = lambda v: ("%g" % v)
    return f"{f(lo)}-{f(hi)}{unit}"

def tap_fit(e):
    lo, hi = e["ph"] if isinstance(e["ph"], tuple) else tuple(float(x) for x in e["ph"].split("-"))
    if lo >= 7.0:
        return "Naturally suited to San Diego's hard, alkaline tap water once it is dechlorinated (the city uses chloramine, so use a conditioner that handles it)."
    if hi >= 7.8:
        return "Tolerates San Diego's hard, alkaline tap water (pH roughly 7.6-8.6) with slow acclimation and a conditioner that handles chloramine."
    if hi >= 7.5:
        return "Captive-bred stock usually adapts to San Diego tap water with slow acclimation. For best color and health, many keepers blend tap with RO/DI water."
    return "Prefers softer, more acidic water than San Diego's tap (pH roughly 7.6-8.6, hard). Most keepers blend tap with RO/DI water or use a remineralized RO/DI supply."

def ph_s(e):
    p = e["ph"]
    return p if isinstance(p, str) else "%.1f-%.1f" % p

def temp_s(e):
    t = e["temp"]
    return t if isinstance(t, str) else rng(t, "°F")

def facts_rows(e):
    k = e["kind"]
    if k == "plant":
        rows = [("Scientific name", e["sci"]), ("Family", e["family"]), ("Origin", e["origin"]), ("Height", e["height"]),
                ("Light", e["light"]), ("CO2", e["co2"]), ("Placement", e["placement"]), ("Growth rate", e["growth"]),
                ("Temperature", temp_s(e)), ("pH", ph_s(e)), ("Difficulty", e["difficulty"]), ("Propagation", e["propagation"])]
    else:
        rows = [("Scientific name", e["sci"]), ("Family", e["family"]), ("Origin", e["origin"]), ("Adult size", e["size"]),
                ("Minimum tank", f"{e['tank']} gallons"), ("Temperature", temp_s(e)), ("pH", ph_s(e)),
                ("Temperament", e["temperament"]), ("Social behavior", e["social"]), ("Swim level", e["level"]),
                ("Difficulty", e["difficulty"]), ("Diet", e["diet"]), ("Typical lifespan", e["life"])]
    return rows

def title_for(e):
    for t in (f"{e['name']} Care: Tank Size, Temperature, pH", f"{e['name']} Care Guide and Facts", f"{e['name']} Care"):
        if len(t) <= 60:
            return t
    return e["name"]

def desc_for(e):
    if e["kind"] == "plant":
        d = f"{e['name']} ({e['sci']}) care: {e['light'].lower()} light, {e['placement'].lower()}, {e['height']} tall, {temp_s(e)}, pH {ph_s(e)}. {e['difficulty']} difficulty."
    else:
        d = f"{e['name']} ({e['sci']}) care: grows to {e['size']}, minimum {e['tank']} gallons, {temp_s(e)}, pH {ph_s(e)}. {e['temperament']}."
    if len(d) > 158:
        d = d[:155].rsplit(" ", 1)[0] + "..."
    return d

HEAD_NAV = """<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
<div class="container nav">
<a class="brand" href="/" aria-label="Freshwater Guides home"><span class="brand-mark">◒</span><span>Freshwater<br><strong>Guides</strong></span></a>
<nav aria-label="Main navigation">
<a href="/#start">Start Here</a><a href="/#topics">Topics</a><a href="/#guides">Guides</a><a href="/care/">Care Guides</a><a href="/glossary/">Glossary</a><a href="/#about">About</a>
</nav>
</div>
</header>
"""

def footer_html():
    # reuse the live footer from an existing page so the sitewide sibling row stays in sync
    src = open(os.path.join(ROOT, "san-diego/tap-water/index.html"), encoding="utf-8").read()
    m = re.search(r'<footer class="site-footer">.*?</footer>', src, re.S)
    return m.group(0)

def head(title, desc, path, extra_ld=""):
    url = f"{BASE}{path}"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{E(desc)}">
<meta name="theme-color" content="#0b3f4a">
<title>{E(title)}</title>
<link rel="canonical" href="{url}">
<link rel="stylesheet" href="/styles.css">
<link rel="stylesheet" href="/care/care.css?v=2">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="article">
<meta name="twitter:card" content="summary">
{extra_ld}
</head>
<body>
"""

def store_block():
    cards = []
    for s in STORES:
        cards.append(f"""<div class="store-card" id="store-{s['id']}"><strong>{E(s['name'])}</strong>
<p>{E(s['addr'])}<br><a href="tel:{s['tel']}">{E(s['phone'])}</a><br>{E(s['hours'])}</p><p class="store-focus">{E(s['focus'])}</p></div>""")
    return f"""<section class="store-block" aria-labelledby="find-us">
<h2 id="find-us">Find it at Pet Zone</h2>
<p>Pet Zone Tropical Fish is a San Diego aquarium store with two locations. Stock changes daily, so call ahead if you are after a specific species or plant. Shop online at <a href="https://www.petzonesd.com/">petzonesd.com</a>.</p>
<div class="store-cards">{''.join(cards)}</div>
</section>"""

PH = json.load(open(os.path.join(ROOT, "care/photos.json")))

def photo_url(slug, size="800x800"):
    path = PH["items"].get(slug)
    return PH["base"].format(size=size, path=path) if path else None

def page_for(e, by_slug):
    path = f"/care/{e['slug']}/"
    title, desc = title_for(e), desc_for(e)
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc,
          "author": {"@type": "Organization", "name": "Pet Zone SD Team"},
          "publisher": {"@type": "Organization", "name": "Freshwater Guides", "url": BASE + "/"},
          "datePublished": TODAY, "dateModified": TODAY, "mainEntityOfPage": BASE + path}
    if photo_url(e["slug"]):
        ld["image"] = [photo_url(e["slug"])]
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Care Guides", "item": BASE + "/care/"},
        {"@type": "ListItem", "position": 3, "name": e["name"], "item": BASE + path}]}
    extra = (f'<script type="application/ld+json">{json.dumps(ld)}</script>\n'
             f'<script type="application/ld+json">{json.dumps(bc)}</script>')
    out = [head(title, desc, path, extra), HEAD_NAV, '<main id="main">\n<div class="container narrow article">']
    out.append(f'<p class="breadcrumb"><a href="/">Home</a> / <a href="/care/">Care Guides</a> / {E(e["name"])}</p>')
    out.append(f'<h1>{E(e["name"])} Care Guide</h1>')
    out.append('<p class="byline">By Pet Zone SD Team · Updated October 7, 2026 · 2 min read</p>')
    ph = photo_url(e["slug"])
    if ph:
        out.append(f'<figure class="care-photo"><img src="{ph}" alt="{E(e["name"])} at Pet Zone Tropical Fish in San Diego" width="400" height="400" loading="eager" onerror="this.parentNode.remove()"><figcaption>Photo: {E(PH["credit"])}</figcaption></figure>')
    out.append('<div class="article-body care-body">')
    if e["kind"] == "plant":
        lead = f"<strong>{E(e['name'])} ({E(e['sci'])}) is a {E(e['difficulty'].lower())}-level aquarium plant.</strong> {E(e['note'])}"
    else:
        lead = f"<strong>{E(e['name'])} ({E(e['sci'])}) is a {E(e['difficulty'].lower())}-level {'freshwater fish' if e['kind']=='fish' else 'freshwater invertebrate'} that needs at least {e['tank']} gallons and {E(temp_s(e))}.</strong> {E(e['note'])}"
    out.append(f"<p>{lead}</p>")
    out.append('<h2>Care facts at a glance</h2>')
    rows = "".join(f"<tr><th scope=\"row\">{E(k)}</th><td>{E(v)}</td></tr>" for k, v in facts_rows(e))
    out.append(f'<table class="care-facts"><tbody>{rows}</tbody></table>')
    out.append('<h2>Quick tips</h2><ul>' + "".join(f"<li>{E(t)}</li>" for t in e["tips"]) + "</ul>")
    out.append('<h2>San Diego water</h2>')
    out.append(f"<p>{E(tap_fit(e))} Learn the numbers in our <a href=\"/san-diego/tap-water/\">San Diego tap water guide</a>.</p>")
    if e["kind"] == "plant":
        out.append('<p>New to planted tanks? Start with <a href="/aquascaping/beginner-planted-tank/">our beginner planted tank guide</a> and the <a href="/guides/aquarium-plant-fertilizing/">plant fertilizer guide</a>.</p>')
    else:
        out.append('<h2>Before you buy</h2>')
        out.append('<p>Make sure your tank is cycled (<a href="/guides/cycle-a-fish-tank/">how to cycle a tank</a>), check your numbers with the <a href="/guides/water-parameters-testing/">water testing guide</a>, and use the <a href="/guides/freshwater-fish-compatibility/">compatibility guide</a> to check tankmates. These are general ranges; individual fish and local water vary.</p>')
    out.append(store_block())
    rel = [x for x in by_slug.values() if x["slug"] != e["slug"] and x["family"] == e["family"]]
    rel += [x for x in by_slug.values() if x["slug"] != e["slug"] and x["kind"] == e["kind"] and x not in rel]
    rel = rel[:5]
    out.append('<div class="related"><h3>More care guides</h3><ul>' + "".join(f'<li><a href="/care/{x["slug"]}/">{E(x["name"])} care</a></li>' for x in rel) + '<li><a href="/labels/">Print care labels for your tank</a></li></ul></div>')
    out.append('</div>')
    out.append('<div class="author-box"><strong>Pet Zone SD Team</strong> — Freshwater Guides is written and reviewed by the team behind Pet Zone Tropical Fish, a San Diego aquarium retailer, drawing on hands-on retail and keeping experience.</div>')
    out.append('</div>\n</main>')
    out.append(footer_html())
    out.append('<script src="/care/store.js" defer></script>\n</body>\n</html>\n')
    return "\n".join(out)

def index_page(by_slug):
    title = "Freshwater Fish, Shrimp and Plant Care Guides"
    desc = "Quick care facts for common freshwater fish, shrimp, snails and aquarium plants: tank size, temperature, pH, temperament and difficulty."
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": title, "description": desc,
          "url": BASE + "/care/", "publisher": {"@type": "Organization", "name": "Freshwater Guides", "url": BASE + "/"},
          "mainEntity": {"@type": "ItemList", "itemListElement": [
              {"@type": "ListItem", "position": i + 1, "url": f"{BASE}/care/{e['slug']}/", "name": e["name"]} for i, e in enumerate(by_slug.values())]}}
    out = [head(title, desc, "/care/", f'<script type="application/ld+json">{json.dumps(ld)}</script>'), HEAD_NAV,
           '<main id="main">\n<div class="container article care-index">',
           '<p class="breadcrumb"><a href="/">Home</a> / Care Guides</p>',
           '<h1>Aquarium Care Guides</h1>',
           f'<p class="byline">By Pet Zone SD Team · Updated October 7, 2026 · {len(by_slug)} guides</p>',
           '<p class="lede-line"><strong>Quick, honest care facts for the fish, shrimp, snails and plants we see most at Pet Zone.</strong> Each guide gives tank size, temperature, pH, temperament and difficulty, plus how the species fits San Diego tap water. Scan the QR code on any Pet Zone tank label to land on the matching guide.</p>',
           '<label class="care-search"><span>Search the guides</span><input id="care-q" type="search" placeholder="Try neon, betta, java fern…" autocomplete="off"></label>',
           '<p id="care-none" class="care-none" hidden>No guides match that search yet. Ask us in store and we will add it.</p>']
    groups = [("fish", "Fish"), ("invert", "Shrimp and snails"), ("plant", "Plants")]
    for kind, label in groups:
        items = sorted([e for e in by_slug.values() if e["kind"] == kind], key=lambda x: x["name"])
        if not items:
            continue
        out.append(f'<section class="care-group" data-kind="{kind}"><h2>{label}</h2><ul class="care-grid">')
        for e in items:
            if kind == "plant":
                meta = f"{e['light']} light · {e['placement']}"
            else:
                meta = f"{e['size']} · {e['tank']}+ gal"
            hay = " ".join([e["name"], e["sci"]] + e["aka"]).lower()
            out.append(f'<li data-hay="{E(hay)}"><a href="/care/{e["slug"]}/"><strong>{E(e["name"])}</strong><em>{E(e["sci"])}</em><span>{E(meta)}</span></a></li>')
        out.append("</ul></section>")
    out.append('<div class="callout"><strong>Own a fish store or run tank displays?</strong> Our <a href="/labels/">care label printer</a> turns a stock list into printable tank labels with QR codes to these guides.</div>')
    out.append('<div class="author-box"><strong>Pet Zone SD Team</strong> — Freshwater Guides is written and reviewed by the team behind Pet Zone Tropical Fish, a San Diego aquarium retailer. Care facts are general guidance, not a guarantee for any individual animal.</div>')
    out.append("</div>\n</main>")
    out.append(footer_html())
    out.append('<script src="/care/store.js" defer></script>\n</body>\n</html>\n')
    return "\n".join(out)

def write(path, content):
    full = os.path.join(ROOT, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    by_slug = {}
    for e in ALL:
        assert e["slug"] not in by_slug, e["slug"]
        by_slug[e["slug"]] = e
    for e in ALL:
        write(f"/care/{e['slug']}/index.html", page_for(e, by_slug))
    write("/care/index.html", index_page(by_slug))
    data = []
    for e in ALL:
        d = dict(e)
        d["temp"] = list(e["temp"]) if isinstance(e["temp"], tuple) else e["temp"]
        d["ph"] = list(e["ph"]) if isinstance(e["ph"], tuple) else e["ph"]
        d["tapfit"] = tap_fit(e)
        if photo_url(e["slug"]):
            d["photo"] = photo_url(e["slug"], "400x400")
        data.append(d)
    write("/care/data.json", json.dumps({"updated": TODAY, "stores": STORES, "items": data}, separators=(",", ":")))

    # sitemap
    sm_path = os.path.join(ROOT, "sitemap.xml")
    sm = open(sm_path, encoding="utf-8").read()
    sm = re.sub(r"<url><loc>https://freshwaterguides\.com/(care|labels|embed|service)/.*?</url>\n?", "", sm)
    new = [("/care/", "0.8"), ("/labels/", "0.7"), ("/embed/", "0.6"), ("/service/", "0.6")] + [(f"/care/{e['slug']}/", "0.6") for e in ALL]
    block = "".join(f"<url><loc>{BASE}{p}</loc><lastmod>{TODAY}</lastmod><changefreq>monthly</changefreq><priority>{pr}</priority></url>\n" for p, pr in new)
    sm = sm.replace("</urlset>", block + "</urlset>")
    open(sm_path, "w", encoding="utf-8").write(sm)

    # llms.txt
    lp = os.path.join(ROOT, "llms.txt")
    ll = open(lp, encoding="utf-8").read()
    ll = re.split(r"\n## Care guides\n", ll)[0].rstrip("\n") + "\n"
    ll += "\n## Care guides\n\n"
    ll += f"- [Care Guides index]({BASE}/care/): Quick care facts (tank size, temperature, pH, temperament, difficulty) for {len(ALL)} common freshwater fish, shrimp, snails and plants.\n"
    ll += f"- [Care label printer]({BASE}/labels/): A free tool for aquarium stores to print tank labels and take-home care sheets with QR codes to the care guides.\n"
    ll += f"- [Care facts embed]({BASE}/embed/): A free snippet that adds species care facts to fish, shrimp and plant product pages, with a link back to the full guide.\n"
    ll += f"- [Aquarium service toolkit]({BASE}/service/): A free in-browser tool for aquarium service businesses: client tanks, water test logs, maintenance reminders, visit reports and invoices with shareable links.\n"
    open(lp, "w", encoding="utf-8").write(ll)
    print(f"built {len(ALL)} care pages")

if __name__ == "__main__":
    main()
