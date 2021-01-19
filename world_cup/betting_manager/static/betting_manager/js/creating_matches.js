

function matchesCreation() {
// getting value of an element
    let stage = document.getElementById('stage').value;
// finding elements
    let sixteen = document.getElementById('matches_wrapper_1');
    let eight = document.getElementById('matches_wrapper_2');
    let four = document.getElementById('matches_wrapper_3');
    let final = document.getElementById('matches_wrapper_4');
// assigning styles based on the value of dropdown selection
    if (stage=='sixteen') {
        sixteen.style.display = "block";
        eight.style.display = "none";
        four.style.display = "none";
        final.style.display = "none";
        }
    else if(stage=='eight'){
        sixteen.style.display = "none";
        eight.style.display = "block";
        four.style.display = "none";
        final.style.display = "none";
        }
    else if(stage=='four'){
        sixteen.style.display = "none";
        eight.style.display = "none";
        four.style.display = "block";
        final.style.display = "none";
        }
    else{
        sixteen.style.display = "none";
        eight.style.display = "none";
        four.style.display = "none";
        final.style.display = "block";
    }
}