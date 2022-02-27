import requests
from bs4 import BeautifulSoup

url = "https://english.elpais.com"

r1 = requests.get(url)
coverpage = r1.content

soup1 = BeautifulSoup(coverpage, 'html5lib')

coverpage_news = soup1.find_all('h2', class_='articulo-titulo')
coverpage_news[4].get_text()
coverpage_news[4]['href']
