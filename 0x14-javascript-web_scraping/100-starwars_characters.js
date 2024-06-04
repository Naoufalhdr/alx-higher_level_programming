#!/usr/bin/node

const request = require('request');

// Define the URL for the Star Wars API
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;

// Make a GET request to the API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error: Unexpected response:', response.statusCode);
  }

  // Parse the response body & extract the chararcter URL
  const characters = JSON.parse(body).characters;

  // Fetch character data and print their names
  characters.forEach(character => {
    request(character, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error('Error: Unexpected response:', response.statusCode);
      }

      const characterName = JSON.parse(body).name;
      console.log(characterName);
    });
  });
});
