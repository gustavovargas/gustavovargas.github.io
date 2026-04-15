(function () {
	'use strict';

	var toggle = document.querySelector('.js-colorlib-nav-toggle');
	var body = document.body;
	var aside = document.getElementById('colorlib-aside');

	function closeMenu() {
		if (!body.classList.contains('offcanvas')) return;
		body.classList.remove('offcanvas');
		if (toggle) {
			toggle.classList.remove('active');
			toggle.setAttribute('aria-expanded', 'false');
			toggle.setAttribute('aria-label', 'Abrir menú');
		}
	}

	if (toggle) {
		toggle.addEventListener('click', function (e) {
			e.preventDefault();
			var isOpen = body.classList.toggle('offcanvas');
			toggle.classList.toggle('active', isOpen);
			toggle.setAttribute('aria-expanded', String(isOpen));
			toggle.setAttribute('aria-label', isOpen ? 'Cerrar menú' : 'Abrir menú');
		});
	}

	document.addEventListener('click', function (e) {
		if (!body.classList.contains('offcanvas')) return;
		if (aside && aside.contains(e.target)) return;
		if (toggle && toggle.contains(e.target)) return;
		closeMenu();
	});

	document.addEventListener('keydown', function (e) {
		if (e.key === 'Escape') closeMenu();
	});

	window.addEventListener('scroll', closeMenu, { passive: true });
})();
