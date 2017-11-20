var dgram = require('dgram');

var client = dgram.createSocket('udp4');
var message = new Buffer('My KungFu is Panda!');

client.send(message, 0, message.length, 5000, '127.0.0.1', function (err, bytes) {
	if (err) throw err;
	console.log('UDP message sent!')
	client.close();
});