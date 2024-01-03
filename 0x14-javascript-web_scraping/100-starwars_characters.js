#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, { json: true }, (err, resp, body) => {
  if (err) throw (err);
  for (const character of body.characters) {
    request(character, { json: true }, (errr, ress, bodyy) => {
      if (errr) throw (errr);
      console.log(body.name);
    });
});
