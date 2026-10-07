(function () {
  'use strict';
  var BASE = 'https://freshwaterguides.com';
  var DATA = null, ITEMS = [], STORES = [], ROWS = [];
  var $ = function (id) { return document.getElementById(id); };

  function h(tag, attrs, kids) {
    var el = document.createElement(tag);
    if (attrs) Object.keys(attrs).forEach(function (k) {
      if (k === 'class') el.className = attrs[k];
      else if (k === 'text') el.textContent = attrs[k];
      else el.setAttribute(k, attrs[k]);
    });
    (kids || []).forEach(function (c) { if (c != null) el.appendChild(typeof c === 'string' ? document.createTextNode(c) : c); });
    return el;
  }
  function store(k, v) { try { if (v === undefined) return localStorage.getItem('fwg-labels-' + k); localStorage.setItem('fwg-labels-' + k, v); } catch (e) { return null; } }

  // ---------- formatting ----------
  function rng(a, u) { return (typeof a === 'string') ? a : (a[0] + '–' + a[1] + (u || '')); }
  function tempS(e) { return typeof e.temp === 'string' ? e.temp : rng(e.temp, '°F'); }
  function phS(e) { return typeof e.ph === 'string' ? e.ph.replace('-', '–') : (e.ph[0].toFixed(1) + '–' + e.ph[1].toFixed(1)); }
  function fix(s) { return String(s).replace(/(\d)-(\d)/g, '$1–$2'); }

  // ---------- matching ----------
  function norm(s) {
    return String(s).toLowerCase().replace(/['’]/g, '').replace(/[^a-z0-9 ]+/g, ' ').replace(/\s+/g, ' ').trim();
  }
  function toks(s) {
    return norm(s).split(' ').filter(Boolean).map(function (t) { return t.length > 3 && /s$/.test(t) ? t.replace(/ies$/, 'y').replace(/s$/, '') : t; });
  }
  function score(q, cand) {
    var nq = norm(q), nc = norm(cand);
    if (!nq || !nc) return 0;
    if (nq === nc) return 1;
    var tq = toks(q), tc = toks(cand);
    var set = {}; tc.forEach(function (t) { set[t] = 1; });
    var inter = tq.filter(function (t) { return set[t]; }).length;
    var uni = tq.length + tc.length - inter;
    var j = uni ? inter / uni : 0;
    if (inter === tq.length || inter === tc.length) j = Math.max(j, 0.8);
    return j;
  }
  function bestMatch(q) {
    var best = null, bs = 0;
    ITEMS.forEach(function (e, i) {
      var c = [e.name, e.sci].concat(e.aka || []);
      c.forEach(function (name) { var s = score(q, name); if (s > bs) { bs = s; best = i; } });
    });
    return bs >= 0.6 ? best : -1;
  }
  function parseLine(line) {
    var s = line.trim(); if (!s) return null;
    var price = '', m = s.match(/\s*[|\t]\s*(.+)$/);
    if (m) { price = m[1].trim(); s = s.slice(0, m.index).trim(); }
    else { m = s.match(/[\s,\-–]*\$\s*([0-9]+(?:\.[0-9]{1,2})?)\s*$/); if (m) { price = '$' + m[1]; s = s.slice(0, m.index).trim(); } }
    if (/^[0-9]+(\.[0-9]{1,2})?$/.test(price)) price = '$' + price;
    return s ? { raw: s, price: price } : null;
  }

  // ---------- review table ----------
  function addRow(parsed, idx) {
    var tbody = $('review').querySelector('tbody');
    var sel = h('select', { 'aria-label': 'Care guide for ' + parsed.raw });
    sel.appendChild(h('option', { value: '-1', text: '— skip this one —' }));
    var groups = { fish: 'Fish', invert: 'Shrimp, snails and crabs', amphibian: 'Frogs and newts', plant: 'Plants' };
    Object.keys(groups).forEach(function (k) {
      var og = h('optgroup', { label: groups[k] });
      ITEMS.forEach(function (e, i) { if (e.kind === k) og.appendChild(h('option', { value: String(i), text: e.name })); });
      sel.appendChild(og);
    });
    sel.value = String(idx);
    var nm = h('input', { type: 'text', 'aria-label': 'Name on label' });
    nm.value = idx >= 0 ? (norm(parsed.raw) === norm(ITEMS[idx].name) ? ITEMS[idx].name : parsed.raw) : '';
    var pr = h('input', { type: 'text', size: '7', 'aria-label': 'Price' }); pr.value = parsed.price;
    var cp = h('input', { type: 'number', min: '1', max: '99', value: '1', 'aria-label': 'Copies' });
    sel.addEventListener('change', function () {
      var i = parseInt(sel.value, 10);
      if (i >= 0 && (!nm.value || nm.dataset.auto === '1')) { nm.value = ITEMS[i].name; nm.dataset.auto = '1'; }
      tr.classList.toggle('unmatched', i < 0);
    });
    nm.addEventListener('input', function () { nm.dataset.auto = '0'; });
    var tr = h('tr', { class: idx < 0 ? 'unmatched' : '' }, [h('td', { text: parsed.raw }), h('td', null, [sel]), h('td', null, [nm]), h('td', null, [pr]), h('td', null, [cp])]);
    tr._f = { sel: sel, nm: nm, pr: pr, cp: cp };
    tbody.appendChild(tr);
  }
  function matchList() {
    var lines = $('list').value.split(/\n/).map(parseLine).filter(Boolean);
    store('list', $('list').value);
    var tbody = $('review').querySelector('tbody'); tbody.innerHTML = '';
    var miss = 0;
    lines.forEach(function (p) { var i = bestMatch(p.raw); if (i < 0) miss++; addRow(p, i); });
    $('review-wrap').hidden = !lines.length; $('types-wrap').hidden = !lines.length;
    $('review-note').textContent = lines.length
      ? (lines.length + ' items. ' + (miss ? miss + ' did not match; pick a guide from the list or leave them skipped. ' : 'All matched. ') + 'Fix any wrong match with the dropdown.')
      : '';
    $('print').disabled = true;
    if (lines.length) $('review-wrap').scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  // ---------- label building ----------
  function qrSvg(url) {
    var q = qrcode(0, 'M'); q.addData(url); q.make();
    var wrap = h('div', { class: 'qr' });
    wrap.innerHTML = q.createSvgTag({ cellSize: 1, margin: 3, scalable: true });
    return wrap;
  }
  function careUrl(e) {
    var loc = $('loc').value;
    return BASE + '/care/' + e.slug + '/?utm_source=label&utm_medium=qr' + (loc ? '&loc=' + loc : '');
  }
  function storeLines() {
    var loc = $('loc').value;
    var list = STORES.filter(function (s) { return !loc || s.id === loc; });
    return list.map(function (x) { return { id: x.id, name: x.name, addr: x.addr, phone: x.phone.replace(' ', '\u00a0').replace('-', '\u2011') }; });
  }
  function storeLine(compact) {
    return storeLines().map(function (s) { return compact ? (s.name + ' ' + s.phone) : (s.name + ' · ' + s.addr + ' · ' + s.phone); });
  }
  function stats(e, level) {
    if (e.kind === 'plant') {
      var base = [['Light', e.light], ['CO₂', e.co2], ['Placement', e.placement], ['Height', e.height], ['Temp', tempS(e)], ['pH', phS(e)], ['Difficulty', e.difficulty]];
      return base;
    }
    return [['Adult size', e.size], ['Min. tank', e.tank + ' gal'], ['Temp', tempS(e)], ['pH', phS(e)], ['Temperament', e.temperament], ['Social', e.social], ['Swim level', e.level], ['Difficulty', e.difficulty]];
  }
  function nameSize(name) { var n = name.length; return n > 30 ? 'xs' : n > 22 ? 's' : n > 15 ? 'm' : 'l'; }

  function small(r) {
    var e = r.e, st = stats(e);
    var line1 = e.kind === 'plant' ? (e.light + ' light · ' + (e.co2 === 'Not required' ? 'no CO₂ needed' : 'CO₂ ' + e.co2.toLowerCase())) : ('Min. ' + e.tank + ' gal · ' + tempS(e));
    var line2 = e.kind === 'plant' ? (e.placement + ' · ' + e.height) : e.social;
    return h('div', { class: 'lbl small' }, [
      h('div', { class: 'lbl-text' }, [
        h('div', { class: 'lbl-brand', text: 'Pet Zone' }),
        h('div', { class: 'lbl-name sz-' + nameSize(r.name), text: r.name }),
        h('div', { class: 'lbl-sci', text: e.sci }),
        h('div', { class: 'lbl-line', text: fix(line1) }),
        h('div', { class: 'lbl-line', text: fix(line2) }),
        r.price ? h('div', { class: 'lbl-price', text: r.price }) : null
      ]),
      h('div', { class: 'lbl-qr' }, [qrSvg(careUrl(e)), h('div', { class: 'lbl-scan', text: 'Scan for care guide' })])
    ]);
  }
  function large(r) {
    var e = r.e;
    var dl = h('dl', { class: 'lbl-facts' });
    stats(e).forEach(function (kv) { dl.appendChild(h('dt', { text: kv[0] })); dl.appendChild(h('dd', { text: fix(kv[1]) })); });
    return h('div', { class: 'lbl large' }, [
      h('div', { class: 'lbl-head' }, [h('div', { class: 'lbl-brand', text: 'Pet Zone Tropical Fish' }), r.price ? h('div', { class: 'lbl-price', text: r.price }) : null]),
      h('div', { class: 'lbl-name sz-' + nameSize(r.name), text: r.name }),
      h('div', { class: 'lbl-sci', text: e.sci }),
      h('div', { class: 'lbl-body' }, [dl, h('div', { class: 'lbl-qr' }, [qrSvg(careUrl(e)), h('div', { class: 'lbl-scan', text: 'Scan for the full care guide' })])]),
      h('div', { class: 'lbl-foot', text: storeLine(true).join('  ·  ') })
    ]);
  }
  function sheet(r) {
    var e = r.e;
    var tbl = h('table', { class: 'sh-facts' });
    stats(e).forEach(function (kv) { tbl.appendChild(h('tr', null, [h('th', { text: kv[0] }), h('td', { text: fix(kv[1]) })])); });
    var steps = e.kind === 'plant'
      ? ['Rinse the plant and remove any plastic pot or rockwool.', 'Trim dead or damaged leaves and roots.', 'Plant the roots in substrate, or attach epiphytes to wood or rock. Do not bury the rhizome.', 'Give it a few weeks to settle; some leaves may melt and regrow.']
      : e.kind === 'amphibian'
      ? ['Keep the bag out of bright light on the way home.', 'Float the sealed bag for 15 minutes, then add small amounts of tank water over 30 minutes.', 'Gently net the animal into the tank. Do not pour the bag water in.', 'Wash your hands before and after handling anything in the tank, and keep the lid secure.']
      : e.kind === 'invert'
      ? ['Keep the bag out of bright light on the way home.', 'Float the sealed bag for 15 minutes, then drip tank water into a container with the animal for 45 to 60 minutes.', 'Net it into the tank and discard the bag water.', 'Never use copper-based medications.']
      : ['Float the sealed bag in the tank for 15 to 20 minutes to match temperature.', 'Add a little tank water to the bag every 5 minutes for 15 to 30 minutes.', 'Net the fish into the tank and discard the bag water.', 'Dim the lights and wait a few hours before feeding. Test your water weekly.'];
    return h('div', { class: 'lbl sheet' }, [
      h('div', { class: 'lbl-head' }, [h('div', { class: 'lbl-brand', text: 'Pet Zone Tropical Fish · care sheet' }), r.price ? null : null]),
      e.photo ? (function () { var im = h('img', { class: 'sh-photo', src: e.photo, alt: '' }); im.onerror = function () { im.remove(); }; return im; })() : null,
      h('div', { class: 'lbl-name sz-' + nameSize(r.name), text: r.name }),
      h('div', { class: 'lbl-sci', text: e.sci }),
      h('p', { class: 'sh-note', text: e.note }),
      tbl,
      h('h4', { text: 'Quick tips' }), h('ul', null, e.tips.map(function (t) { return h('li', { text: t }); })),
      h('h4', { text: 'Getting it home' }), h('ol', null, steps.map(function (t) { return h('li', { text: t }); })),
      h('h4', { text: 'San Diego water' }), h('p', { class: 'sh-small', text: e.tapfit }),
      h('div', { class: 'sh-foot' }, [
        h('div', null, storeLine(false).map(function (t) { return h('div', { text: t }); }).concat([h('div', { text: 'petzonesd.com' })])),
        h('div', { class: 'lbl-qr' }, [qrSvg(careUrl(e)), h('div', { class: 'lbl-scan', text: 'Full care guide' })])
      ])
    ]);
  }
  function sign() {
    return h('div', { class: 'lbl sign' }, [
      h('div', { class: 'lbl-brand', text: 'Pet Zone Tropical Fish' }),
      h('div', { class: 'sign-big', text: 'Scan any tank label for care facts' }),
      h('div', { class: 'lbl-qr' }, [qrSvg(BASE + '/care/?utm_source=sign&utm_medium=qr' + ($('loc').value ? '&loc=' + $('loc').value : ''))]),
      h('p', { class: 'sign-sub', text: 'Tank size, temperature, pH, temperament and more for every fish, shrimp and plant we sell.' }),
      h('div', { class: 'sign-foot' }, storeLine(false).map(function (t) { return h('div', { text: t }); }))
    ]);
  }

  function collect() {
    var out = [];
    [].slice.call($('review').querySelectorAll('tbody tr')).forEach(function (tr) {
      var f = tr._f, i = parseInt(f.sel.value, 10);
      if (i < 0) return;
      var e = ITEMS[i], copies = Math.max(1, Math.min(99, parseInt(f.cp.value, 10) || 1));
      var price = f.pr.value.trim(); if (/^[0-9]+(\.[0-9]{1,2})?$/.test(price)) price = '$' + price;
      out.push({ e: e, name: (f.nm.value.trim() || e.name), price: price, copies: copies });
    });
    return out;
  }
  function page(cls, kids) { return h('section', { class: 'pg ' + cls }, kids); }
  function build() {
    var rows = collect(), root = $('print-root'); root.innerHTML = '';
    var types = [].slice.call(document.querySelectorAll('.ptype:checked')).map(function (c) { return c.value; });
    if (!rows.length || !types.length) { root.appendChild(h('p', { class: 'no-print lab-empty', text: 'Nothing to print yet: match at least one item and choose a piece.' })); $('print').disabled = true; return; }
    function chunk(arr, n) { var o = []; for (var i = 0; i < arr.length; i += n) o.push(arr.slice(i, i + n)); return o; }
    function expand(fn) { var o = []; rows.forEach(function (r) { for (var c = 0; c < r.copies; c++) o.push(fn(r)); }); return o; }
    if (types.indexOf('small') >= 0) chunk(expand(small), 10).forEach(function (c) { root.appendChild(page('p-small', c)); });
    if (types.indexOf('large') >= 0) chunk(expand(large), 6).forEach(function (c) { root.appendChild(page('p-large', c)); });
    if (types.indexOf('sheet') >= 0) chunk(expand(sheet), 2).forEach(function (c) { root.appendChild(page('p-sheet', c)); });
    if (types.indexOf('sign') >= 0) root.appendChild(page('p-sign', [sign()]));
    $('print').disabled = false;
    root.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  // ---------- init ----------
  function init() {
    fetch('/care/data.json').then(function (r) { return r.json(); }).then(function (d) {
      DATA = d; ITEMS = d.items; STORES = d.stores;
      var dl = $('catalog');
      ITEMS.slice().sort(function (a, b) { return a.name.localeCompare(b.name); }).forEach(function (e) { dl.appendChild(h('option', { value: e.name })); });
      var saved = store('list'); if (saved) $('list').value = saved;
      var sl = store('loc'); if (sl !== null && sl !== undefined) $('loc').value = sl;
    }).catch(function () { $('review-note').textContent = 'Could not load the care catalog. Check your connection and reload.'; });

    $('match').addEventListener('click', matchList);
    $('build').addEventListener('click', build);
    $('print').addEventListener('click', function () { window.print(); });
    $('loc').addEventListener('change', function () { store('loc', $('loc').value); });
    $('clear').addEventListener('click', function () { $('list').value = ''; store('list', ''); $('review').querySelector('tbody').innerHTML = ''; $('review-wrap').hidden = true; $('types-wrap').hidden = true; $('print-root').innerHTML = ''; });
    $('sample').addEventListener('click', function () {
      $('list').value = ['Neon Tetra | $2.99', 'Cardinal Tetra | $3.99', 'Panda Cory | $6.99', 'CPD | $4.99', 'Betta | $14.99', 'Bristlenose Pleco', 'Cherry shrimp | $3.49', 'Nerite snail', 'Java Fern', 'Anubias Nana', 'Amazon Sword'].join('\n');
    });
    $('add-btn').addEventListener('click', function () {
      var v = $('add-q').value.trim(); if (!v) return;
      $('list').value = ($('list').value.replace(/\s+$/, '') + '\n' + v).trim(); $('add-q').value = '';
    });
  }
  init();
})();
