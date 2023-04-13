#!/usr/bin/node
// Task 6
const request = require('request');

if (process.argv.length < 3) {
  console.error('URL needed');
} else {
  const apiUrl = process.argv[2];

  request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.error(`Error occurred while making the GET request: ${error}`);
      return;
    }

    if (response.statusCode === 200) {
      const todos = JSON.parse(body);
      const userTaskCounts = {};

      todos.forEach((todo) => {
        if (todo.completed) {
          if (userTaskCounts[todo.userId]) {
            userTaskCounts[todo.userId] += 1;
          } else {
            userTaskCounts[todo.userId] = 1;
          }
        }
      });

      Object.keys(userTaskCounts).forEach(userId => {
        console.log(`${userId}: ${userTaskCounts[userId]}`);
      });
    } else {
      console.error(`Error occurred while fetching the todos: ${response.statusCode}`);
    }
  });
}
