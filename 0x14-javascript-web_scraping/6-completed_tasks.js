#!/usr/bin/node
const req = require('request');
const url = process.argv[2];

req(url, { json: true }, (err, resp, body) => {
  if (err) throw (err);
  const users = {};
  for (const task of body) {
    if (task.completed) {
      users[task.userId] = (users[task.userId] || 0) + 1;
    }
  }
  console.log(users);
});
