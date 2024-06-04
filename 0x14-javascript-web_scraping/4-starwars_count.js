#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error('error:', error);
  } else if (response.statusCode !== 200) {
    console.log('status code:', response.statusCode);
  } else {
    let count = 0;
    const films = JSON.parse(body).results;
    films.forEach(film => {
      film.characters.forEach(character => {
        const characterId = parseInt(character.split('/').slice(-2, -1)[0]);
        if (characterId === 18) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
