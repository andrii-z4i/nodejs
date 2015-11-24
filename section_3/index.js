var express = require('express');
var app = express();
var apiController = require('./controllers/apiController');
var htmlController = require('./controllers/htmlController');


var port = process.env.PORT || 3000;

// add middleware layers
app.use('/assets', express.static(__dirname + '/public'));
app.use('/', function(req, res, next){
    console.log("Request url: " + req.url);
    next();
});

app.set('view engine', 'ejs');

apiController(app);
htmlController(app);

app.listen(port);
