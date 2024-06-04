#!/usr/bin/node

const request = require('request');

// Extract command-line argument
const url = process.argv[2];

// Make a Get request to the API url
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error: Unexpected response:', response.statusCode);
    return;
  }

  // Parse the response body
  const todos = JSON.parse(body);

  // Initialize an object to store the count of completed tasks for each user
  const completedTasks = {};

  // Count completed tasks for each user
  todos.forEach(todo => {
    if (todo.completed) {
      if (completedTasks[todo.userId]) {
        completedTasks[todo.userId]++;
      } else {
        completedTasks[todo.userId] = 1;
      }
    }
  });
  console.log(completedTasks);
});
