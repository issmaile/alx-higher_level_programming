#!/usr/bin/node
const fs = require('fs');
const req = require('request');
const url = process.argv[2];
const file = process.argv[3];

req(url, (err, resp, body) => {
  if (err) throw (err);
  try {
    fs.writeFileSync(file, body, 'utf-8');
  } catch (err) {
    console.error(err);
  }
});
