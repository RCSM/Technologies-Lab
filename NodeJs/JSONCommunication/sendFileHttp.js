var http = require('http');
var path = require('path');
var fs = require('fs');

var server = http.createServer( function (req, res) {
	var filePath = path.join(__dirname, 'index.html');
	var stat = fs.statSync(filePath);

	res.writeHead(200, {
		'Content-Type': 'text/html',
		'Content-Length': stat.size
	});

	var readStream = fs.createReadStream(filePath);

	readStream.pipe(res);
});

server.listen(5000, function () {
	console.log('Server on')
});