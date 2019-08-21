import requests
from bs4 import BeautifulSoup

ebayReq = requests.get("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR12.TRC2.A0.H0.Xblanke.TRS0&_nkw=blanket&_sacat=0")
srcEbay = ebayReq.content

ebay = BeautifulSoup(srcEbay, 'html.parser')
parentElement = ebay.find_all('div', class_="s-item__wrapper clearfix")
priceAndUrl = []
for element in parentElement:
    price = element.find('div', class_='s-item__info clearfix').find('span', class_='s-item__price').text
    url = element.find('div', class_='s-item__info clearfix').find('a', class_='s-item__link').get('href')
    priceAndUrl.append([price, url])

print(priceAndUrl)
