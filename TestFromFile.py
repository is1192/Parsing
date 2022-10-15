import json
import requests as rq
from bs4 import BeautifulSoup as bs
from urllib import parse as p
url = "https://www.globus.ru/catalog/"
with open('test_catalog.txt','r') as f:
    cjs = f.read()
#print(cjs)
#js = json.loads(cjs)
cdict = eval(cjs)
#print(cdict)
urls={}
for key in cdict:
    print(key, cdict[key])
    urls[key] = p.urljoin(url, cdict[key])
    print(urls[key])

with open('test_subcatalog.txt','w') as f:
    soups={}
 #   for key in urls:
    resp = rq.get(urls['Овощи, фрукты, зелень'])
    soup = bs(resp.text, "html.parser")
    links = soup.select("pim-list__item--standart")
 #       soups[key] = soup
 #       print(str(soup))
    f.write(str(links))



