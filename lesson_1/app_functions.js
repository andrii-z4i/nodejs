// function statement
function greet(){
	console.log('hi');
}

greet();

// functions are first-class 
function logGreeting(fn){
	fn();
}

logGreeting(greet);

// function expression
var greetMe = function(){
	console.log('Hi Andrii');
};

greetMe();

// it's first-class
logGreeting(greetMe);

logGreeting(function(){
	console.log('Hello Andrii');
});


function Person(firstname, lastname) {
	
	this.firstname = firstname;
	this.lastname = lastname;
	
}

Person.prototype.greet = function() {
	console.log('Hello ' + this.firstname + ' ' + this.lastname);
}

var john = new Person('John', 'Doe');
john.greet();

var jane = new Person('Jane', 'Doe');
jane.greet();

console.log(john.__proto__);
console.log(jane.__proto__);


// pass by value

function change(value) {
	value = 2;
}

var a = 1;
change(a);
console.log(a);


function changeObj(obj) {
	obj.prop1 = function () {
		
	};
	obj.prop2 = {};
}

var cObject = {};
cObject.prop1 = {};
console.log(cObject);
changeObj(cObject);
console.log(cObject);


(function(){
	console.log('in function expression');
}());