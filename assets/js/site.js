(() => {
  const button = document.querySelector('[data-menu-toggle]');
  const navigation = document.getElementById('primary-nav');
  if (button && navigation) {
    button.addEventListener('click', () => {
      const expanded = button.getAttribute('aria-expanded') === 'true';
      button.setAttribute('aria-expanded', String(!expanded));
      button.textContent = expanded ? 'Menu' : 'Close';
      navigation.classList.toggle('open', !expanded);
    });
    navigation.addEventListener('click', event => {
      if (event.target.closest('a')) {
        button.setAttribute('aria-expanded','false');
        button.textContent = 'Menu';
        navigation.classList.remove('open');
      }
    });
  }
  const year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();
})();
