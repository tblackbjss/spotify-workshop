document.addEventListener('DOMContentLoaded', function() {
  const toggleSearchButton = document.getElementById('toggle_search_button');
  const searchBox = document.getElementById('search_box');

  toggleSearchButton.addEventListener('click', function() {
    if (searchBox.style.display === 'none') {
      searchBox.style.display = 'block';
    } else {
      searchBox.style.display = 'none';
    }
  });
});
