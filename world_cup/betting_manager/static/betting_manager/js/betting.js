function selectGoalsOne(){
// finding element
    let select_goal_one = document.getElementById('goals_team_one');
    // getting value of the element
    x = select_goal_one.selectedIndex;
    // getting elements
    form_one = document.getElementById('id_goals_team_one');
    form_two = document.getElementById('id_goals_team_two');
    // assigning value to an element
    form_one.value = x
    // setting variable based on element value
    form_one_value = form_one.value
    form_two_value = form_two.value
    //finding elements
    let score_team_one = document.getElementById('id_score_team_one')
    let score_team_two = document.getElementById('id_score_team_two')
    // if value of 1 element is higher than 2
    if(form_one_value>form_two_value){
    // assign proper values to elements
    score_team_one.value = 'WIN';
    score_team_two.value = 'DEFEAT';
    document.getElementById('penalties_team_one').value =0
    document.getElementById('penalties_team_two').value =0
    }
    // if value for element 1 is lower than for element 2
    else if(form_one_value<form_two_value){
    // assing proper values for elements
        score_team_two.value = 'WIN';
        score_team_one.value = 'DEFEAT';
        document.getElementById('penalties_team_one').value =0
    document.getElementById('penalties_team_two').value =0
    }
    else{
    //else = assign values for elements
    score_team_two.value = 'DRAW';
    score_team_one.value = 'DRAW';
    }
}

function selectGoalsTwo(){
// finding element
    let select_goal_two = document.getElementById('goals_team_two');
    // getting value of the element
    x = select_goal_two.selectedIndex;
    // getting elements
    form_two = document.getElementById('id_goals_team_two');
    form_one = document.getElementById('id_goals_team_one');
    //assigning value to an element
    form_two.value = x
    // setting variable based on element value
    form_one_value = form_one.value
    form_two_value = form_two.value
    //finding elements
    let score_team_one = document.getElementById('id_score_team_one')
    let score_team_two = document.getElementById('id_score_team_two')
    // if value of 1 element is higher than 2
    if(form_one_value>form_two_value){
    // assign proper values for elements
    score_team_one.value = 'WIN';
    score_team_two.value = 'DEFEAT';
    document.getElementById('penalties_team_one').value =0
    document.getElementById('penalties_team_two').value =0
    }
    // if value of 1 is lower than 2
    else if(form_one_value<form_two_value){
    // assign proper values for elements
        score_team_two.value = 'WIN';
        score_team_one.value = 'DEFEAT';
        document.getElementById('penalties_team_one').value =0
    document.getElementById('penalties_team_two').value =0
    }
    else{
    // else - assign values for elements
    score_team_two.value = 'DRAW';
    score_team_one.value = 'DRAW';
    }
}

function selectPenaltiesOne() {
// find element
    let select_penalties_one = document.getElementById('penalties_team_one');
    // get value of element
    x = select_penalties_one.selectedIndex;
    // create elements
    form_one = document.getElementById('id_penalties_team_one');
    form_two = document.getElementById('id_penalties_team_two');
    // assign value to element
    form_one.value = x
    // create variables based on value of elements
    form_one_value = form_one.value
    form_two_value = form_two.value
    // find elements
    let score_team_one = document.getElementById('id_score_team_one')
    let score_team_two = document.getElementById('id_score_team_two')
    // if value of 1 is higher than 2
    if(form_one_value>form_two_value){
    // assign values
    score_team_one.value = 'WIN';
    score_team_two.value = 'DEFEAT';
    }
    // if value of 1 is lower than 2
    else if(form_one_value<form_two_value){
    // assign values
        score_team_two.value = 'WIN';
        score_team_one.value = 'DEFEAT';
    }
    // else - assign values
    else{
    score_team_two.value = 'DRAW';
    score_team_one.value = 'DRAW';
    }
}




function selectPenaltiesTwo() {
    // find element
    let select_penalties_two = document.getElementById('penalties_team_two');
    // get value of an element
    x = select_penalties_two.selectedIndex;
    // find elements
    form_two = document.getElementById('id_penalties_team_two');
    form_one = document.getElementById('id_penalties_team_one');
    // get value of an element
    form_two.value = x
    // create variables based on elements values
    form_one_value = form_one.value
    form_two_value = form_two.value
    // find elements
    let score_team_one = document.getElementById('id_score_team_one')
    let score_team_two = document.getElementById('id_score_team_two')
    // if value for 1 is higher than 2
    if(form_one_value>form_two_value){
    // assign values
    score_team_one.value = 'WIN';
    score_team_two.value = 'DEFEAT';
    }
    // if value for 1 is lower than 2
    else if(form_one_value<form_two_value){
    // assign values
        score_team_two.value = 'WIN';
        score_team_one.value = 'DEFEAT';
    }
    // else - assign values
    else{
    score_team_two.value = 'DRAW';
    score_team_one.value = 'DRAW';
    }
}

function loading() {
// find elements
let select_goal_one_select = document.getElementById('goals_team_one');
let select_goal_two_select = document.getElementById('goals_team_two');

let score_team_one_bet = document.getElementById('id_goals_team_one');
let score_team_two_bet = document.getElementById('id_goals_team_two');

// assign values to elements
select_goal_one_select.value = score_team_one_bet.value;
select_goal_two_select.value = score_team_two_bet.value;
}


function loadingPenalties() {
//find elements
let select_penalties_one_select = document.getElementById('penalties_team_one');
let select_penalties_two_select = document.getElementById('penalties_team_two');

let penalties_team_one_bet = document.getElementById('id_penalties_team_one');
let penalties_team_two_bet = document.getElementById('id_penalties_team_two');
// assign values to elements
select_penalties_one_select.value = penalties_team_one_bet.value;
select_penalties_two_select.value = penalties_team_two_bet.value;
}

// get href of a website
let website = document.location.href

// if href contains string - add two events listeners
if(!website.includes('GROUP')){
    window.addEventListener('load', loading);
    window.addEventListener('load', loadingPenalties);
}
// else - add one event listener
else{
    window.addEventListener('load', loading);
}