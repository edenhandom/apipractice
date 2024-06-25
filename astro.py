import requests

url = 'http://api.open-notify.org/astros.json'
response = requests.get(url)
print(response.status_code)

data = response.json()
people = data.get('people', [])

for person in people[:5]:
  print(person.get('name'))
