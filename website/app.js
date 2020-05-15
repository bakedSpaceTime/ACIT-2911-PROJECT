var express       = require('express');
var mongoose      = require('mongoose');
var http          = require('http');
var path          = require('path');
var engine        = require('ejs-locals');
var bodyParser    = require('body-parser');
const DB_URI      = 'mongodb://localhost:27017/testdb';

let options       = { useNewUrlParser: true , useUnifiedTopology: true };
mongoose.connect(process.env.MONGODB_URI || DB_URI, options);
mongoose.set('useCreateIndex', true);

var app           = express();

// Parse URL-encoded bodies (as sent by HTML forms)
app.use(express.urlencoded({ extended: true }));;
app.use(express.json());
app.use(bodyParser.urlencoded({ extended: false }));


 // Enable routing and use port 1337.
require('./router')(app);
app.set('port', 1337);

 // Set up ejs templating.
app.engine('ejs', engine);
app.set('view engine', 'ejs');

// Set view folder.
app.set('views', path.join(__dirname, '/views'));

// That line is to specify a directory where you could 
// link to static files (images, CSS, etc.). 
// So if you put a style.css file in that directory and you 
// could link directly to it in your view <link href=”style.css” rel=”stylesheet”>
app.use(express.static(path.join(__dirname, 'static')));

// Set up the ability to reference images
app.use(express.static(__dirname+'/public'));

// Local listening
// http.createServer(app).listen(app.get('port'), function(){
//   console.log('Express server listening on port ' + app.get('port'));
// });

http.createServer(app).listen(process.env.PORT || 3000, function() {
  console.log('Express server listening on port ' + app.get('port'));
});

module.exports = app