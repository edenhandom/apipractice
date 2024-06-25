import requests

url_newest_story = 'https://hacker-news.firebaseio.com/v0/newsstories.json?print=pretty'


response = requests.get(url_newest_story)
latest_ids = response.json()

if latest_ids:
  latest_id = latest_ids[0]
  url_story = f'https://hacker-news.firebaseio.com/v0/item/{latest_id}.json?print=pretty'


  response = requests.get(url_story)
  story = response.json()

  if 'title' in story and 'by' in story and 'url' in story:
    print("Title:", story['title'])
    print("Author:", story['by'])
    print("Link:", story['url'])

