'use strict';

class Person {
    constructor(firstname, lastname) {
        this.firstname = firstname;
        this.lastname = lastname;
    }

    greet() {
        console.log('Hello ' + this.firstname + ' ' + this.lastname);
    }
}

var andrii = new Person('Andrii', 'Kozin');
andrii.greet();

var svitlana = new Person('Svitlana', 'Kozina');
svitlana.greet();

console.log(andrii.__proto__);
console.log(svitlana.__proto__);
console.log(andrii.__proto__ === svitlana.__proto__);