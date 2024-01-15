---
dg-publish: true
tags: 
created: ""
---
>[!summary]- Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```

# Javascript

## Promises (todo)
## Closures
- Defining a function inside another function
- The inner function can access variables declared inside the outer function
- This means you can share values between function calls without making them global

```js
function makeCounter() {
  let counter = 0;  
  return () => {
	  counter += 1; 
	  return counter;
  };
}
const count = makeCounter();

count();
count();
count();
//3

const counter = (function () {
  let privateCounter = 0;
  function changeBy(val) {
    privateCounter += val;
  }

  return {
    increment() {
      changeBy(1);
    },

    decrement() {
      changeBy(-1);
    },

    value() {
      return privateCounter;
    },
  };
})();

console.log(counter.value()); // 0.

counter.increment();
counter.increment();
console.log(counter.value()); // 2.

counter.decrement();
console.log(counter.value()); // 1.


```

### Closures vs Classes, when to use which
- Do you (possibly in the future) need multiple methods? 
- Do you encapsulate state? 
- Then use a `class` to create objects. Do you only need a function to call? Then create a closure.

## Maps and Sets

```js
const fruits = new Map([  
  ["apples", 500],  
  ["bananas", 300],  
  ["oranges", 200]  
]);

const letters = new Set(["a","b","c"]);

fruits.has/delete/get/set
fruits.forEach((value,key)=> {
	text += key + value;
})

```

## Class 
```js
class Car {  
  constructor(name, year) {  
    this.name = name;  
    this.year = year;  
  } 
  age(){
  }
  method2{
  } 
}
```

## Javascript Modules
```js
<script type="module">  
import message from "./message.js";  
</script>

Named Exports
export const name = "Jesse";  
export const age = 40;

const name = "Jesse";  
const age = 40;
export {name, age}

Default Exports (once per file)
const message = () => {  
	const name = "Jesse";  
	const age = 40;  
	return name + ' is ' + age + 'years old.';  
};  
  
export default message;
import message from "./message.js";

```




## Variable Scoping and Assignment

### Destructuring
```js
[a, b, ...rest] = [10, 20, 30, 40, 50];

console.log(rest);
// Expected output: Array [30, 40, 50]

// Destructuring objects on the left-hand side of assignment
const obj = { a: 1, b: 2 };
const { a, b } = obj;
// is equivalent to:
// const a = obj.a;
// const b = obj.b;

//Two variables can be swapped in one destructuring expression
const arr = [1, 2, 3];
[arr[2], arr[1]] = [arr[1], arr[2]];
console.log(arr); // [1, 3, 2]
```

- Destructuring an array of Length N with number of variables specified on the left hand side greater than N will result in remaining variables being undefined

### Binding and Assignment

```js
//Binding pattern
const numbers = [];
const obj = { a: 1, b: 2 };
//Assignment pattern, can't use with compound operators such as += or *=
({ a: numbers[0], b: numbers[1] } = obj);
```

> [!important]+ Required Parentheses
> `{ a, b } = { a: 1, b: 2 }`
> is not valid stand-alone syntax, as the { a, b } on the left-hand side is considered a block and not an object literal according to the rules of expression statements. However, `({ a, b } = { a: 1, b: 2 })` is valid, as is const `{ a, b } = { a: 1, b: 2 }`.


### Rest Parameter
```js
const [first, ...others2] = [1, 2, 3];
console.log(others2); // [2, 3]

//Inner destructuring destructures from the array created after collecting the rest elements
//So you cannot access any properties present on the original iterable in this way
const [a, b, ...{ length }] = [1, 2, 3];
console.log(a, b, length); // 1 2 1

const [a, b, ...[c, d]] = [1, 2, 3, 4];
console.log(a, b, c, d); // 1 2 3 4


```
 - Allows a function to accept an indefinite number of arguments as an array
 - function definition can only have one rest parameter and it must be the last parameter (with no trailing comma)


### .apply()
- null can be passed as the first parameter when you have no specific value you want to set this pointer to 
### Spread operator
- allows an iterable to be expanded in places where zero or more arguments are expected

### var/let/const
- var always has global scope and can be redeclared
- let always have block scope and can't be redeclared
- const have block scope and can't be reassigned/redeclared
- var can be "hoisted to the top" (used before it is initialized)
	- function hoisting is useful for readability by showing business logic at the top

### Strict equality, does-not-equal
` ===, !== `
- strict equality requires that the types are also equal
- note that comparing two javascript objects always returns false
### Nullish coalescing assignment operator
`let x;` `x ??= 5;`
- If the first value is undefined or null, the second value is assigned
### Escaping special characters
- `\`
- An additional escape is needed if for a function (ie: querySelector())
	- `document.querySelector(#foo\\\\bar");` matches `<div id="foo\bar"></div>`
### Javascript Types are Dynamic
- same variable can be reassigned to a different data type
## Event
### querySelector, querySelectorAll
`document.querySelector("p.example")`
- get the first `<p>` element with class "example"
`document.querySelector("a[target="name"])"`
- Select first `<a>` element that has a "target" attribute = "name"
`document.querySelector("div > p")`
- select first `<p>` element with parent `<div>`
#### Negation
- negate selectors with `not`

### Event handlers
`<html-element>.addEventListener("event", function (){});

#### Common Events
`onchange, onclick, onmouseover, onmouseout, onkeydown, onload`

## Types
### Undefined vs null
- null is an assigned value (of nothing)
- undefined means the variable has been declared but not defined yet
### template literals
`string text ${expression} string text`

### object shorthand
```
const name = 'nsdf';
const age = 20;

const user = {
	name,
	age
};
```
## Array vs Object
Objects can be anything. Everything in JS is an object and can be stored in a variable
```js
const person = {  
  firstName: "John",  
  lastName : "Doe",  
  id       : 5566,  
  fullName : function() {  
    return this.firstName + " " + this.lastName;  
  }  
};
```

- `this` is used to refer the object/element in the current scope

### When to use objects

### Mutable vs Immutable

## Functions
### Assignment

### Pass by value vs reference
- All primitive values are passed by value
- All objects (including functions) are passed by "copy of a reference"
	- It is possible to modify the contents of that object but not overwrite the reference

```js
function reference(obj){
	obj.a = 100;
}
let obj = {
	a: 1
};

function value(a){
	a = 100
	return a;
}

// Not possible

function replace(obj){
	obj = {}
}

```

### Closures

### Function keyword vs  arrow function
- every new function has it's own "this"
- an arrow function does not have its own this. The this value of the enclosing execution context is used
### Callbacks
- Passing a function as an argument
### Immediately invoked function expressions

## Transpilers
- source to source compilers that transform source codes in Javascript

## Importing/exporting modules

## DOM Nodes

## DOM events

## Event Handlers

## Event queue

## Promises and async managements

## Try/catch

# Other

### Objects are often not instances of classes

### Event-based flow vs multi threading
### "Const"
- const does not be a constant value
- it defines a constant reference to a value
- You can't reassign a constant value/array/object but you CAN change the elements of a constant array/object
### Strict mode
- Anything inside a `class` is in strict mode by default
- Prevents you from using undefined variables, helpful for debugging and writing/compiling better code
# Related
