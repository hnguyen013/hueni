/**
 * Gallery lightbox (Task 3.7) — JS thuần, không thư viện ngoài.
 * Tự chứa hoàn toàn, không phụ thuộc quiz_demo.js hay digital_map.js.
 *
 * Cấu trúc DOM mong đợi (xem templates/showcase/_gallery.html):
 *   [data-gallery-root]            (1 khối cho mỗi Gallery)
 *     .gallery-thumb[data-src][data-caption]
 *   [data-gallery-lightbox]        (modal dùng chung cho cả trang)
 *     [data-gallery-image]
 *     [data-gallery-caption]
 *     [data-gallery-close] / [data-gallery-prev] / [data-gallery-next]
 */
(function () {
  'use strict';

  var lightbox = document.querySelector('[data-gallery-lightbox]');
  if (!lightbox) return;

  var imgEl = lightbox.querySelector('[data-gallery-image]');
  var captionEl = lightbox.querySelector('[data-gallery-caption]');
  var closeBtn = lightbox.querySelector('[data-gallery-close]');
  var prevBtn = lightbox.querySelector('[data-gallery-prev]');
  var nextBtn = lightbox.querySelector('[data-gallery-next]');

  var currentThumbs = [];
  var currentIndex = 0;

  function render() {
    var thumb = currentThumbs[currentIndex];
    if (!thumb || !imgEl) return;
    imgEl.src = thumb.dataset.src;
    imgEl.alt = thumb.dataset.caption || '';
    if (captionEl) captionEl.textContent = thumb.dataset.caption || '';
  }

  function open(thumbs, index) {
    currentThumbs = thumbs;
    currentIndex = index;
    render();
    lightbox.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
  }

  function close() {
    lightbox.classList.add('hidden');
    if (imgEl) imgEl.src = '';
    document.body.style.overflow = '';
  }

  function showPrev() {
    if (!currentThumbs.length) return;
    currentIndex = (currentIndex - 1 + currentThumbs.length) % currentThumbs.length;
    render();
  }

  function showNext() {
    if (!currentThumbs.length) return;
    currentIndex = (currentIndex + 1) % currentThumbs.length;
    render();
  }

  document.querySelectorAll('[data-gallery-root]').forEach(function (root) {
    var thumbs = Array.prototype.slice.call(root.querySelectorAll('.gallery-thumb'));
    thumbs.forEach(function (thumb, index) {
      thumb.addEventListener('click', function () {
        open(thumbs, index);
      });
    });
  });

  if (closeBtn) closeBtn.addEventListener('click', close);
  if (prevBtn) prevBtn.addEventListener('click', showPrev);
  if (nextBtn) nextBtn.addEventListener('click', showNext);

  lightbox.addEventListener('click', function (e) {
    if (e.target === lightbox) close();
  });

  document.addEventListener('keydown', function (e) {
    if (lightbox.classList.contains('hidden')) return;
    if (e.key === 'Escape') close();
    if (e.key === 'ArrowLeft') showPrev();
    if (e.key === 'ArrowRight') showNext();
  });
})();
