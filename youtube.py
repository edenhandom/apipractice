import requests
import json
import re
import pandas as pd
import sqlalchemy as db


# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'AIzaSyDpFMBN2YJAtF0TxMsnNJlYRRXLm3CQbMo'
search_query = 'Minecraft Bed Wars'
url = f'https://www.googleapis.com/youtube/v3/search?key={api_key}&part=snippet&q={search_query}'

response = requests.get(url)

if response.status_code == 200:
  data = response.json()
  video_titles_dict = {}
  for item in data['items']:
    if item['id']['kind'] == 'youtube#video':
      video_titles_dict[item['id']['videoId']] = item['snippet']['title']
  df = pd.DataFrame.from_dict(video_titles_dict, orient='index', columns=['Video Title'])
  print("DataFrame from Video Titles:")
  print(df)

  engine = db.create_engine('sqlite:///data_base_name.db')
  df.to_sql('table_name', con=engine, if_exists='replace', index=False)
  with engine.connect() as connection:
   query_result = connection.execute(db.text("SELECT * FROM table_name;")).fetchall()
   print(pd.DataFrame(query_result))

