#!/usr/bin/node
// Task 6
const request = require('request');

const api_url = "https://jsonplaceholder.typicode.com/todos";

request(api_url, function (error, response, body) {
  if (error) {
    console.error("Error: Failed to fetch data from API");
    return;
  }
  
  if (response.statusCode !== 200) {
    console.error("Error: Failed to fetch data from API");
    return;
  }
  
  const data = JSON.parse(body);
  
  const completedTasksByUser = {};
  
  for (const task of data) {
    if (task.completed) {
      const userId = task.userId;
      if (userId in completedTasksByUser) {
        completedTasksByUser[userId]++;
      } else {
        completedTasksByUser[userId] = 1;
      }
    }
  }

  for (const [userId, completedTaskCount] of Object.entries(completedTasksByUser)) {
    console.log(`'${userId}': ${completedTaskCount}`);
  }
});
