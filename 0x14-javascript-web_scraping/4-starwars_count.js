#!/usr/bin/node
const req = require('request');
const url = process.argv[2];

req(url, (err, resp, body) => {
  if (err) throw (err);
  console.log(body.split('/people/18/').length - 1);
});
