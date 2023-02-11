#!/usr/bin/env python3

import requests

headers = {
  'User-Agent': '<Bot_upvote_discord>/0.0.1',
  'Authorization': 'bearer <6YPF_vDIhdqTjgkFgA5l0qRpTAaBVg>',
  'Content-Type': 'application/json'
}

response = requests.get('https://api.reddit.com/r/all/top?limit=1&t=day', headers=headers)

if response.status_code == 200:
  print(response.json())
else:
  print('Failed to fetch data from Reddit API')
