var http = require('http');
var fs = require('fs');

var http_server = http.createServer(function(request, response){

    response.writeHead(200, { 'Content-Type' : 'text/html'});
    var message = "Who are you?"

    var html = fs.readFile(__dirname + '/index.html', 'utf8', function(err, data){
        console.log(data);
        data = data.replace('{Message}', message);
        response.end(data);
    });
});

http_server.listen(8081, 'localhost');

