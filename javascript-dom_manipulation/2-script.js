const header = document.querySelector("header");
const redBtn = document.querySelector("#red_header");

redBtn.addEventListener("click", function () {
  header.classList.add("red");
});