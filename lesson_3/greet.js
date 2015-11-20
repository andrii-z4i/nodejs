/*
// Incorrect assign 
exports = function() {
	console.log('Hello');
}
*/

// Mutate object
exports.greet = function() {
	console.log('Hello');
}

console.log(exports);
console.log(module.exports);