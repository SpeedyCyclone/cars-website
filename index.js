function changeBG() {
    document.getElementById("moon").src = "img/sun.png";
    document.getElementById("moon").onclick = function() {changebg()};
    document.body.style.background = "#790252";
    document.getElementById("nav").style.backgroundColor = "#4C0033";
    document.getElementById("name").style.color = "white";
    document.getElementById("hi").style.color = "#16213E";
    document.getElementById("showcase").style.backgroundColor = "#B25068";
    document.getElementById("showcase").style.color = "#D6D5A8";
}

function changebg() {
    document.getElementById("moon").src = "img/moon.png";
    document.getElementById("moon").onclick = function() {changeBG()};
    document.body.style.background = "#6200ee";
    document.getElementById("nav").style.backgroundColor = "#03dac5";
    document.getElementById("name").style.color = "#023020";
    document.getElementById("hi").style.color = "#16213E";
    document.getElementById("showcase").style.backgroundColor = "#bb86fc";
    document.getElementById("showcase").style.color = "black";
}