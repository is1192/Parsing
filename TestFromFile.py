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

with open('test_subcatalog.txt','a') as f:
    f.truncate(0)
  #  soups={}
 #   for key in urls:
#    resp = rq.get(urls['Овощи, фрукты, зелень'],params={'page':'2'})
    resp = rq.get(urls['Овощи, фрукты, зелень'])
    soup = bs(resp.text, "html.parser")
#    f.write(resp.text)
    pcount = int(soup.select_one("a.pim-list-count__element-select").text.strip())
    print(pcount)
    param = {'page':str(pcount)}
    print(param)
    result = []
    for p in range(pcount,pcount+1):
        param={'page':str(p)}
        print(param)
        resp = rq.get(urls['Овощи, фрукты, зелень'], params=param)
        links = bs(resp.text, "html.parser").select("div.pim-list__item-content")
        for link in links:
            name=link.select_one("div.pim-list__item-title").text.strip()
            price = int(link.select_one("span.pim-list__item-price-actual-main").text.strip()) + int(link.select_one("span.pim-list__item-price-actual-sub").text.strip())/100
            #print(name, price)
            result.append({'name':name, 'price':price})
        print(result)
        f.write(json.dumps(result,ensure_ascii=False, indent=2))
 #       soups[key] = soup
 #       print(str(soup))
  #  idict={}
  #  for link in links:
  #      if link.text.strip():
   #         idict[link.text.strip()] = link.attrs['data-full-text']
   # ijs = json.dumps(idict, ensure_ascii=False, indent=2)
    #f.write(ijs)



