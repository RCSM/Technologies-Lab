var express = require('express');
var app = express();

var path = require('path');

app.get('/', function (req, res) {
	var filePath = path.join(__dirname, 'index.html');
	res.sendFile(filePath);
});

app.listen(5000, function () {
	console.log('Server running at : http://127.0.0.1:5000');
});