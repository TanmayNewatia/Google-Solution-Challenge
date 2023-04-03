function icon(anchor) {
  anchor.classList.toggle("fa-sun");
  anchor.classList.toggle("fa-moon");
  var element = document.getElementsByClassName("dark");
  for(let i=0;i<element.length;i++){
      element[i].classList.toggle("dark-mode");
  }
}

function su() {
    var signin = document.getElementById("signincard");
    var signup = document.getElementById("signupcard");
    var sut = document.getElementById("sut");
    var sit = document.getElementById("sit");
    var i=sit.querySelector("span");
    var u=sut.querySelector("span");
    signin.classList.remove("show");
    i.classList.remove("act");
    signin.classList.add("collapse");
    signup.classList.add("show");
    u.classList.add("act");
  }
  
  function si() {
    var signin = document.getElementById("signincard");
    var signup = document.getElementById("signupcard");
    var sut = document.getElementById("sut");
    var sit = document.getElementById("sit");
    var i=sit.querySelector("span");
    var u=sut.querySelector("span")
    signup.classList.remove("show");
    u.classList.remove("act");
    signin.classList.add("show");
    i.classList.add("act");
  }

  function renderuserlogo() {
    var user = document.getElementById("user");
    user.classList.toggle("fa-right-to-bracket");
    user.classList.toggle("fa-user");
  }