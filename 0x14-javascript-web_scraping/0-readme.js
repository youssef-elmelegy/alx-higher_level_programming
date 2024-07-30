#!/usr/bin/node
const req = require('fs');
req.readFile(process.argv[2], 'utf8', function(error, content) {
	if (error) {
		return console.log(error);
	}
	console.log(content);
});
