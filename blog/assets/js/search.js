const searchInput = document.getElementById("search");
const searchResults = document.getElementById("search-results");

// Fetch the index and the content
fetch('/index.json')
  .then(response => response.json())
  .then(data => {
    const idx = lunr(function () {
      this.field('title');
      this.field('content');
      data.forEach(doc => {
        this.add(doc);
      });
    });

    // Handle the search
    searchInput.addEventListener('input', function () {
      const query = searchInput.value;
      const results = idx.search(query);
      searchResults.innerHTML = '';
      if (results.length > 0) {
        results.forEach(result => {
          const item = data.find(post => post.id === result.ref);
          searchResults.innerHTML += `<li><a href="${item.url}">${item.title}</a></li>`;
        });
      } else {
        searchResults.innerHTML = '<li>No results found</li>';
      }
    });
  });
