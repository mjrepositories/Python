}


function myFunction() {
    var x = document.getElementById("id1").value;
    if (x == "Other") {document.getElementById("id2").style.display = "block";document.getElementById('id2').value = '';}
    else {document.getElementById("id2").style.display = "none"}
}