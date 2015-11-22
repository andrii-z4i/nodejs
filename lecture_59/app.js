var http = require('http');

var http_server = http.createServer(function(request, response){
    console.log(request.url);
    console.log(request.headers);
    console.log(request.method);
    response.writeHead(200, { 'Content-Type' : 'text/plain'});
    response.end('Hello world\n');
});

http_server.listen(8081, 'localhost');

