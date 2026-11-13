// Before/after slider
document.querySelectorAll('[data-ba]').forEach(function (ba) {
  var r = ba.querySelector('.ba-range');
  var set = function () { ba.style.setProperty('--pos', r.value + '%'); };
  r.addEventListener('input', set); set();
});

// Privacy-friendly YouTube: poster + play button, iframe loads on click.
document.querySelectorAll('[data-yt]').forEach(function (box) {
  var btn = box.querySelector('.yt-lite-btn');
  if (!btn) return;
  btn.addEventListener('click', function () {
    var id = box.getAttribute('data-yt');
    var title = box.getAttribute('data-yt-title') || 'YouTube video';
    var iframe = document.createElement('iframe');
    iframe.src = 'https://www.youtube-nocookie.com/embed/' + encodeURIComponent(id) + '?autoplay=1';
    iframe.title = title;
    iframe.setAttribute('allow', 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; fullscreen');
    iframe.setAttribute('allowfullscreen', '');
    iframe.setAttribute('referrerpolicy', 'strict-origin-when-cross-origin');
    box.classList.add('is-playing');
    box.innerHTML = '';
    box.appendChild(iframe);
  });
});
