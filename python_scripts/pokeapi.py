def pokemon():
    import requests
    import random as random

    url = 'https://pokeapi.co/api/v2/pokemon/'

    num_pokes = 1025
    random_poke = random.randrange(0, num_pokes, 1)
    random_poke=str(random_poke)

    pokemito = url+random_poke

    response = requests.get(pokemito)
    # print(response.json())

    nombre = response.json()['name']
    num = response.json()['id']
    # print(nombre)
    # print(num)
    if len(response.json()['types']) == 1:
        tipo = response.json()['types'][0]['type']['name']
    elif len(response.json()['types']) == 2:
        tipo = response.json()['types'][0]['type']['name'] + ' ' + response.json()['types'][1]['type']['name']
    # print(tipo)
    image = response.json()['sprites']['front_default']
    # print(image)
    # respuesta = (f"Nombre: {nombre}\n\nNº Pokedex: {num}\n\nTipo: {tipo}\n\n{image}")
    texto = f"Nombre: {nombre}\n\nNº Pokedex: {num}\n\nTipo: {tipo}"
    imagen = image

    return texto, imagen
