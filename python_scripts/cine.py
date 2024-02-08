def cartelera():

    import requests
    from bs4 import BeautifulSoup

    URL = 'https://www.taquilla.com/a-coruna/cinesa-marineda-city-a-coruna'
    paxina = requests.get(URL)
    soup = BeautifulSoup(paxina.content,'html.parser')
    html = 'Cartelera Marineda City - A Coruña\n\n'

    for noticia in soup.find_all(class_="list-films__content"):
        film = noticia.find(class_="film-title data-link").text
        url = noticia.h3.get('data-link')
        html += f'· <a href="{url}">{film}</a>\n\n'
    return html
    
# cartelera()