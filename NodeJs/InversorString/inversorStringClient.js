var net = require('net');
const readline = require('readline');
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

var client = new net.Socket();

client.connect(5000, '127.0.0.1');

rl.on('line', function (input) {
	client.write(input.toString().trim());
});

client.on('data', function(data) {
	console.log(data.toString());
});

client.on('end', function() {
	console.log('Connection closed');
	process.exit(1);
});