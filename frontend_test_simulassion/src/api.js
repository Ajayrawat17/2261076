const BASE = process.env.REACT_APP_API_URL;
const TOKEN = process.env.REACT_APP_BEARER_TOKEN;

export async function customRequest(endpoint, data = {}, method = "POST") {
  const raw = JSON.stringify(data);

  const response = await fetch(`${BASE}${endpoint}`, {
    method,
    headers: {
      'Authorization': TOKEN,
      'Content-Type': 'application/json'
    },
    body: method !== 'GET' ? raw : null
  });

  return await response.json();
}
