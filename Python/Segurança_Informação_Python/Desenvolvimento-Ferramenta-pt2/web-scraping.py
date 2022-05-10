from bs4 import BeautifulSoup
import requests

site = requests.get("https://www.climatempo.com.br").content
#objeto site recebendo o conteudo da requisição http do site
soup = BeautifulSoup(site, 'html.parser')
##Objeto soup baixando do site o html
print(soup.prettify())
##trabsforma html em string e o print vai exibir o html

# temperatura = soup.find("span",class_="_block _margin-b-5 -gray")/ somente a caso de exemplo

