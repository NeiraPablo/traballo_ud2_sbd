def titular():

    import requests
    from bs4 import BeautifulSoup
    
    url = 'https://www.eldiario.es'
    response = requests.get(url)

    soup = BeautifulSoup(response.content,'html.parser')
    html = f''

    for noticia in soup.find_all(class_="ni-title")[:5]:
        titular = noticia.a.text.strip()
        link =  noticia.a.get('href')
        html += f'· <a href="https://www.eldiario.es{link}">{titular}</a>\n\n'

    return html