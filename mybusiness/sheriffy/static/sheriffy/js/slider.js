 var slideIndex = 1;
showDivs(slideIndex);

function plusDivs(n) {
  showDivs(slideIndex += n);
}

function showDivs(n) {
  var i;
  var x = document.getElementsByClassName("mySlides");
  if (n > x.length) {slideIndex = 1}
  if (n < 1) {slideIndex = x.length} ;
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  x[slideIndex-1].style.display = "block";
}

//let tag = document.getElementById('naming')
//
//let btn = document.getElementById('item_naming')
//
//let tag_text = tag.innerText
//
//btn.addEventListener('mouseover',e=>{
//tag.innerHTML = 'Check offer';
//})
//
//btn.addEventListener('mouseout',e=>{
//tag.innerHTML = tag_text
//})


// 37 is left
// 39 is right

let but_back = document.getElementById('button_back')
let but_next = document.getElementById('button_next')

let doc = document.body

doc.addEventListener("keyup", function(event) {
  if (event.keyCode === 37) {
   event.preventDefault();
   document.getElementById("button_back").click();
  }
});

doc.addEventListener("keyup", function(event) {
  if (event.keyCode === 39) {
   event.preventDefault();
   document.getElementById("button_next").click();
  }
});

