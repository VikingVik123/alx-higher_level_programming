#!/usr/bin/node

const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request.get(url, (_, response, body) => {
  const movie = JSON.parse(body);
  console.log(movie.title);
});
