var util = require('util');

function Person(firstname, lastname) {
    this.firstname = firstname;
    this.lastname = lastname;
}

Person.prototype.greet = function() {
    console.log('Hello ' + this.firstname + ' ' + this.lastname);
}

var andrii = new Person('Andrii', 'Kozin');
andrii.greet();

var svitlana = new Person('Svitlana', 'Kozina');
svitlana.greet();

console.log(andrii.__proto__);
console.log(svitlana.__proto__);
console.log(andrii.__proto__ === svitlana.__proto__);