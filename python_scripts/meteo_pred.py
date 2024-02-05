def meteo_pred():

    import requests

    url  = 'http://api.openweathermap.org/geo/1.0/direct?q=Corme&limit=5'
    API_KEY = '485494d92810c23e867fb42e23af5282'

    response = requests.get(url, params = {'apiKey':API_KEY})
    lat=response.json()[0]['lat']
    lon=response.json()[0]['lon']

    url='http://api.openweathermap.org/data/2.5/forecast'

    response = requests.get(url, params = {'apiKey':API_KEY, 'lat':lat, 'lon':lon})
    response.json()
    # print(response.json()['list'][0]['main'])
    temp_max=(f"Temperatura máxima: {response.json()['list'][0]['main']['temp_max']}")
    temp_min=(f"Temperatura mínima: {response.json()['list'][0]['main']['temp_min']}")
    sky=(f"Estado do ceo: {response.json()['list'][0]['weather'][0]['main']}")
    rain=("Non hai precipitacións")
    if 'rain' in response.json()['list'][0]:
        if response.json()['list'][0]['rain']['1h']:
            rain=(f"Volumen de chuvia na última hora: {response.json()['list'][0]['rain']['1h']}mm")
        else:
            rain=(f"Volumen de chuvia nas últimas 3 horas: {response.json()['list'][0]['rain']['3h']}mm")

    respuesta = (f"{temp_max}\n{temp_min}\n{sky}\n{rain}")

    return respuesta