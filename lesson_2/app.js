var greet = require('./greet1');

greet();

var greet2 = require('./greet2').greet;
greet2();

var greet3 = require('./greet3');
greet3.greet();
greet3.greeting = "Something";

// the same object due to chaching modules by node
var greet3b = require('./greet3');
greet3b.greet();

var Greet4 = require('./greet4');

var grtr = new Greet4();
grtr.greet();

var Greet4b = require('./greet4');

var grtrb = new Greet4b();
grtrb.greet();


var greet5 = require('./greet5');
greet5.greet();