// scrolling to top of table smoothly
function topFunction() {
  document.getElementById("shipmentTable").scrollTo({
  top: 0,
  left: 0,
  behavior: 'smooth'
});

}
// scrolling to the middle of the table smoothly
function midFunction() {
   document.getElementById("shipmentTable").scrollTo({
  top: document.getElementById("body_table").offsetHeight/2,
  left: 0,
  behavior: 'smooth'
});

}

// scrolling to the end of the table smoothly
function endFunction() {
  document.getElementById("shipmentTable").scrollTo({
  top: document.getElementById("body_table").offsetHeight,
  left: 0,
  behavior: 'smooth'
});
}