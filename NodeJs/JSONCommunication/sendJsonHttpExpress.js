var bodyParser = require('body-parser');
var express = require('express');
var path = require('path');
var fs = require('fs');
var app = express();

app.use(bodyParser.json());

// Send the index.html
app.get('/', function (req, res) {
	var filePath = path.join(__dirname, 'index.html');
	res.sendFile(filePath);
});

// Send the json
app.get('/sent_from_server', function (req, res) {
	var filePath = path.join(__dirname, 'test.json');
	res.sendFile(filePath);
});

app.get('/sent_from_client', function (req, res) {
	console.log(req.body);
});

app.listen(5000, function () {
   console.log("Example app listening at http://%s:%s", "127.0.0.1", 5000);
});