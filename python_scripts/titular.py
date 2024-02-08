def titular():

    import requests
    from bs4 import BeautifulSoup
    
    url = 'https://www.eldiario.es'
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    html = f''

    for new in soup.find_all(class_="ni-subtitle"):
        headLine, link = new.a.text, new.a.get('href')
        html += f'· <a href="{link}">{headLine}</a>\n\n'

    for new in soup.find_all(class_="ni-title")[:7]:
        headLine, link = new.a.text.strip(), new.a.get('href')
        html += f'· <a href="https://www.eldiario.es{link}">{headLine}</a>\n\n'

    return html