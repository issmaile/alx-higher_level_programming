#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];
const data = fs.readFile(file, 'utf8', function(err, cont) {
	console.log(err || cont);
});
console.log(data);
