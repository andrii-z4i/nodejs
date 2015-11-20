var obj = {
    greet: 'Hello'
}

console.log(obj.greet);
console.log(obj['greet']);
var prop = 'greet';
console.log(obj[prop]);


//

var arr = [];
//arr.push('element1');
arr.push(function(){
    console.log('Hello world 1');
});
arr.push(function(){
    console.log('Hello world 2');
});
arr.push(function(){
    console.log('Hello world 3');
});

console.log(arr);

arr.forEach(function(item){
    item();
});