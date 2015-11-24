var express = require('express');

var app = express();

var port = process.env.PORT || 3000;

app.get('/', function(req, res) {
    res.send('<html><head></head><body><h1>Hello world!<h1><h3>Who are you?</h3></body></html>')
});

app.get('/api', function(req, res) {
    res.send({ firstname: 'Andrii', lastname: 'Kozin' })
});

app.get('/person/:id', function(req, res) {
    res.send('<html><head></head><body><h1>Hello world!<h1><h3>' + req.params.id + '</h3></body></html>')
});

app.get('/connect/:id', function(req, res) {
    if (req.params.id === 'me') {
        res.send({ firstname: 'Andrii', lastname: 'Kozin' });
    }
    else {
        res.send({ firstname: req.params.id});
    }
})

app.listen(port);
