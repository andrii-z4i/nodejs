var express = require('express');
var app = express();

var mysql = require('mysql');

var apiController = require('./controllers/apiController');
var htmlController = require('./controllers/htmlController');


var port = process.env.PORT || 3000;

// add middleware layers
app.use('/assets', express.static(__dirname + '/public'));
app.use('/', function(req, res, next){
    console.log("Request url: " + req.url);
    var connection = mysql.createConnection({
        host: "localhost",
        port: "8889",
        user: "root",
        password: "root",
        database: "addressbook"
    });

    connection.query('SELECT People.ID, Firstname, Lastname, Address FROM People INNER JOIN PersonAddress ON People.ID = PersonAddress.PersonID INNER JOIN Address ON PersonAddress.AddressID = Address.ID ORDER BY People.ID', function(err, rows){
        if (err) throw err;
        console.log(rows);
    });
    next();
});

app.set('view engine', 'ejs');

apiController(app);
htmlController(app);

app.listen(port);
