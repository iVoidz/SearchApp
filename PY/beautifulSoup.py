import requests
from bs4 import BeautifulSoup

ebayReq = requests.get("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR12.TRC2.A0.H0.Xblanke.TRS0&_nkw=blanket&_sacat=0")
srcEbay = ebayReq.content

ebay = BeautifulSoup(srcEbay, 'lxml')
atags = ebay.find_all('a', attrs ={"class" : "s-item__link"})
litags = ebay.find_all('li', attrs = {"class" : "s-item"})
ePrices = ebay.find_all('span', attrs = {"class" : "s-item__price"})
rangePrice = []
singlePrice = []
filterPrice = []

def getPrice():
    for price in ePrices:
        if price.text.count('$') == 2:
            price1 = float(price.text[price.text.index('$')+1:price.text.index(" ")])
            price2 = float(price.text[price.text.index('o')+3:len(price.text)])
            rangePrice.append([price1,price2])
        else:
           price3 = price.text[1:len(price.text)]
           singlePrice.append(float(price3))

getPrice()
singlePrice.sort()
rangePrice.sort()
##print(singlePrice)
print(rangePrice)
##for tag in atags:
##    print(tag.get('href'))
"""

for li_tag in litags:
    a_tags = li_tag.find('a', attrs ={"class" : "s-item__link"})
    urls.append(a_tags.attrs['href'])

print(urls)
"""
