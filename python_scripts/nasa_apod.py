import requests
from datetime import datetime

API_KEY = '79DIZTyZxb4DsDHvWlirQGIP2NoWqKetp60zctxT'
url = 'https://api.nasa.gov/planetary/apod'
date = datetime.today().strftime('%Y-%m-%d') 


response = requests.get(url, params = {'api_key':API_KEY, 'date':date})
# print(response.json())

fecha = response.json()['date']
# print(fecha)
titulo = response.json()['title']
print(fecha, '-',titulo)
url_imagen = response.json()['url']
print(url_imagen) 
texto = response.json()['explanation']
print(texto)