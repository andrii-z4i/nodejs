var Emitter = require('./emitter');

var emitter = new Emitter();

emitter.on('greet', function(){
    console.log('greet happened!');
});

emitter.on('greet', function(){
    console.log('greet 2 happened!');
});

emitter.on('bye', function(){
    console.log('bye happened!');
});

console.log('Hello!');

emitter.emit('greet');