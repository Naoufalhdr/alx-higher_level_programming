#!/usr/bin/node

const request = require('request');

// Define the URL for the Star Wars API
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;

// Function to fetch character data given a character URL
const fetchCharacter = (characterURL) => {
  return new Promise((resolve, reject) => {
    request(characterURL, (error, response, body) => {
      if (error) {
        reject(error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error(`Unexpected response: ${response.statusCode}`);
        return;
      }

      const characterData = JSON.parse(body);
      resolve(characterData);
    });
  });
};

// Make a GET request to the API URL
request(apiUrl, async (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error: Unexpected response:', response.statusCode);
    return;
  }

  // Parse the response body
  const movieData = JSON.parse(body);

  // Extract character URLs from the movie data
  const characterURLs = movieData.characters;

  try {
    // Fetch character data for each character URL
    for (let i = 0; i < characterURLs.length; i++) {
      const characterData = await fetchCharacter(characterURLs[i]);
      console.log(`${characterData.name}`);
    }
  } catch (error) {
    console.error('Error:', error);
  }
});
