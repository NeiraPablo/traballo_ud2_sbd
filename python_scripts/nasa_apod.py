def nasa():
    import requests
    from datetime import datetime

    API_KEY = '79DIZTyZxb4DsDHvWlirQGIP2NoWqKetp60zctxT'
    url = 'https://api.nasa.gov/planetary/apod'
    date = datetime.today().strftime('%Y-%m-%d') 

    response = requests.get(url, params = {'api_key':API_KEY, 'date':date})

    intro = (f"{response.json()['date']} - {response.json()['title']}")
    url_imagen = (f"{response.json()['url']}")
    texto = response.json()['explanation']
    # respuesta = (f"{intro} \n{url_imagen} \n{texto}")
    text = f"{intro}\n\n{texto}"
    
    return text, url_imagen
