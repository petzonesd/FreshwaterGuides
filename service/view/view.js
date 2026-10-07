(function () {
  'use strict';
  var doc = document.getElementById('doc');
  function h(tag, cls, text) { var n = document.createElement(tag); if (cls) n.className = cls; if (text != null) n.textContent = text; return n; }
  function add(p) { for (var i = 1; i < arguments.length; i++) if (arguments[i]) p.appendChild(arguments[i]); return p; }
  function money(n) { return '$' + (Math.round(n * 100) / 100).toFixed(2); }
  function fmtDate(s) { if (!s) return ''; var d = new Date(s + 'T12:00:00'); return isNaN(d) ? s : d.toLocaleDateString(undefined, { year: 'numeric', month: 'long', day: 'numeric' }); }

  function header(biz, title, sub) {
    var hd = h('header', 'dh');
    var left = h('div'); add(left, h('div', 'biz', biz.name || 'Aquarium service'), biz.contact ? h('div', 'small', biz.contact) : null,
      (biz.phone || biz.email) ? h('div', 'small', [biz.phone, biz.email].filter(Boolean).join(' · ')) : null);
    var right = h('div', 'rt'); add(right, h('h1', null, title), sub ? h('div', 'small', sub) : null);
    return add(hd, left, right);
  }
  function table(cols, rows, cls) {
    var t = h('table', cls || 'tbl'), th = h('tr'); cols.forEach(function (c) { th.appendChild(h('th', null, c)); });
    var thead = h('thead'); thead.appendChild(th); t.appendChild(thead);
    var tb = h('tbody'); rows.forEach(function (r) { var tr = h('tr'); r.forEach(function (c, i) { var td = h('td', i && /^\$|^[0-9.]+$/.test(String(c)) ? 'num' : null, c); tr.appendChild(td); }); tb.appendChild(tr); });
    t.appendChild(tb); return t;
  }

  function report(d) {
    var b = d.biz || {};
    doc.innerHTML = '';
    add(doc, header(b, 'Service visit report', fmtDate(d.date)));
    var meta = h('div', 'meta');
    add(meta, h('div', null, 'Client: ' + (d.client || '')));
    if (d.tank) meta.appendChild(h('div', null, 'Tank: ' + d.tank + (d.gallons ? ' (' + d.gallons + ' gal)' : '')));
    doc.appendChild(meta);
    if (d.done && d.done.length) { doc.appendChild(h('h2', null, 'Work completed')); var ul = h('ul'); d.done.forEach(function (x) { ul.appendChild(h('li', null, x)); }); doc.appendChild(ul); }
    if (d.tests && Object.keys(d.tests).length) {
      doc.appendChild(h('h2', null, 'Water test results'));
      var labels = { temp: 'Temperature (°F)', ph: 'pH', ammonia: 'Ammonia (ppm)', nitrite: 'Nitrite (ppm)', nitrate: 'Nitrate (ppm)', gh: 'GH', kh: 'KH' };
      doc.appendChild(table(['Test', 'Reading'], Object.keys(labels).filter(function (k) { return d.tests[k] !== undefined && d.tests[k] !== ''; }).map(function (k) { return [labels[k], String(d.tests[k])]; })));
    }
    if (d.work) { doc.appendChild(h('h2', null, 'Notes on the visit')); doc.appendChild(h('p', 'pre', d.work)); }
    if (d.notes) { doc.appendChild(h('h2', null, 'Recommendations')); doc.appendChild(h('p', 'pre', d.notes)); }
    if (d.next) { doc.appendChild(h('p', 'next', 'Next visit: ' + fmtDate(d.next))); }
    document.title = 'Service report - ' + (d.client || '') + ' - ' + (d.date || '');
  }

  function invoice(d) {
    var b = d.biz || {};
    doc.innerHTML = '';
    add(doc, header(b, 'Invoice ' + (d.no || ''), d.status === 'paid' ? 'PAID' + (d.paidDate ? ' ' + fmtDate(d.paidDate) : '') : null));
    var meta = h('div', 'meta two'); var l = h('div'), r = h('div');
    add(l, h('div', 'lbl', 'Bill to'), h('div', 'strong', d.client || ''), d.clientContact ? h('div', 'small', d.clientContact) : null);
    add(r, h('div', null, 'Invoice date: ' + fmtDate(d.date)), d.due ? h('div', null, 'Due: ' + fmtDate(d.due)) : null);
    add(meta, l, r); doc.appendChild(meta);
    var sub = 0, rows = (d.items || []).map(function (i) { var amt = (Number(i.qty) || 0) * (Number(i.price) || 0); sub += amt; return [i.desc || '', String(Number(i.qty) || 0), money(Number(i.price) || 0), money(amt)]; });
    doc.appendChild(table(['Description', 'Qty', 'Price', 'Amount'], rows, 'tbl items'));
    var tax = sub * (Number(d.taxRate) || 0) / 100, tot = sub + tax;
    var tt = h('div', 'totals'); add(tt, h('div', null, 'Subtotal ' + money(sub)));
    if (tax) tt.appendChild(h('div', null, 'Tax (' + d.taxRate + '%) ' + money(tax)));
    tt.appendChild(h('div', 'grand', (d.status === 'paid' ? 'Total paid ' : 'Total due ') + money(tot)));
    doc.appendChild(tt);
    if (d.status !== 'paid') {
      var pay = []; if (b.venmo) pay.push('Venmo: ' + b.venmo); if (b.paypal) pay.push('PayPal: ' + b.paypal); if (b.cashapp) pay.push('Cash App: ' + b.cashapp); if (b.zelle) pay.push('Zelle: ' + b.zelle);
      if (pay.length) { doc.appendChild(h('h2', null, 'How to pay')); var ul = h('ul'); pay.forEach(function (p) { ul.appendChild(h('li', null, p)); }); doc.appendChild(ul); }
    }
    if (d.notes) { doc.appendChild(h('h2', null, 'Notes')); doc.appendChild(h('p', 'pre', d.notes)); }
    document.title = 'Invoice ' + (d.no || '') + ' - ' + (b.name || '');
  }

  function init() {
    document.getElementById('print').addEventListener('click', function () { window.print(); });
    var token = location.hash.replace(/^#/, '');
    if (!token) { doc.textContent = 'This link has no report or invoice in it.'; return; }
    FWGShare.decode(token).then(function (d) { if (d.t === 'invoice') invoice(d); else report(d); })
      .catch(function () { doc.textContent = 'This link could not be read. It may have been cut off when copied; ask the sender to share it again.'; });
  }
  init();
})();
