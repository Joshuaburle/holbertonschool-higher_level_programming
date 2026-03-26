const url = "https://hellosalut.stefanbohacek.com/?lang=fr";

fetch(url)
    .then(response => response.json())
    .then(data => {
        const helloDiv = document.querySelector("#hello");
        helloDiv.textContent = data.hello;
    })
    .catch(error => {
        console.error("Erreur :", error);
    });
