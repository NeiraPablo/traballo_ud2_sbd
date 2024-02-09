def pokemon():
    import requests
    import random as random

    url_pokes = 'https://pokeapi.co/api/v2/pokemon/'
    url = 'https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0'

    response = requests.get(url)
    poke_limit = len(response.json()['results'])

    random_poke = random.randrange(0, poke_limit, 1)
    random_url= response.json()['results'][random_poke]['url']

    random_response = requests.get(random_url)

    nombre = random_response.json()['name']
    num = random_response.json()['id']
    if len(random_response.json()['types']) == 1:
        tipo = random_response.json()['types'][0]['type']['name']
    elif len(random_response.json()['types']) == 2:
        tipo = random_response.json()['types'][0]['type']['name'] + ' ' + random_response.json()['types'][1]['type']['name']

    image = random_response.json()['sprites']['front_default']

    texto = f"Nombre: {nombre}\n\nNº Pokedex: {num}\n\nTipo: {tipo}"
    imagen = image

    return texto, imagen
