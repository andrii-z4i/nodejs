var http = require('http');

var http_server = http.createServer(function(request, response){

    response.writeHead(200, { 'Content-Type' : 'application/json'});

    var obj = {
        firstname: 'Andrii',
        lastname: 'Kozin'
    };

    response.end(JSON.stringify(obj));
});

http_server.listen(8081, 'localhost');

