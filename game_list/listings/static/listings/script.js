// let button_top = document.getElementById("top-button")

// window.onscroll = function() {top_button_function()};

// function top_button_function() {
//     if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
//         button_top.style.display = "block";
//       } else {
//         button_top.style.display = "none";
//       }
// }

// Get the button:
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  const backToTopBtn = document.getElementById("myBtn");
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    backToTopBtn.classList.add("show");
  } else {
    backToTopBtn.classList.remove("show");
  }
}