// Ollama Home Server Guide — minor enhancements
document.addEventListener('DOMContentLoaded', function () {
  // Highlight the current page in the nav
  var path = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.site-nav a').forEach(function (link) {
    if (link.getAttribute('href') === path) {
      link.classList.add('active');
    }
  });
  // Print shortcut hint
  if (window.matchMedia && window.matchMedia('print').matches) return;
  var hint = document.createElement('p');
  hint.className = 'print-hint';
  hint.style.cssText = 'font-size:0.8rem;color:#6b7280;text-align:center;margin-top:8px;';
  hint.textContent = 'Tip: use your browser Print command for a printable checklist.';
  var checklist = document.querySelector('.page ul.tasks');
  if (checklist) checklist.after(hint);
});
