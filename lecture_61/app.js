var http = require('http');
var fs = require('fs');

var http_server = http.createServer(function(request, response){

    response.writeHead(200, { 'Content-Type' : 'text/html'});

    fs.createReadStream(__dirname + '/index.html').pipe(response);
});

http_server.listen(8081, 'localhost');

