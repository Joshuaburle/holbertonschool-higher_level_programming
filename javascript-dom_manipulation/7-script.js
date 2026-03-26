const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
const list = document.querySelector('#list_movies');

fetch(url)
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    data.results.forEach(function (movie) {
      const li = document.createElement('li');
      li.textContent = movie.title;
      list.appendChild(li);
    });
  })
  .catch(function (error) {
    console.error('Error:', error);
  });
