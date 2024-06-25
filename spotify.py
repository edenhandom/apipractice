import requests
import json
import re
import os 

CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
'grant_type': 'client_credentials',
'client_id': os.environ.get('SPOTIFY_CLIENT_ID'),
'client_secret': os.environ.get('SPOTIFY_CLIENT_SECRET'),
})