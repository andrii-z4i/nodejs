module.exports = function(app) {
    // RESTful API
    app.get('/api/person/:id', function(req, res) {
        // get that data from database
        res.json({ firstname: 'Andrii', lastname: 'Kozin' });
    });

    app.post('/api/person', function(req, res){
        // save to the database
    });

    app.delete('/api/person/:id', function(req, res) {
        // delete that from database
    });
}
