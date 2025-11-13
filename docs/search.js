const idx = lunr(function(){
  this.ref('id'); this.field('title'); this.field('content');
  this.add({id:'intro', title:'Getting Started', content:'Install and initialize Alance SDK'});
  this.add({id:'api', title:'API Reference', content:'All SDK methods and classes'});
  this.add({id:'examples', title:'Examples', content:'Example projects and demos'});
});

const searchBox = document.getElementById('searchBox');
const resultsDiv = document.getElementById('searchResults');

searchBox.addEventListener('input', ()=>{
  const query = searchBox.value;
  const results = idx.search(query);
  resultsDiv.innerHTML = results.length
    ? results.map(r=>`<div><a href="${r.ref}.html">${r.ref}</a></div>`).join('')
    : '<div>No results found</div>';
});
