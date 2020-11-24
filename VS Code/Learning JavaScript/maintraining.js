const employee = {
    age: 35,
    hobbies : ['painting','drawing','cycling'],
    langauages : ['python','javascript'],
    project : {
        python : ['air calculator','repair manager'],
        javascript : ['timer','counter']
    }
}

console.log(employee.project.javascript[1])

console.log(employee.project.python[1])

const zupa = 'pomidorowa jest super'

console.log(zupa.toLowerCase())

console.log(zupa.toUpperCase())
console.log(zupa.substring(0,6))

console.log(zupa.split(" "))

// this is just one line comment

/* but if i would like to keep it with more lines
then i have to use start and backslash
so let's end the comment here */

const moja_osoba = ['Maciej','Janowski',27,'Sukiennicza','Polska',188]
console.log(moja_osoba[4])

moja_osoba.push('Wolny')

console.log(moja_osoba)

moja_osoba.unshift('Pracownik')

console.log(moja_osoba)

// now we want to check what is the index of my age
console.log(moja_osoba.indexOf(27))

const worker ={
    name: "Maciej",
    lastname: "Janowski",
    age: 27,
    employer: 'Philips',
    home_office:true,
    favorite:['programming','cycling','cooking'],
    address:{
        city:'Lodz',
        street:'Sukiennicza',
        zipcode:'91855',
        near_streets:['Inflancka','Pojezierska','Rysownicza']xx
    }
}

console.log(worker.address.city)

console.log(worker.address.near_streets[1])

const {address:{near_streets}} = worker

console.log(near_streets)

const friends = [
    {
        name: 'Maciej',
        skill: 'baking',
        age: 27,
        isSmart: true
    },
    {
        name: 'Kamil',
        skill: 'negotiating',
        age: 33,
        isSmart: true
    },
    {
        name: 'Remysław',
        skill: 'managing',
        age: 35,
        isSmart: false
    },
    {
        name: 'Karolina',
        skill: 'singing',
        age: 22,
        isSmart: false
    }
]

console.log(friends[1])

const toJSON = JSON.stringify(friends)
console.log(toJSON)

// for loop - how it works?
for(let i=1;i<10;i++){
    console.log(i);
}

// so first is for word, then we have to type 3 arugments
// first is initiating variable, then how long the iteration works, finally - iteration increrment

for(let z=2; z < 5; z++) {
    console.log(`Myy age is ${z}`);
}

//while loop is created a little bit differently
// we declare the iteration variable outside loop

let k = 1

while(k<4){
console.log('lets go in '+ k);
k = k + 2
}

// so while loop is woroking this way:
/*We declare variable outside the loop
in while statement we declare how long the loop is going to work
then we are declaring what is going inside the loop
once that is done - we declare how variable is incremented
*/


// let's loop over arrays

for(let igrek= 0; igrek < friends.length; igrek++){
    console.log(friends[igrek].skill);
}

// let's create an array

training = ['bread','butter','ham','tomato','juice']
for(let iterator=0;iterator < training.length;iterator++){
    console.log(training[iterator].length);
}

// again explanation on how for loop works
/*
we state for and in parentheses we firstly initiate the iterator
then we have to declare how long the iterator will proceed
and as last - what we do with iterator after each loop
*/

//for while loop we pick the topic differently a little bit
//we declare variable outside loop
let it = 0

//then we create a loop declaring the rule of how long the loop will work
while(it<10){
    console.log(it);
    // and we need to add information what we do with the iterator in each loop
    it = it +2
}

// we can also loop in a different way
for(let done of training){
    console.log(done.length);
}

//in above case the loop works this way - we type for to initiate the loop
//and in parentheses we declare variable for looping indicadting by "of" that we will loop over
// some array we have declared previously

training.forEach(function(x){
    console.log(x);
})

// in case of map we can create a new array
example = ['Maciej','Aneta','Karolina','Wojciech']

const created = example.map(function(x){
    return x.substring(2,5)
})

console.log(created);

// let's now use filter to create an array with some condition

const created_filter = example.filter(function(x){
    return x.substring(2,5)==='jci'
})

console.log(created_filter);

// let's recap what we have learned on loops 
/*
using forEach we are looping over each element in the array
we have to declare function that is used in each iteration

in case of map - we are creating a new array
so we declare new variable then we use our array and type map
in map - we declare function that will be executed in each loo
*/

//conditions
const pi = 10
if(pi>10){
    console.log('wieksze od 10');
} else if(pi<5){
    console.log('pi jest mniejsze od 5');
} else{
    console.log('pi jest większe od 10');
}

// how to type conditions 
/* So we have to have variable for checking
then we type if and in parentheses we type what we want to check ()
then we use curly braces and type what we want to do if condition is met
we can then close curly braces and type else if and repeat the procedure
at the end - we can use else to check everything that was not verified previously
*/


//again let's go through methodology
const testing = 7
if(testing>10){
    console.log('testing wieksze od 11');
} else if(testing<5){
    console.log('testing mniejsze od 5');
} else{
    console.log('pozostała odpowiedź');
}

// equation
// double equal == is just checking if the values are the same on both ends
// triple equal is checking if the values are the same AND if datatype is the same as well

// we can also use some signs to represent if statement
const crosscheck = 10
const t = crosscheck > 10 ? 11 : 12  
console.log(t);

// let's check values having multiply ifs
function taking(value){
    return value >10 ? 'większe od 10'
    : value <2 ? "wartość mniejsza od 2"
    : value >2 && value <10 ? "wartośc miedzy 2 i 10"
    : 'nothing'
}

