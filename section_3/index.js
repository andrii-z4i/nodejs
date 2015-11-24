var express = require('express');
var app = express();

var apiController = require('./controllers/apiController');
var htmlController = require('./controllers/htmlController');

var port = process.env.PORT || 3000;

// add middleware layers
app.use('/assets', express.static(__dirname + '/public'));
/*var mysql = require('mysql');
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
});*/

var mongoose = require('mongoose');

mongoose.connect('mongodb://test:test@ds057244.mongolab.com:57244/addressbook');

var Schema = mongoose.Schema;

var personSchema = new Schema({
    firstname: String,
    lastname: String,
    address: String
});

var Person = mongoose.model('Person', personSchema);

var john = Person({
    firstname: 'John',
    lastname: 'Doe',
    address: '555 Main St.'
});

john.save(function(err){
    if (err) throw err;
    console.log('person saved!');
});

var jane = Person({
    firstname: 'Jane',
    lastname: 'Doe',
    address: '555 Main St.'
});

jane.save(function(err){
    if (err) throw err;
    console.log('person saved!');
});

app.use('/', function(req, res, next){
    console.log("Request url: " + req.url);
    Person.find({}, function(err, users){
        if (err) throw err;
        console.log(users);
    });
    next();
});

app.set('view engine', 'ejs');

apiController(app);
htmlController(app);

app.listen(port);
