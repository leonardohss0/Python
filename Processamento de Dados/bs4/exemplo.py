from bs4 import BeautifulSoup
import requests

with open("arquivo.html") as html_doc:
    soup = BeautifulSoup(html_doc, 'html.parser')
    print(soup.title)
    print(soup.title.name)
    print(soup.title.string)

    resultado = soup.find_all('a')

    for i in range(len(resultado)):
        print(resultado[i])

    print(soup.find(id='link3'))
