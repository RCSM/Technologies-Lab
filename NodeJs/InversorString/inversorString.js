var net = require('net');

var server = net.createServer(function (socket) {
	console.log("\n---------------------------");
	console.log("Connection from" + socket.remoteAddress);
	console.log("---------------------------");

	socket.on('data', function (data) {
		console.log('MSG RECEIVED... : ' + data);

		var rvs = data.toString().split("").reverse().join();

		console.log('MSG after processing : ' + rvs);
		socket.write('MSG REVERSED... : ' + rvs);
	});
});

server.listen(5000, function () {
	console.log('Server running at http://127.0.0.1:5000/');
});