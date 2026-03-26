const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const character = document.querySelector('#character');

fetch(url)
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    character.textContent = data.name;
  })
  .catch(function (error) {
    console.error('Error:', error);
  });
