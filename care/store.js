(function () {
  try {
    var loc = new URLSearchParams(location.search).get('loc');
    if (loc) { var el = document.getElementById('store-' + loc); if (el) el.classList.add('is-here'); }
  } catch (e) {}
  var q = document.getElementById('care-q');
  if (!q) return;
  var items = [].slice.call(document.querySelectorAll('.care-grid li'));
  var groups = [].slice.call(document.querySelectorAll('.care-group'));
  var none = document.getElementById('care-none');
  q.addEventListener('input', function () {
    var t = q.value.trim().toLowerCase(), shown = 0;
    items.forEach(function (li) {
      var ok = !t || li.getAttribute('data-hay').indexOf(t) !== -1;
      li.hidden = !ok; if (ok) shown++;
    });
    groups.forEach(function (g) { g.hidden = !g.querySelector('li:not([hidden])'); });
    if (none) none.hidden = shown !== 0;
  });
})();
