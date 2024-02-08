def cartelera():

    import requests
    from bs4 import BeautifulSoup

    URL = 'https://www.taquilla.com/a-coruna/cinesa-marineda-city-a-coruna'

    response = requests.get(URL)
    soup = BeautifulSoup(response.content,'html.parser')
    html = 'Cartelera Marineda City - A Coruña\n\n'

    for peli in soup.find_all(class_="list-films__content"):
        film = peli.find(class_="film-title data-link").text
        url = peli.h3.get('data-link')
        html += f'· <a href="{url}">{film}</a>\n\n'
        
    return html