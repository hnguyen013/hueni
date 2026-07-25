/**
 * Task 5.2 — Toggle menu hamburger trên mobile.
 * JS thuần, chỉ đọc/ghi 2 phần tử #nav-toggle và #mobile-menu trong
 * templates/partials/navbar.html. Dùng đúng pattern hidden/flex đã thống
 * nhất trong project (JS chỉ remove/add class 'hidden').
 */
(function () {
  var toggle = document.getElementById('nav-toggle');
  var menu = document.getElementById('mobile-menu');

  if (!toggle || !menu) {
    return;
  }

  var icon = toggle.querySelector('.material-symbols-outlined');

  function isOpen() {
    return toggle.getAttribute('aria-expanded') === 'true';
  }

  function openMenu() {
    menu.classList.remove('hidden');
    toggle.setAttribute('aria-expanded', 'true');
    toggle.setAttribute('aria-label', 'Đóng menu');
    if (icon) {
      icon.textContent = 'close';
    }
  }

  function closeMenu() {
    menu.classList.add('hidden');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', 'Mở menu');
    if (icon) {
      icon.textContent = 'menu';
    }
  }

  toggle.addEventListener('click', function () {
    if (isOpen()) {
      closeMenu();
    } else {
      openMenu();
    }
  });

  // Bấm 1 link trong menu mobile thì tự đóng lại.
  menu.querySelectorAll('a').forEach(function (link) {
    link.addEventListener('click', closeMenu);
  });

  // Nếu người dùng xoay ngang / resize sang desktop, đảm bảo panel
  // luôn đóng (tránh kẹt trạng thái mở khi md:hidden không còn tác dụng ẩn).
  window.addEventListener('resize', function () {
    if (window.innerWidth >= 768 && isOpen()) {
      closeMenu();
    }
  });
})();
