function Greeter() {
	this.greeting = 'Hello World!!!';
	
	this.greet = function() {
		console.log(this.greeting);
	}
}

module.exports = Greeter;