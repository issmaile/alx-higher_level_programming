#!/usr/bin/node
const req = require('request');
const url = 'https://swapi-api.alx-tools.com/api/people/18';

req(url, { json: true }, (err, resp, body) => {
  if (err) throw (err);
  console.log(body.films.length);
});
