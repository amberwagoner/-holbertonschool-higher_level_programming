#!/usr/bin/node
// Task 6
const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const tasks = JSON.parse(body);

  const completedTasksByUserId = {};

  tasks.forEach(task => {
    if (task.completed) {
      if (completedTasksByUserId[task.userId]) {
        completedTasksByUserId[task.userId]++;
      } else {
        completedTasksByUserId[task.userId] = 1;
      }
    }
  });

  Object.keys(completedTasksByUserId).forEach(userId => {
    console.log(`${userId}: ${completedTasksByUserId[userId]}`);
  });
});
