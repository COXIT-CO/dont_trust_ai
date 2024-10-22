document.addEventListener("DOMContentLoaded", function() {
    let indexData;

    // Fetch the index.json file
    fetch("/index.json")
        .then(response => response.json())
        .then(data => {
            indexData = data;
        });

    // Listen for input changes in the search box
    document.getElementById('search-input').addEventListener('input', function(event) {
        let query = event.target.value.toLowerCase();
        let results = search(query);
        displayResults(results);
    });

    // Search through the index
    function search(query) {
        return indexData.filter(page => {
            return page.title.toLowerCase().includes(query) || page.content.toLowerCase().includes(query);
        });
    }

    // Display the results
    function displayResults(results) {
        let resultsContainer = document.getElementById('search-results');
        resultsContainer.innerHTML = '';  // Clear previous results

        results.forEach(result => {
            let li = document.createElement('li');
            let a = document.createElement('a');
            a.href = result.link;
            a.textContent = result.title;
            li.appendChild(a);
            resultsContainer.appendChild(li);
        });
    }
});
