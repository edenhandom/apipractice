import requests
import json
import re

#supernatural https://open.spotify.com/track/142PiXzA84lmEw2RstFHFa?si=40153655ed614f5f
CLIENT_ID = 'b74375f472fc4642ae52a40302a52e04'
CLIENT_SECRET = 'ad9e4134b73440b583d808af6737035f'

AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

auth_response_data = auth_response.json()
access_token = auth_response_data['access_token']

headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}
BASE_URL = 'https://api.spotify.com/v1/' #endpoint
track_url = input('Enter track url: ')
track_id = re.findall('track/(\w+)\?', track_url)[0]
r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)

print(r.status_code)
data = r.json()
print(data)