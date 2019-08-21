import requests
from bs4 import BeautifulSoup

ebayReq = requests.get("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR12.TRC2.A0.H0.Xblanke.TRS0&_nkw=blanket&_sacat=0")
srcEbay = ebayReq.content

ebay = BeautifulSoup(srcEbay, 'lxml')
litags = ebay.find_all('li', attrs = {"class" : "s-item"})
for li in litags:
    atag = li.findChild('a',href = True)
    print(atag)
"""

for li_tag in litags:
    a_tags = li_tag.find('a', attrs ={"class" : "s-item__link"})
    urls.append(a_tags.attrs['href'])

print(urls)
"""
"""
htags = amazon.find_all("h2")
print(htags)

urls = []
for h2_tag in amazon.find_all("h2"):
    a_tag = h2_tag.find("a")
    urls.append(a_tag.attrs['href'])
print(urls)
"""
