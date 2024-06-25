import requests

user_text = input('Enter text:')
url = 'http://text-processing.com/api/sentiment/'

myobj = {'text': user_text}
response = requests.post(url, data = myobj)

print(response.json())