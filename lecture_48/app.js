var buffer = new ArrayBuffer(8);
var view = new Int32Array(buffer); // 2 numbers only because we use buffer for 8 bytes and we declare int32 array which means that one element of array will hold 4 bytes
view[0] = 5;
view[1] = 15;
console.log(view);
