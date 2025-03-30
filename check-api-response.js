// check-api-response.js
import fetch from 'node-fetch';
import dotenv from 'dotenv';

dotenv.config();

const GITHUB_ACCESS_TOKEN = process.env.GITHUB_ACCESS_TOKEN;
const GITHUB_API_URL = 'https://api.github.com/graphql';

console.log(process.cwd());
console.log("Token aus dotenv:", process.env.GITHUB_ACCESS_TOKEN);


const query = `
{
  repository(owner: "wearesolutionarchitects", name: "ausbildung-public") {
    discussions(first: 20) {
      edges {
        node {
          id
          title
          bodyHTML
        }
      }
    }
  }
}`;

async function fetchDiscussions() {
  const response = await fetch(GITHUB_API_URL, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${GITHUB_ACCESS_TOKEN}`,
    },
    body: JSON.stringify({ query }),
  });

  const data = await response.json();
  console.log(JSON.stringify(data, null, 2));
}

fetchDiscussions().catch(console.error);