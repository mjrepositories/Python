//let, const (let variable can be assign again, const is constant
// in case of let i can just initialize the value, in case of const - value has to be assign at the beginning

//data types String, Numbers, Boolean,null

const name = 'John';
const age  = 30;
const rating = 4.5;
const isCool = true;
const x = null;
const y = undefined;
let z;
console.log(typeof y)

//concatenation
console.log('My name is ' + name)
//Template String
// To use template strings we have to use backticks (button for tylda)
console.log(`My name is well known ${name} and I am ${age}`);

const s = 'technology, computers, it, code';

console.log(s.toUpperCase())
console.log('Hello')
console.log(s.toLowerCase())
console.log(s.substring(0,5))

console.log(s.split(', '))

//comment
/*multi line
comment
*/

//arrays - variables for storing multiple values
// below new is a constructor
const numbers = new Array(1,2,3,4,5)
console.log(numbers)
//Even having const - we are able to assign additional values to array

const fruits = ['apples','oranges','pears']
fruits[3] = 'bananas'

//Arrays are indexed so we can type position in square brackets and access the value

fruits.push('mangos')
// push allows us to put the value at the end of the array
fruits.unshift('lemons')
//unshift allows us to put the value at the beginning of the array
console.log(fruits)

// accessing indexOf we can get info on the position of specific value in the array
// in our example we are getting 5 as mangos are fifth in the array
console.log(fruits.indexOf('mangos'))

// accessing isArray from Array class we can check if the value passed is indeed an array
console.log(Array.isArray(fruits))
console.log("Maciej")
  
//object literals (that can be treated similar as dictionaries in Python)
// we type in theses pairs as follows: variable is without quotes but if value is 
// a string then we have to put it in quotes
const   person = {
    firstName: "John",
    lastName: "Doe",
    age: 30,
    hobbies: ['music','movies','sports'],
    address:{
        street: "50 main st",
        city: 'Boston',
        state: "MA"
    }
}
// we can log multiple values
console.log(person.firstName,person.lastName)
// getting the hobby movies
console.log(person.hobbies[1])
// getting the city in address
console.log(person.address['city'])
console.log(person.address.city)

// there is an option to pull data from the object
const {firstName,lastName} = person

console.log(firstName)

// if we have an embeded object we can pull the values as below
const {address: {city}} = person

console.log(city)


person.email = 'john@gmail.com'

console.log(person.email)

const todos = [
    {
        id: 1,
        text: 'Take out trash',
        isCompleted: true
    },
    {
        id: 2,
        text: 'Meeting with boss',
        isCompleted: true
    },
    {
        id: 3,
        text: 'Dentist appointment',
        isCompleted: false
    }
]
console.log(todos)

console.log(todos[1].text)

//JSON
// If we would like to create a json object we can use function stringify
const todoJSON = JSON.stringify(todos)
console.log(todoJSON)

//FOR loops
// first thing is to declare the variable
// then after semicolon we are indicating the condition to be met
// finally, we are indicating what has to happen in each iteration
// such loop is done in curly braces
for(let i = 0; i<10; i++) {
    console.log(`For loop number ${i}`)
}

//WHILE Loops
// For this loop we are declaring the variable outside loop
let i  = 0

while(i<10){
console.log(`While loop number ${i}`)
i++
}

//Looping over arrays
for(let i = 0; i<todos.length; i++) {
    console.log(todos[i].text)
}
 
for(let todo of todos) {
    console.log(todo.id)
}

//HIgher order array methods

/*
forEach is just looping through arrays
map is allowing us to create a new array
filter is allowing us to create a new array based on the condition
*/

//Starting with forEach
// it takes as a parameter a function and it take the variable as each item
// So each time we go through the iteration loop is executing the function using the parameter
todos.forEach(function(todo){
    console.log(todo.text)
})

//map 
// it assings/creates the array
// the outcome of using map is that it creates an array using the parameter that was passed
// to the function
const todoText = todos.map(function(todo){
    return todo.text
})

console.log(todoText)

// filter
// by using filter we are able to create an array by having a condition that is met 
// during iteration
const todoCompleted = todos.filter(function(todo){
    return todo.isCompleted===true
})

console.log(todoCompleted)

// We are able to chaing loops
const todoCompletednew = todos.filter(function(todo){
    return todo.isCompleted===true
}).map(function(todo){
    return todo.text
})

console.log(todoCompletednew)

// Conditionals
const q = 10;
if(q == 10){
    console.log('q is 10')
} else if(q >10){
    console.log('greater than 10')
}
else{
    console.log('q is below 10')
}

// double = (so '==') is matching the value without checking the data type
// triple = (so "===") is matching the value and considering the data type as well

const a = 10;
const p = 10;
if(a> 5 || p > 10){
    console.log('a greater than 10 or p is greater than 10')
}

// double pipe line (so ||) is used for "OR" representation
// double ampersand (so &&) is used for "AND" representation

// we can type conditions in one line
// we type first condition, after that we have quotation mark representing "then"
// and as thirt option we could have colon ":" which is the represenation of "else"
const you = 14
const color = you >10 ? 'green' : 'blue'

console.log(color)

//switches - another way of evaluating conditions
// in switches we can type in the cases that we would like to verify
//we type what we would like to check in parenthesis
// and then we are typing the cases and the outcome of each case
// we can also declare default value
switch(color){
    case 'red':
        console.log('Color is red')
        break;
    case 'blue':
        console.log('Color is blue')
        break
    default:
        console.log('Color is not red or blue')
}

// functions
// in functions we can set default parameters
function addNums(num1 = 1,num2=2){
    console.log(num1+num2)
}

addNums()

function addNumsTwice(num1 = 1,num2=2){
    return num1+num2
}

console.log(addNumsTwice(3,3))


// arrow function
// this function is allowing us to cut down the number of code
// as we can se we were able to declare a function as a variable
// then we type in parameter 
// and after the arrow we indicated what the function shoul return
const addNumsArrow = num1 => num1 + 5
console.log(addNumsArrow(4))

// object oriented programming
//  constructor function
/*
HOW CREATING OF OBJECT WAS DONE PREVIOUSLY (BUT COULD BE STILL DONE THIS WAY)

function Person(firstName,lastName,birth){
    this.firstName = firstName;
    this.lastName = lastName;
    this.birth = new Date (birth)
}

// prototype
// by using prototype we can avoid having functions in all objects but just where we want it
Person.prototype.getBirthYear = function(){
    return this.birth.getFullYear()
}

Person.prototype.getFullName = function(){
    return `${this.firstName} ${this.lastName}`
}
*/



//CLASS creation
class Person{
    constructor(firstName,lastName,birth){
        this.firstName = firstName;
        this.lastName = lastName;
        this.birth = new Date (birth)   
    };
    getBirthYear(){
        return this.birth.getFullYear() 
    };
    getFullName(){
        return `${this.firstName} ${this.lastName}` 
    }

}











//instantiating object
const person1 = new Person('John','Doe','1993-01-01')
const person2 = new Person('Mary','Doe','1970-04-01')

console.log(person2)
console.log(person2.birth.getFullYear())
console.log(person1.getBirthYear())
console.log(person1.getFullName())

console.log(person1)


