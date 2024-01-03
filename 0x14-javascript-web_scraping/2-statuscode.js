#!/usr/bin/node
const req = require('request');
const url = process.argv[2]

req(url, (err, res) => {
  if (err) throw(err);
  console.log('code:', res.statusCode);
});
