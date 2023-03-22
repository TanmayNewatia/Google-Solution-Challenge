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