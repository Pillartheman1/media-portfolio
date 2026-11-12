// Before/after slider
document.querySelectorAll('[data-ba]').forEach(function (ba) {
  var r = ba.querySelector('.ba-range');
  var set = function () { ba.style.setProperty('--pos', r.value + '%'); };
  r.addEventListener('input', set); set();
});
