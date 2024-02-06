import requests

url = 'https://pokeapi.co/api/v2/pokemon/'
tal = 'pikachu'

pokemito = url+tal

response = requests.get(pokemito)
# print(response.json())

nombre = response.json()['name']
num = response.json()['id']
print(nombre)
print(num)