console.log(taking(11));

//SWITCHES baby!!! We can also check conditions using them

const coloring = 'yellow'
switch(coloring){
    case 'blue':
        console.log('the color is blue');
        break
    case 'purple':
        console.log('color is purple');
        break
    case 'yellow':
        console.log('yellow color lads');
        break
    default:
        console.log("don't know the color");
}


// so switches work this way
// we type switch and declare variable
// and then we state conditions


//writing functions
function mama(num1,num2){
    return num1*num2
}

console.log(mama(2,2));

// we can declare default values
function brzostek(num1, num2=8){
    return `brzostek ma ${num1*num2} metrow kwadratowych`
}

console.log(brzostek(2));

//arrow function

const macius = wiek => `Macius ma ${wiek} lat`

console.log(macius(19));

//creating classes in javascript

class bballer{
    constructor(name,nick,ppg,rpg,apg){
        this.name = name
        this.nick = nick
        this.ppg = ppg
        this.rpg = rpg
        this.apg = apg
    };
    getpointperminute(){
        return this.ppg / 48
    }
    getnaming(minutes){
        return `${this.nick} is plapying ${minutes} minutes and scoring ${this.ppg} points`
    }
}

lebron =new bballer('lebron','king james',30,11,12)

console.log(lebron.nick);

console.log(lebron.getpointperminute());

console.log(lebron.getnaming(36))


console.log(lebron)


//DOM

//window is the top object and we do not have to use it

console.log(window);

//single element selectors


const form = document.getElementById('my-form')

console.log(form);

// first selector that is used is getElementById

// second selectro is querySelector and it finds first element on the page

console.log(document.querySelector('h1'));

// mutliple element selectors
// it is returing NODElist on which we can use array methods
console.log(document.querySelectorAll('.item'));

// below we are assigning a node list to variable
const items = document.querySelectorAll('.item')
// and we are loop through each item passing an arrow fuction
// which indicates the variable passed so item and each item is printed
items.forEach(item => console.log(item))

const ul = document.querySelector('.items')

// ul.remove()

//ul.lastElementChild.remove()

//textContent is allowing us to chanage the content of the element. No matter if it is hidden or not
ul.firstElementChild.textContent = 'Maciej  zmienił'

// in case of innerText we can adjust the text that is in the element written
// innerText is only the text visible for us on the webpage
ul.children[1].innerText = 'Też zmienione'

//innerHTML is allowing us to add some HTML on the webpage
ul.lastElementChild.innerHTML ='<h1>Macius</h1>'

//using query selector we are able to indicate the element we want to use
const btn = document.querySelector('.btn')
btn.style.background = 'red'

// we can add functionalities based on event going on the screen

// below we are triggering changes on cursor being out of the button
// so when the cursor is out we are preventing default action which is submit for button
// we are changing the bacckground of form to brown
// we are adding class to body
// we are inserting inner html to last element having items class
// we are changing the color of last element to red
btn.addEventListener('mouseout',e => {
    e.preventDefault();
    document.querySelector('#my-form').style.background = 'brown'
    document.querySelector('body').classList.add('bg-dark')
    document.querySelector('.items').lastElementChild.innerHTML = '<h1>Helloooo</h1>'
    document.querySelector('.items').lastElementChild.style.background  = 'red'
})


// below we are triggering changes on curson being on the button
// when cursor is on the button
// we are preventing default action which is submit for the button
// we are changing the background of form to green
// we are giving body class 
// we are giving last element of items class inner html
//we are setting the background for last element of items class to green

btn.addEventListener('mouseover',e => {
    e.preventDefault();
    document.querySelector('#my-form').style.background = 'green'
    document.querySelector('body').classList.add('bg-dark')
    document.querySelector('.items').lastElementChild.innerHTML = '<h1>Spadaj</h1>'
    document.querySelector('.items').lastElementChild.style.background  = 'green'
})


// let's make it functional
// we created variables indicating my-form id, name id, email and users, as well as msg class
const myForm = document.querySelector('#my-form')
const nameInput = document.querySelector('#name')
const emailInput = document.querySelector('#email')
const msg = document.querySelector('.msg')
const userList = document.querySelector('#users')

// we have added an event when myform will influence the set-up on page
// function is onSubmit
myForm.addEventListener('submit',onSubmit);

// We created function onSubmit which is preventing standard behaviour of button
function onSubmit(e){
    e.preventDefault();
    // and is checking the values on nameInput as well as emailInput
    if(nameInput.value === ''|| emailInput.value === ''){
        // we are adding a class of error to msg element

        msg.classList.add('error');
        msg.innerHTML='Please enter all fields';
        setTimeout(() =>  msg.remove(),3000)
    } else {
        const li = document.createElement('li');
        li.appendChild(document.createTextNode(`${nameInput.value}; ${emailInput.value}`))
        userList.appendChild(li)

        // clearing the fields
        nameInput.value = ''
        emailInput.value = ''
    }
}


const realFileBtn = document.getElementById('real-file');
const customBtn = document.getElementById('custom-button');
const customText = document.getElementById('custom-text');

customBtn.addEventListener('click',function(){
    realFileBtn.click();
})

realFileBtn.addEventListener('change',function(){
    if (realFileBtn.value){
        customText.innerHTML = realFileBtn.value.split('\\')[realFileBtn.value.split('\\').length-1];
    }
    else {
        customText.innerHTML =  'No chosen'
    }
})
