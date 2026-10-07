(function () {
  'use strict';
  var KEY = 'fwg-service-v1';
  var TABS = [['dash', 'Dashboard'], ['clients', 'Clients and tanks'], ['visit', 'Visit report'], ['invoices', 'Invoices'], ['settings', 'Settings']];
  var TEST_FIELDS = [['temp', 'Temp °F'], ['ph', 'pH'], ['ammonia', 'Ammonia'], ['nitrite', 'Nitrite'], ['nitrate', 'Nitrate'], ['gh', 'GH'], ['kh', 'KH']];
  var INTERVALS = { monthly: 1, quarterly: 3, '6months': 6, yearly: 12 };
  var DEFAULT_TASKS = [['Water change', 7], ['Glass cleaning', 7], ['Filter media rinse', 30], ['Gravel vacuum', 14], ['Dose fertilizer / supplements', 7]];

  function blank() { return { v: 1, biz: { name: '', contact: '', phone: '', email: '', venmo: '', paypal: '', cashapp: '', zelle: '', taxRate: 0, prefix: 'INV-', next: 1, dueDays: 14 }, clients: [], tanks: [], visits: [], invoices: [] }; }
  var S = load(), storageOk = true;
  function load() { try { var r = localStorage.getItem(KEY); if (r) { var o = JSON.parse(r), b = blank(); return Object.assign(b, o, { biz: Object.assign(b.biz, o.biz || {}) }); } } catch (e) { } return blank(); }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(S)); storageOk = true; } catch (e) { storageOk = false; warn('This browser is blocking storage, so changes will be lost when you close the page. Download a backup from Settings, or turn off private browsing.'); } }
  function warn(msg) { var w = $('warn'); w.textContent = msg; w.hidden = !msg; }
  var $ = function (id) { return document.getElementById(id); };
  function uid() { return Date.now().toString(36) + Math.random().toString(36).slice(2, 6); }
  function iso(d) { return d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0'); }
  function todayS() { return iso(new Date()); }
  function dt(s) { return new Date(s + 'T12:00:00'); }
  function addDays(s, n) { var d = dt(s); d.setDate(d.getDate() + n); return iso(d); }
  function addMonths(s, n) { var d = dt(s); var day = d.getDate(); d.setDate(1); d.setMonth(d.getMonth() + n); var last = new Date(d.getFullYear(), d.getMonth() + 1, 0).getDate(); d.setDate(Math.min(day, last)); return iso(d); }
  function daysBetween(a, b) { return Math.round((dt(b) - dt(a)) / 86400000); }
  function fmt(s) { return s ? dt(s).toLocaleDateString(undefined, { month: 'short', day: 'numeric', year: 'numeric' }) : ''; }
  function money(n) { return '$' + (Math.round(n * 100) / 100).toFixed(2); }
  function by(arr, id) { return arr.filter(function (x) { return x.id === id; })[0]; }
  function clientName(id) { var c = by(S.clients, id); return c ? c.name : '(deleted client)'; }

  // ---------- dom helpers ----------
  function h(tag, attrs, kids) {
    var el = document.createElement(tag);
    if (attrs) Object.keys(attrs).forEach(function (k) {
      if (k === 'class') el.className = attrs[k]; else if (k === 'text') el.textContent = attrs[k]; else if (k === 'on') Object.keys(attrs.on).forEach(function (ev) { el.addEventListener(ev, attrs.on[ev]); });
      else if (attrs[k] !== false && attrs[k] != null) el.setAttribute(k, attrs[k]);
    });
    (kids || []).forEach(function (c) { if (c != null) el.appendChild(typeof c === 'string' ? document.createTextNode(c) : c); });
    return el;
  }
  function btn(label, fn, cls) { return h('button', { type: 'button', class: 'sbtn ' + (cls || ''), on: { click: fn } }, [label]); }
  function field(label, input, cls) { return h('label', { class: 'sf ' + (cls || '') }, [h('span', { text: label }), input]); }
  function input(obj, key, type, extra) {
    var i = h('input', Object.assign({ type: type || 'text' }, extra || {}));
    i.value = obj[key] == null ? '' : obj[key];
    i.addEventListener('change', function () { obj[key] = (type === 'number') ? (i.value === '' ? '' : Number(i.value)) : i.value; save(); });
    return i;
  }
  function textarea(obj, key, rows) { var t = h('textarea', { rows: rows || 3 }); t.value = obj[key] || ''; t.addEventListener('change', function () { obj[key] = t.value; save(); }); return t; }
  function select(obj, key, opts) {
    var s = h('select'); opts.forEach(function (o) { s.appendChild(h('option', { value: o[0], text: o[1] })); });
    s.value = obj[key] == null ? opts[0][0] : obj[key]; s.addEventListener('change', function () { obj[key] = s.value; save(); }); return s;
  }
  function card(title, kids, cls) { return h('section', { class: 'scard ' + (cls || '') }, [title ? h('h2', { text: title }) : null].concat(kids)); }

  // ---------- ui state ----------
  var ui = { tab: 'dash', clientId: null, tankId: null, invId: null, visit: null, msg: '' };
  function go(tab, extra) { ui.tab = tab; Object.assign(ui, extra || {}); render(); window.scrollTo({ top: $('tabs').offsetTop - 10, behavior: 'smooth' }); }
  function render() {
    var tabs = $('tabs'); tabs.innerHTML = '';
    TABS.forEach(function (t) { tabs.appendChild(h('button', { type: 'button', class: 'stab' + (ui.tab === t[0] ? ' on' : ''), 'aria-current': ui.tab === t[0] ? 'page' : false, on: { click: function () { go(t[0]); } } }, [t[1]])); });
    var app = $('app'); app.innerHTML = '';
    var views = { dash: dash, clients: clients, visit: visit, invoices: invoices, settings: settings };
    app.appendChild(views[ui.tab]());
    if (ui.msg) { app.insertBefore(h('p', { class: 'smsg', role: 'status', text: ui.msg }), app.firstChild); ui.msg = ''; }
  }

  // ---------- share ----------
  function bizShare(withPay) { var b = S.biz, o = { name: b.name, contact: b.contact, phone: b.phone, email: b.email }; if (withPay) { o.venmo = b.venmo; o.paypal = b.paypal; o.cashapp = b.cashapp; o.zelle = b.zelle; } return o; }
  function clipboardLink(payload, label) {
    return FWGShare.link(payload).then(function (url) {
      var done = function () { ui.msg = label + ' link copied. Paste it into a text or email. (' + url.length + ' characters)'; render(); };
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(url).then(done, function () { window.prompt('Copy this link:', url); });
      else window.prompt('Copy this link:', url);
      return url;
    });
  }
  function openLink(payload) { FWGShare.link(payload).then(function (url) { window.open(url, '_blank', 'noopener'); }); }
  function visitPayload(v) {
    var c = by(S.clients, v.clientId), t = v.tankId ? by(S.tanks, v.tankId) : null;
    return { t: 'report', biz: bizShare(false), client: c ? c.name : '', tank: t ? t.name : '', gallons: t ? t.gallons : '', date: v.date, done: v.done || [], tests: v.tests || {}, work: v.work || '', notes: v.notes || '', next: v.next || '' };
  }
  function invTotals(inv) { var sub = 0; (inv.items || []).forEach(function (i) { sub += (Number(i.qty) || 0) * (Number(i.price) || 0); }); var tax = sub * (Number(inv.taxRate) || 0) / 100; return { sub: sub, tax: tax, total: sub + tax }; }
  function invPayload(inv) {
    var c = by(S.clients, inv.clientId);
    return { t: 'invoice', biz: bizShare(true), no: inv.no, client: c ? c.name : '', clientContact: c ? [c.contact, c.email, c.phone].filter(Boolean).join(' · ') : '', date: inv.date, due: inv.due, items: inv.items, taxRate: inv.taxRate, status: inv.status, paidDate: inv.paidDate, notes: inv.notes };
  }

  // ---------- dashboard ----------
  function dueTasks() {
    var out = [], t0 = todayS();
    S.tanks.forEach(function (t) { (t.tasks || []).forEach(function (k) {
      if (!k.every) return;
      var over = k.last ? daysBetween(k.last, t0) - Number(k.every) : 0;
      if (!k.last || over >= 0) out.push({ tank: t, task: k, over: over, never: !k.last });
    }); });
    return out.sort(function (a, b) { return b.over - a.over; });
  }
  function recurringDue() { var t0 = todayS(); return S.clients.filter(function (c) { return c.rec && c.rec.on && c.rec.next && c.rec.next <= t0; }); }
  function newInvoice(clientId, items) {
    var b = S.biz, no = (b.prefix || '') + String(b.next || 1).padStart(3, '0'); b.next = (Number(b.next) || 1) + 1;
    var d = todayS(), inv = { id: uid(), no: no, clientId: clientId, date: d, due: addDays(d, Number(b.dueDays) || 14), items: items || [{ desc: '', qty: 1, price: 0 }], taxRate: Number(b.taxRate) || 0, status: 'draft', notes: '' };
    S.invoices.push(inv); save(); return inv;
  }
  function dash() {
    var t0 = todayS(), wrap = h('div');
    var due = dueTasks();
    wrap.appendChild(card('Maintenance due (' + due.length + ')', due.length ? [h('table', { class: 'stbl' }, [h('thead', null, [h('tr', null, ['Client', 'Tank', 'Task', 'Status', ''].map(function (x) { return h('th', { text: x }); }))]),
      h('tbody', null, due.slice(0, 40).map(function (d) {
        return h('tr', null, [h('td', { text: clientName(d.tank.clientId) }), h('td', { text: d.tank.name }), h('td', { text: d.task.name }),
          h('td', { text: d.never ? 'Never done' : (d.over === 0 ? 'Due today' : d.over + ' day' + (d.over > 1 ? 's' : '') + ' overdue'), class: d.over > 0 || d.never ? 'late' : '' }),
          h('td', null, [btn('Done today', function () { d.task.last = t0; save(); render(); })])]);
      }))])] : [h('p', { text: S.tanks.length ? 'Nothing due. Nice work.' : 'Add a client and a tank, then give the tank maintenance tasks. They will show up here.' })]));
    var rec = recurringDue();
    wrap.appendChild(card('Recurring invoices ready (' + rec.length + ')', rec.length ? rec.map(function (c) {
      return h('div', { class: 'srow' }, [h('span', { text: c.name + ': ' + (c.rec.desc || 'Monthly service') + ' ' + money(Number(c.rec.amount) || 0) + ' (was due ' + fmt(c.rec.next) + ')' }),
        btn('Create invoice', function () {
          var inv = newInvoice(c.id, [{ desc: c.rec.desc || 'Aquarium service', qty: 1, price: Number(c.rec.amount) || 0 }]);
          c.rec.next = addMonths(c.rec.next, INTERVALS[c.rec.every] || 1); save(); go('invoices', { invId: inv.id, msg: 'Created ' + inv.no + '.' });
        })]);
    }) : [h('p', { text: 'None due. Turn on a recurring invoice for a client under Clients and tanks.' })]));
    var unpaid = S.invoices.filter(function (i) { return i.status === 'sent'; });
    var out = 0, late = 0; unpaid.forEach(function (i) { var t = invTotals(i).total; out += t; if (i.due && i.due < t0) late += t; });
    var paidMonth = 0; S.invoices.forEach(function (i) { if (i.status === 'paid' && (i.paidDate || '').slice(0, 7) === t0.slice(0, 7)) paidMonth += invTotals(i).total; });
    wrap.appendChild(card('Money', [h('div', { class: 'sstats' }, [stat('Outstanding', money(out)), stat('Past due', money(late), late ? 'late' : ''), stat('Paid this month', money(paidMonth)), stat('Clients', String(S.clients.length)), stat('Tanks', String(S.tanks.length))])]));
    return wrap;
  }
  function stat(l, v, c) { return h('div', { class: 'sstat ' + (c || '') }, [h('div', { class: 'sv', text: v }), h('div', { class: 'sl', text: l })]); }

  // ---------- clients & tanks ----------
  function clients() {
    var wrap = h('div', { class: 'ssplit' }), list = h('div', { class: 'slist' });
    list.appendChild(btn('+ Add client', function () { var c = { id: uid(), name: 'New client', contact: '', phone: '', email: '', address: '', notes: '', rec: { on: false, every: 'monthly', next: todayS(), amount: '', desc: 'Monthly aquarium service' } }; S.clients.push(c); save(); ui.clientId = c.id; ui.tankId = null; render(); }, 'primary'));
    S.clients.slice().sort(function (a, b) { return a.name.localeCompare(b.name); }).forEach(function (c) {
      list.appendChild(h('button', { type: 'button', class: 'sitem' + (ui.clientId === c.id ? ' on' : ''), on: { click: function () { ui.clientId = c.id; ui.tankId = null; render(); } } }, [c.name || '(no name)', h('small', { text: S.tanks.filter(function (t) { return t.clientId === c.id; }).length + ' tank(s)' })]));
    });
    if (!S.clients.length) list.appendChild(h('p', { class: 'smuted', text: 'No clients yet.' }));
    wrap.appendChild(list);
    var c = ui.clientId && by(S.clients, ui.clientId);
    var det = h('div', { class: 'sdetail' });
    if (!c) det.appendChild(h('p', { class: 'smuted', text: 'Pick a client, or add one.' }));
    else det.appendChild(clientForm(c));
    wrap.appendChild(det);
    return wrap;
  }
  function clientForm(c) {
    var f = h('div');
    var nameIn = input(c, 'name'); nameIn.addEventListener('change', function () { render(); });
    f.appendChild(card('Client', [h('div', { class: 'sgrid' }, [field('Name', nameIn), field('Contact person', input(c, 'contact')), field('Phone', input(c, 'phone', 'tel')), field('Email', input(c, 'email', 'email')), field('Address', input(c, 'address'), 'wide')]), field('Notes (access, pets, alarm codes: keep it brief)', textarea(c, 'notes', 2))]));
    if (!c.rec) c.rec = { on: false, every: 'monthly', next: todayS(), amount: '', desc: 'Monthly aquarium service' };
    var recOn = h('input', { type: 'checkbox' }); recOn.checked = !!c.rec.on; recOn.addEventListener('change', function () { c.rec.on = recOn.checked; save(); });
    f.appendChild(card('Recurring invoice', [h('label', { class: 'scheck' }, [recOn, ' Bill this client on a schedule']), h('div', { class: 'sgrid' }, [
      field('Repeats', select(c.rec, 'every', [['monthly', 'Monthly'], ['quarterly', 'Quarterly'], ['6months', 'Every 6 months'], ['yearly', 'Yearly']])), field('Next invoice date', input(c.rec, 'next', 'date')),
      field('Amount ($)', input(c.rec, 'amount', 'number', { step: '0.01', min: '0' })), field('Description', input(c.rec, 'desc'))]), h('p', { class: 'smuted', text: 'When the date arrives, the Dashboard offers a ready-to-send invoice. Nothing is sent automatically.' })]));
    var tanks = S.tanks.filter(function (t) { return t.clientId === c.id; });
    f.appendChild(card('Tanks (' + tanks.length + ')', [btn('+ Add tank', function () {
      var t = { id: uid(), clientId: c.id, name: 'Tank ' + (tanks.length + 1), gallons: '', type: 'Freshwater community', livestock: '', equipment: '', notes: '', tasks: DEFAULT_TASKS.map(function (d) { return { id: uid(), name: d[0], every: d[1], last: '' }; }), tests: [] };
      S.tanks.push(t); save(); ui.tankId = t.id; render();
    }, 'primary')].concat(tanks.map(function (t) { return h('button', { type: 'button', class: 'sitem inline' + (ui.tankId === t.id ? ' on' : ''), on: { click: function () { ui.tankId = ui.tankId === t.id ? null : t.id; render(); } } }, [t.name + (t.gallons ? ' · ' + t.gallons + ' gal' : '')]); }))));
    if (ui.tankId && by(S.tanks, ui.tankId) && by(S.tanks, ui.tankId).clientId === c.id) f.appendChild(tankForm(by(S.tanks, ui.tankId)));
    f.appendChild(h('p', null, [btn('Delete this client and their tanks', function () {
      if (!confirm('Delete ' + c.name + ' and all their tanks? Invoices and reports already saved stay in your records.')) return;
      S.tanks = S.tanks.filter(function (t) { return t.clientId !== c.id; }); S.clients = S.clients.filter(function (x) { return x.id !== c.id; }); ui.clientId = null; ui.tankId = null; save(); render();
    }, 'danger')]));
    return f;
  }
  function tankForm(t) {
    var nameIn = input(t, 'name');
    var f = card('Tank: ' + t.name, [h('div', { class: 'sgrid' }, [field('Name', nameIn), field('Gallons', input(t, 'gallons', 'number', { min: '0' })),
      field('Type', select(t, 'type', [['Freshwater community', 'Freshwater community'], ['Planted', 'Planted'], ['Cichlid', 'Cichlid'], ['Goldfish', 'Goldfish'], ['Shrimp', 'Shrimp'], ['Brackish', 'Brackish'], ['Pond', 'Pond'], ['Other', 'Other']])),
      field('Livestock', input(t, 'livestock'), 'wide'), field('Equipment', input(t, 'equipment'), 'wide')]), field('Notes', textarea(t, 'notes', 2))], 'inner');
    f.appendChild(h('h3', { text: 'Maintenance tasks' }));
    var tt = h('table', { class: 'stbl' }, [h('thead', null, [h('tr', null, ['Task', 'Every (days)', 'Last done', ''].map(function (x) { return h('th', { text: x }); }))])]);
    var tb = h('tbody'); (t.tasks = t.tasks || []).forEach(function (k) {
      tb.appendChild(h('tr', null, [h('td', null, [input(k, 'name')]), h('td', null, [input(k, 'every', 'number', { min: '1' })]), h('td', null, [input(k, 'last', 'date')]), h('td', null, [btn('Remove', function () { t.tasks = t.tasks.filter(function (x) { return x !== k; }); save(); render(); }, 'small')])]));
    });
    tt.appendChild(tb); f.appendChild(h('div', { class: 'stbl-wrap' }, [tt]));
    f.appendChild(btn('+ Add task', function () { t.tasks.push({ id: uid(), name: '', every: 7, last: '' }); save(); render(); }));
    f.appendChild(h('h3', { text: 'Water test log' }));
    var nt = { date: todayS() }; var row = h('div', { class: 'sgrid tests' }, [field('Date', input(nt, 'date', 'date'))].concat(TEST_FIELDS.map(function (tf) { return field(tf[1], input(nt, tf[0], 'text', { inputmode: 'decimal', size: '5' })); })));
    f.appendChild(row);
    f.appendChild(btn('Add reading', function () { var r = Object.assign({}, nt); (t.tests = t.tests || []).push(r); t.tests.sort(function (a, b) { return a.date < b.date ? 1 : -1; }); save(); render(); }));
    if ((t.tests || []).length) {
      var lt = h('table', { class: 'stbl' }, [h('thead', null, [h('tr', null, ['Date'].concat(TEST_FIELDS.map(function (x) { return x[1]; })).map(function (x) { return h('th', { text: x }); }))]),
        h('tbody', null, t.tests.slice(0, 12).map(function (r) { return h('tr', null, [h('td', { text: fmt(r.date) })].concat(TEST_FIELDS.map(function (x) { return h('td', { text: r[x[0]] == null ? '' : String(r[x[0]]) }); }))); }))]);
      f.appendChild(h('div', { class: 'stbl-wrap' }, [lt]));
    }
    f.appendChild(h('p', null, [btn('Delete this tank', function () { if (!confirm('Delete ' + t.name + '?')) return; S.tanks = S.tanks.filter(function (x) { return x !== t; }); ui.tankId = null; save(); render(); }, 'danger')]));
    return f;
  }

  // ---------- visit report ----------
  function visit() {
    var wrap = h('div');
    if (!S.clients.length) return card('Visit report', [h('p', { text: 'Add a client and a tank first (Clients and tanks).' })]);
    if (!ui.visit) ui.visit = { id: uid(), clientId: ui.clientId || S.clients[0].id, tankId: '', date: todayS(), done: [], doneIds: [], tests: {}, work: '', notes: '', next: '' };
    var v = ui.visit, tanks = S.tanks.filter(function (t) { return t.clientId === v.clientId; });
    var cs = h('select'); S.clients.forEach(function (c) { cs.appendChild(h('option', { value: c.id, text: c.name })); }); cs.value = v.clientId;
    cs.addEventListener('change', function () { v.clientId = cs.value; v.tankId = ''; v.doneIds = []; render(); });
    var ts = h('select'); ts.appendChild(h('option', { value: '', text: '(no specific tank)' })); tanks.forEach(function (t) { ts.appendChild(h('option', { value: t.id, text: t.name })); }); ts.value = v.tankId || '';
    ts.addEventListener('change', function () { v.tankId = ts.value; v.doneIds = []; render(); });
    var f = card('New visit report', [h('div', { class: 'sgrid' }, [field('Client', cs), field('Tank', ts), field('Date', (function () { var i = h('input', { type: 'date' }); i.value = v.date; i.addEventListener('change', function () { v.date = i.value; }); return i; })())])]);
    var tank = v.tankId && by(S.tanks, v.tankId);
    if (tank && (tank.tasks || []).length) {
      f.appendChild(h('h3', { text: 'Work completed (checked tasks are marked done today)' }));
      tank.tasks.forEach(function (k) { var cb = h('input', { type: 'checkbox' }); cb.checked = v.doneIds.indexOf(k.id) >= 0; cb.addEventListener('change', function () { v.doneIds = v.doneIds.filter(function (x) { return x !== k.id; }); if (cb.checked) v.doneIds.push(k.id); }); f.appendChild(h('label', { class: 'scheck' }, [cb, ' ' + k.name])); });
    }
    f.appendChild(h('label', { class: 'sf' }, [h('span', { text: 'Other work done (one per line)' }), (function () { var t = h('textarea', { rows: 2 }); t.value = v.extra || ''; t.addEventListener('change', function () { v.extra = t.value; }); return t; })()]));
    f.appendChild(h('h3', { text: 'Water test results (optional)' }));
    f.appendChild(h('div', { class: 'sgrid tests' }, TEST_FIELDS.map(function (tf) { var i = h('input', { type: 'text', inputmode: 'decimal', size: '5' }); i.value = v.tests[tf[0]] || ''; i.addEventListener('change', function () { v.tests[tf[0]] = i.value; }); return field(tf[1], i); })));
    f.appendChild(field('Notes on the visit', (function () { var t = h('textarea', { rows: 3 }); t.value = v.work; t.addEventListener('change', function () { v.work = t.value; }); return t; })()));
    f.appendChild(field('Recommendations for the client', (function () { var t = h('textarea', { rows: 3 }); t.value = v.notes; t.addEventListener('change', function () { v.notes = t.value; }); return t; })()));
    f.appendChild(field('Next visit', (function () { var i = h('input', { type: 'date' }); i.value = v.next; i.addEventListener('change', function () { v.next = i.value; }); return i; })()));
    function finish() {
      var saved = Object.assign({}, v); saved.done = [];
      if (tank) (tank.tasks || []).forEach(function (k) { if (v.doneIds.indexOf(k.id) >= 0) { saved.done.push(k.name); k.last = v.date; } });
      (v.extra || '').split(/\n/).forEach(function (l) { if (l.trim()) saved.done.push(l.trim()); });
      var tests = {}; Object.keys(v.tests).forEach(function (k) { if (String(v.tests[k]).trim() !== '') tests[k] = v.tests[k]; }); saved.tests = tests;
      if (tank && Object.keys(tests).length) { var r = Object.assign({ date: v.date }, tests); (tank.tests = tank.tests || []).push(r); tank.tests.sort(function (a, b) { return a.date < b.date ? 1 : -1; }); }
      if (tank && v.next) { /* nothing else to update */ }
      S.visits = S.visits.filter(function (x) { return x.id !== saved.id; }); S.visits.push(saved); save(); return saved;
    }
    f.appendChild(h('div', { class: 'sactions' }, [
      btn('Save and copy share link', function () { var s = finish(); ui.visit = null; clipboardLink(visitPayload(s), 'Report'); }, 'primary'),
      btn('Save and open printable view', function () { var s = finish(); ui.visit = null; openLink(visitPayload(s)); ui.msg = 'Report saved.'; render(); }),
      btn('Save only', function () { finish(); ui.visit = null; ui.msg = 'Report saved. Find it below.'; render(); })]));
    wrap.appendChild(f);
    var past = S.visits.slice().sort(function (a, b) { return a.date < b.date ? 1 : -1; }).slice(0, 25);
    wrap.appendChild(card('Past reports (' + S.visits.length + ')', past.length ? [h('table', { class: 'stbl' }, [h('thead', null, [h('tr', null, ['Date', 'Client', 'Tank', ''].map(function (x) { return h('th', { text: x }); }))]), h('tbody', null, past.map(function (p) {
      var t = p.tankId && by(S.tanks, p.tankId);
      return h('tr', null, [h('td', { text: fmt(p.date) }), h('td', { text: clientName(p.clientId) }), h('td', { text: t ? t.name : '' }), h('td', { class: 'sact' }, [btn('Copy link', function () { clipboardLink(visitPayload(p), 'Report'); }, 'small'), btn('Open', function () { openLink(visitPayload(p)); }, 'small'), btn('Delete', function () { if (confirm('Delete this report?')) { S.visits = S.visits.filter(function (x) { return x !== p; }); save(); render(); } }, 'small danger')])]);
    }))])] : [h('p', { class: 'smuted', text: 'No reports yet.' })]));
    return wrap;
  }

  // ---------- invoices ----------
  function invoices() {
    var wrap = h('div');
    if (ui.invId && by(S.invoices, ui.invId)) return invoiceForm(by(S.invoices, ui.invId));
    wrap.appendChild(card('Invoices', [h('div', { class: 'sactions' }, [btn('+ New invoice', function () { if (!S.clients.length) { ui.msg = 'Add a client first.'; go('clients'); return; } var inv = newInvoice(ui.clientId || S.clients[0].id); ui.invId = inv.id; render(); }, 'primary')]),
      S.invoices.length ? h('table', { class: 'stbl' }, [h('thead', null, [h('tr', null, ['No.', 'Client', 'Date', 'Total', 'Status', ''].map(function (x) { return h('th', { text: x }); }))]), h('tbody', null, S.invoices.slice().sort(function (a, b) { return a.date < b.date ? 1 : (a.date > b.date ? -1 : (a.no < b.no ? 1 : -1)); }).map(function (i) {
        var late = i.status === 'sent' && i.due && i.due < todayS();
        return h('tr', null, [h('td', { text: i.no }), h('td', { text: clientName(i.clientId) }), h('td', { text: fmt(i.date) }), h('td', { text: money(invTotals(i).total) }), h('td', { text: late ? 'overdue' : i.status, class: late ? 'late' : '' }), h('td', null, [btn('Open', function () { ui.invId = i.id; render(); }, 'small')])]);
      }))]) : h('p', { class: 'smuted', text: 'No invoices yet.' })]));
    return wrap;
  }
  function invoiceForm(inv) {
    var f = h('div'), tot = h('div', { class: 'stot' });
    function recalc() { var t = invTotals(inv); tot.textContent = 'Subtotal ' + money(t.sub) + (t.tax ? '   Tax ' + money(t.tax) : '') + '   Total ' + money(t.total); }
    var cs = h('select'); S.clients.forEach(function (c) { cs.appendChild(h('option', { value: c.id, text: c.name })); }); cs.value = inv.clientId; cs.addEventListener('change', function () { inv.clientId = cs.value; save(); });
    var statusSel = h('select'); [['draft', 'Draft'], ['sent', 'Sent'], ['paid', 'Paid']].forEach(function (o) { statusSel.appendChild(h('option', { value: o[0], text: o[1] })); }); statusSel.value = inv.status;
    statusSel.addEventListener('change', function () { inv.status = statusSel.value; if (inv.status === 'paid' && !inv.paidDate) inv.paidDate = todayS(); save(); render(); });
    var c = card('Invoice ' + inv.no, [h('div', { class: 'sgrid' }, [field('Client', cs), field('Invoice no.', input(inv, 'no')), field('Date', input(inv, 'date', 'date')), field('Due', input(inv, 'due', 'date')), field('Status', statusSel), field('Tax rate (%)', (function () { var i = input(inv, 'taxRate', 'number', { step: '0.01', min: '0' }); i.addEventListener('change', recalc); return i; })())])]);
    var tb = h('tbody');
    function rows() {
      tb.innerHTML = '';
      inv.items.forEach(function (it) {
        var q = input(it, 'qty', 'number', { step: '0.25', min: '0' }), p = input(it, 'price', 'number', { step: '0.01', min: '0' });
        q.addEventListener('change', recalc); p.addEventListener('change', recalc);
        tb.appendChild(h('tr', null, [h('td', null, [input(it, 'desc')]), h('td', null, [q]), h('td', null, [p]), h('td', null, [btn('✕', function () { inv.items = inv.items.filter(function (x) { return x !== it; }); save(); rows(); recalc(); }, 'small')])]));
      });
    }
    rows();
    c.appendChild(h('div', { class: 'stbl-wrap' }, [h('table', { class: 'stbl items' }, [h('thead', null, [h('tr', null, ['Description', 'Qty', 'Price', ''].map(function (x) { return h('th', { text: x }); }))]), tb])]));
    c.appendChild(btn('+ Add line', function () { inv.items.push({ desc: '', qty: 1, price: 0 }); save(); rows(); }));
    c.appendChild(tot); recalc();
    c.appendChild(field('Notes (shown on the invoice)', textarea(inv, 'notes', 2)));
    c.appendChild(h('div', { class: 'sactions' }, [
      btn('Copy share link', function () { if (inv.status === 'draft') { inv.status = 'sent'; save(); } clipboardLink(invPayload(inv), 'Invoice'); }, 'primary'),
      btn('Open printable view', function () { openLink(invPayload(inv)); }),
      btn('Back to list', function () { ui.invId = null; render(); }),
      btn('Delete', function () { if (!confirm('Delete invoice ' + inv.no + '?')) return; S.invoices = S.invoices.filter(function (x) { return x !== inv; }); ui.invId = null; save(); render(); }, 'danger')]));
    c.appendChild(h('p', { class: 'smuted', text: 'Copying the link marks a draft as Sent. Your payment details come from Settings.' }));
    f.appendChild(c); return f;
  }

  // ---------- settings ----------
  function settings() {
    var b = S.biz, wrap = h('div');
    wrap.appendChild(card('Your business', [h('div', { class: 'sgrid' }, [field('Business name', input(b, 'name')), field('Contact name / address', input(b, 'contact')), field('Phone', input(b, 'phone', 'tel')), field('Email', input(b, 'email', 'email'))])]));
    wrap.appendChild(card('How clients pay', [h('p', { class: 'smuted', text: 'Shown on invoices. Leave blank what you do not use. These go in the invoice link, so only enter what you are happy to share.' }), h('div', { class: 'sgrid' }, [field('Venmo', input(b, 'venmo', 'text', { placeholder: '@yourname' })), field('PayPal', input(b, 'paypal')), field('Cash App', input(b, 'cashapp', 'text', { placeholder: '$yourname' })), field('Zelle', input(b, 'zelle'))])]));
    wrap.appendChild(card('Invoice defaults', [h('div', { class: 'sgrid' }, [field('Number prefix', input(b, 'prefix')), field('Next number', input(b, 'next', 'number', { min: '1' })), field('Days until due', input(b, 'dueDays', 'number', { min: '0' })), field('Default tax rate (%)', input(b, 'taxRate', 'number', { step: '0.01', min: '0' }))])]));
    var file = h('input', { type: 'file', accept: 'application/json,.json', class: 'sr-only', id: 'imp' });
    file.addEventListener('change', function () {
      var f = file.files[0]; if (!f) return; var r = new FileReader();
      r.onload = function () { try { var o = JSON.parse(r.result); if (!o || !Array.isArray(o.clients)) throw 0; if (!confirm('Replace everything in this browser with the backup (' + o.clients.length + ' clients)?')) return; var bl = blank(); S = Object.assign(bl, o, { biz: Object.assign(bl.biz, o.biz || {}) }); save(); ui.clientId = ui.tankId = ui.invId = null; ui.visit = null; ui.msg = 'Backup restored.'; render(); } catch (e) { alert('That file is not a toolkit backup.'); } };
      r.readAsText(f);
    });
    wrap.appendChild(card('Backup', [h('p', { text: 'Your data lives only in this browser. Download a backup after any busy day, and before clearing browser data or switching devices.' }), h('div', { class: 'sactions' }, [
      btn('Download backup', function () { var a = h('a', { href: URL.createObjectURL(new Blob([JSON.stringify(S, null, 1)], { type: 'application/json' })), download: 'service-toolkit-backup-' + todayS() + '.json' }); document.body.appendChild(a); a.click(); a.remove(); }, 'primary'),
      h('label', { class: 'sbtn', for: 'imp', tabindex: '0', text: 'Restore from backup' }), file,
      btn('Erase everything', function () { if (confirm('Erase all clients, tanks, reports and invoices from this browser? Download a backup first.') && confirm('This cannot be undone. Erase now?')) { S = blank(); save(); ui.clientId = ui.tankId = ui.invId = null; ui.visit = null; render(); } }, 'danger')])]));
    return wrap;
  }

  render();
  if (!storageOk) warn('This browser is blocking storage.');
  try { localStorage.setItem(KEY + '-t', '1'); localStorage.removeItem(KEY + '-t'); } catch (e) { warn('This browser is blocking storage, so changes will be lost when you close the page. Download a backup from Settings, or leave private browsing.'); }
})();
