#!/usr/bin/node
const req = require('req');
req.readFile(process.argv[2], 'utf8', function(error, content) {
	console.log(error || content);
});
