var express = require('express');

var app = express();

var port = process.env.PORT || 3000;
app.use('/assets', express.static(__dirname + '/public'));
app.use('/', function(req, res, next){
    console.log("Request url: " + req.url);
    next();
});

app.set('view engine', 'ejs');

app.get('/person/:person', function(req, res) {
    res.render('person', { ID: req.params.person });
});

app.get('/api', function(req, res) {
    res.send({ firstname: 'Andrii', lastname: 'Kozin' })
});

app.get('/', function(req, res) {
    res.render('index');
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
