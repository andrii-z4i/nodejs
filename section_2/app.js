var http = require('http');
var fs = require('fs');

var http_server = http.createServer(function(request, response){
    if (request.url === '/') {
        response.writeHead(200, { 'Content-Type' : 'text/html'});
        fs.createReadStream(__dirname + '/index.html').pipe(response);
    }
    else if (request.url === '/api') {
        response.writeHead(200, { 'Content-Type' : 'application/json'});

        var obj = {
            firstname: 'Andrii',
            lastname: 'Kozin'
        };

        response.end(JSON.stringify(obj));
    }
    else {
        response.writeHead(404, { 'Content-Type' : 'text/plain'});
        response.end("Nothing to show to you...")
    }

});

http_server.listen(8081, 'localhost');
