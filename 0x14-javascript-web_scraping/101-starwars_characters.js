#!/usr/bin/node
const request = require('request');
const util = require('util');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

const prequest = util.promisify(request);

(async () => {
  try {
    const body = (await prequest(url, { json: true })).body;
    for (const charUrl of body.characters) {
      const bodyy = (await prequest(charUrl, { json: true })).body;
      console.log(bodyy.name);
    }
  } catch (err) {
    console.log(err);
  }
})();
