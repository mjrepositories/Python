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
//unshft allows us to put the value at the beginning of the array
console.log(fruits)

// accessing indexOf we can get info on the position of specific value in the array
// in our example we are getting 5 as mangos are fifth in the array
console.log(fruits.indexOf('mangos'))

// accessing isArray from Array class we can check if the value passed is indeed an array
console.log(Array.isArray(fruits))
console.log