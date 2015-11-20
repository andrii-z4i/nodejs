var EventEmitter = require('events');
var util = require('util');

function Greetr() {
    // call Constructor of the base class
    EventEmitter.call(this);
    this.greeting = 'Hello world!';
}

util.inherits(Greetr, EventEmitter);

Greetr.prototype.greet = function (data) {
    console.log(this.greeting + ': ' + data);
    this.emit('greet', data);
}

var greeter1 = new Greetr();

greeter1.on('greet', function(data) {
    console.log('Someone greeted! ' + data);
});

greeter1.greet('I did this!');

// check how does it work without params
greeter1.greet();