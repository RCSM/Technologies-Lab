var dgram = require('dgram');
var server = dgram.createSocket('udp4');

server.on('listening', function (){
	var address = server.address();
	console.log('UDP Server listening on ' 
		+ address.address + ':' + address.port);
});

server.on('message', function (message, remote) {
	console.log('From = ' + remote.address + ':' + remote.port);
	console.log('Message --> ' + message);
});

server.bind(5000, '127.0.0.1');