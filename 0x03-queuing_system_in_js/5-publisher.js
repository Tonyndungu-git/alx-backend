#!/usr/bin/yarn dev
import { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

const publishMessage = (message, time) => {
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log(`About to send ${message}`);
      client.publish('holberton school channel', message, () => {
        resolve(); // Resolve the promise after publishing
      });
    }, time);
  });
};

client.on('connect', async () => {
  console.log('Redis client connected to the server');

  // Use Promise.all to wait for all messages to be published
  await Promise.all([
    publishMessage('Holberton Student #1 starts course', 100),
    publishMessage('Holberton Student #2 starts course', 200),
    publishMessage('KILL_SERVER', 300),
    publishMessage('Holberton Student #3 starts course', 400),
  ]);

  // Close the Redis client after all messages are published
  client.quit();
});
