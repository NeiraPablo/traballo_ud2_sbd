import requests

url  = 'http://api.openweathermap.org/geo/1.0/direct?q=Corme&limit=5'
API_KEY = '485494d92810c23e867fb42e23af5282'

response = requests.get(url, params = {'apiKey':API_KEY})
lat=response.json()[0]['lat']
lon=response.json()[0]['lon']

url='http://api.openweathermap.org/data/2.5/forecast'

response = requests.get(url, params = {'apiKey':API_KEY, 'lat':lat, 'lon':lon})
response.json()
print(response.json()['list'][0]['main'])
