var fs = require('fs');


var readable = fs.createReadStream(__dirname + '/greet.txt', {encoding: 'utf8', highWaterMark: 2 * 1024});

var writable = fs.createWriteStream(__dirname + '/greet_copy.txt');

var chunk_number = 0;
readable.on('data', function(chunk){
    console.log('Chunk number: ' + chunk_number);
    writable.write(chunk);
    chunk_number++;
});

