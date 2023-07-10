function responsiveMenu() {
    var x = document.querySelector(".navegador-inicio");
    if (x.className === "navegador-inicio") {
      x.className += " responsive";
    } else {
      x.className = "navegador-inicio";
    }
  }