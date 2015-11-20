// REVEALING MODULE PATTERN

var greeting = 'Hello wrorld!!!!';

function greet() {
	console.log(greeting);
}

module.exports = {
	greet: greet
};