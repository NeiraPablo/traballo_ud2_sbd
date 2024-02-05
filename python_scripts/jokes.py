def joke():    
    import requests

    URL = 'https://v2.jokeapi.dev/joke/Programming?lang=en'
    # URL = 'https://v2.jokeapi.dev/joke/Programming?lang=es' 
    ## En inglés hai máis chistes e son mellores (ou peores en realidade)

    response = requests.get(URL)
    # print(response.json())

    if response.json()['type'] == 'single':
        joke=response.json()['joke']
    elif response.json()['type'] == 'twopart':
        joke=(f"{response.json()['setup']}\n{response.json()['delivery']}")
    
    return joke
