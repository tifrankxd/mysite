const darkModeToggle = document.getElementById('darkModeToggle');

darkModeToggle.addEventListener('change', (event) => {
  if (event.target.checked) {
    // Apply dark mode styles
    document.body.classList.add('dark-mode');
  } else {
    // Remove dark mode styles
    document.body.classList.remove('dark-mode');
  }
});
