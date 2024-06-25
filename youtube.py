import requests
import json
import re


# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'AIzaSyDpFMBN2YJAtF0TxMsnNJlYRRXLm3CQbMo'
search_query = 'Minecraft Bed Wars'
url = f'https://www.googleapis.com/youtube/v3/search?key={api_key}&part=snippet&q={search_query}'

response = requests.get(url)

if response.status_code == 200:
  data = response.json()
  video_titles = []
  for item in data['items']:
    if item['id']['kind'] == 'youtube#video':
      video_titles.append(item['snippet']['title'])
  print("Video Titles:")
  for title in video_titles:
      print(title)
else:
    print(f'Error: {response.status_code}')