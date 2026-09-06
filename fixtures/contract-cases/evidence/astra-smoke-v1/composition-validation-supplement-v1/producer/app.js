const names = {pocket: 'Pocket Audio Kit', interview: 'Interview Kit', room: 'Room Recording Kit'};
let selectedKit = null;
for (const button of document.querySelectorAll('[data-select]')) {
  button.addEventListener('click', () => {
    selectedKit = button.dataset.select;
    for (const other of document.querySelectorAll('[data-select]')) {
      const selected = other.dataset.select === selectedKit;
      other.setAttribute('aria-pressed', String(selected));
      other.closest('[data-kit]').classList.toggle('is-selected', selected);
    }
    document.getElementById('selection-output').textContent = `${names[selectedKit]} selected. Local preview only — no reservation made.`;
  });
}
