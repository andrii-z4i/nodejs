var Emitter = require('events');
var eventConfig = require('./config').events;

var emitter = new Emitter();

emitter.on(eventConfig.events, function(){
    console.log('greet happened!');
});

emitter.on(eventConfig.events, function(){
    console.log('greet 2 happened!');
});

emitter.on(eventConfig.bye, function(){
    console.log('bye happened!');
});

console.log('Hello!');

emitter.emit(eventConfig.greet);