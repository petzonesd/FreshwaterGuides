/*! Freshwater Guides care block — embeddable care facts for aquarium product pages.
    Usage:  <div data-fwg-care="neon-tetra"></div>   (or a name: "Neon Tetra")
            <div data-fwg-care="auto" data-title="h1.product-title"></div>
            <script src="https://freshwaterguides.com/embed/care.js" defer></script>
    Docs: https://freshwaterguides.com/embed/   */
(function () {
  'use strict';
  var BASE = 'https://freshwaterguides.com';
  var CSS = '.fwg-care{box-sizing:border-box;margin:1.2em 0;padding:1em 1.2em;border:1px solid #d9e5e1;border-left:4px solid #bfdc78;border-radius:4px;background:#fff;color:#10343b;font:14px/1.5 system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;max-width:640px}' +
    '.fwg-care *{box-sizing:border-box}.fwg-care h3{margin:0 0 .2em;font-size:1.05em;color:#0b3f4a}.fwg-care .fwg-sci{margin:0 0 .6em;font-style:italic;color:#557177;font-size:.9em}' +
    '.fwg-care dl{display:grid;grid-template-columns:max-content 1fr;gap:.2em 1em;margin:0}.fwg-care dt{font-weight:700;color:#0b3f4a}.fwg-care dd{margin:0}' +
    '.fwg-care .fwg-more{margin:.7em 0 0}.fwg-care a{color:#0b3f4a;font-weight:700}.fwg-care .fwg-credit{margin:.4em 0 0;font-size:.8em;color:#557177}';
  var ALLOW = {}; ('fish fishes live raised captive bred wild caught tropical freshwater assorted mix mixed random color colors colour variety male female pair trio group juvenile adult baby small medium large xl xxl xs sm md lg inch in inches cm mm approx approximately tank cichlid tetra shrimp snail plant plants potted bunch stem stems portion bare rhizome catfish zebra tiger red blue green black white gold golden yellow orange pink purple silver albino blood pigeon dalmatian electric neon super').split(' ').forEach(function (w) { ALLOW[singular(w)] = 1; });
  delete ALLOW['tank'];
  var PLANT_OK = { on: 1, wood: 1, rock: 1, root: 1, mat: 1, mesh: 1 };
  function okRest(rest, e) { return rest.every(function (w) { return /^[0-9]+$/.test(w) || ALLOW[w] || (e.kind === 'plant' && PLANT_OK[w]); }); }

  var DATA = null, waiting = [];
  function norm(s) { return String(s).toLowerCase().replace(/\(.*?\)/g, ' ').replace(/['’]/g, '').replace(/[^a-z0-9 ]+/g, ' ').replace(/\s+/g, ' ').trim(); }
  function singular(t) { return t.length > 3 && /s$/.test(t) ? t.replace(/ies$/, 'y').replace(/s$/, '') : t; }
  function toks(s) { return norm(s).split(' ').filter(Boolean).map(singular); }

  // strict matching: whole-phrase match of a known name, few leftover words, and none of them product-type words
  function findItem(query, auto) {
    query = String(query).replace(/tank[\s-]*(raised|bred)/ig, 'captive bred');
    var q = norm(query), qt = toks(query), best = null, bl = 0;
    if (!q) return null;
    DATA.items.forEach(function (e) {
      if (e.slug === query) { best = e; bl = 99; }
    });
    if (best) return best;
    DATA.items.forEach(function (e) {
      [e.name, e.sci].concat(e.aka || []).forEach(function (name) {
        var nt = toks(name); if (!nt.length) return;
        var exact = nt.join(' ') === qt.join(' ');
        if (exact && bl < 90) { best = e; bl = 90 + nt.length; return; }
        if (!auto || bl >= 90 || nt.length < 2 && name.length < 5) return;
        // phrase appears inside the (longer) title
        var s = qt.join(' '), p = nt.join(' ');
        var i = (' ' + s + ' ').indexOf(' ' + p + ' ');
        if (i < 0) return;
        if (/\b(black|green|false|blue|gold|golden|red|rainbow|glowlight) neons?\b/i.test(query) && !/\b(black|green|false|blue|gold|golden|red|rainbow|glowlight) neons?\b/i.test(name)) return;
        var rest = (' ' + s + ' ').replace(' ' + p + ' ', ' ').trim().split(' ').filter(Boolean);
        if (rest.length > 5 || !okRest(rest, e)) return;
        if (nt.length > bl) { best = e; bl = nt.length; }
      });
    });
    return best;
  }
  function rng(a, u) { return typeof a === 'string' ? a.replace('-', '–') : (a[0] + '–' + a[1] + (u || '')); }
  function ph(e) { return typeof e.ph === 'string' ? e.ph.replace('-', '–') : e.ph[0].toFixed(1) + '–' + e.ph[1].toFixed(1); }
  function rows(e) {
    if (e.kind === 'plant') return [['Light', e.light], ['CO₂', e.co2], ['Placement', e.placement], ['Height', e.height], ['Water', rng(e.temp, '°F') + ', pH ' + ph(e)], ['Difficulty', e.difficulty]];
    return [['Geographic range', e.origin], ['Average adult size', e.size], ['Preferred water', rng(e.temp, '°F') + ', pH ' + ph(e)], ['Minimum tank size', e.tank + ' gallons'],
      ['Temperament', e.temperament], ['Social behavior', e.social], ['Swim level', e.level], ['Difficulty', e.difficulty]];
  }
  function el(tag, cls, text) { var n = document.createElement(tag); if (cls) n.className = cls; if (text != null) n.textContent = text; return n; }

  function render(host, e) {
    var box = el('div', 'fwg-care');
    box.appendChild(el('h3', null, e.name + ' care facts'));
    box.appendChild(el('p', 'fwg-sci', e.sci));
    var dl = el('dl');
    rows(e).forEach(function (r) { dl.appendChild(el('dt', null, r[0])); dl.appendChild(el('dd', null, String(r[1]).replace(/(\d)-(\d)/g, '$1–$2'))); });
    box.appendChild(dl);
    var p = el('p', 'fwg-more'), a = el('a', null, 'Read the full ' + e.name + ' care guide →');
    a.href = BASE + '/care/' + e.slug + '/?utm_source=embed&utm_medium=product-page&utm_campaign=' + encodeURIComponent(location.hostname);
    a.rel = 'noopener'; p.appendChild(a); box.appendChild(p);
    var c = el('p', 'fwg-credit'); c.appendChild(document.createTextNode('Care information courtesy of '));
    var fa = el('a', null, 'Freshwater Guides'); fa.href = BASE + '/care/?utm_source=embed'; fa.rel = 'noopener'; c.appendChild(fa); c.appendChild(document.createTextNode('. General guidance; individual animals vary.'));
    box.appendChild(c);
    host.innerHTML = ''; host.appendChild(box);
  }

  function run() {
    if (!document.getElementById('fwg-care-css')) { var s = document.createElement('style'); s.id = 'fwg-care-css'; s.textContent = CSS; document.head.appendChild(s); }
    [].slice.call(document.querySelectorAll('[data-fwg-care]')).forEach(function (host) {
      var v = (host.getAttribute('data-fwg-care') || '').trim(), item = null;
      if (v === 'auto' && host.getAttribute('data-name')) {
        item = findItem(host.getAttribute('data-name'), true);
      } else if (!v || v === 'auto') {
        var sel = host.getAttribute('data-title') || 'h1', t = document.querySelector(sel);
        item = t ? findItem(t.textContent, true) : null;
      } else item = findItem(v, false);
      if (item) render(host, item); else host.style.display = 'none';
    });
  }
  function load() {
    fetch(BASE + '/care/data.json').then(function (r) { return r.json(); }).then(function (d) { DATA = d; run(); }).catch(function () {});
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', load); else load();
  window.FWGCare = { refresh: function () { if (DATA) run(); } };
})();
