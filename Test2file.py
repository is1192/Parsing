import requests as rq
from bs4 import BeautifulSoup as bs
import json

def link2dict(url,obj_str):
    import requests as rq
    from bs4 import BeautifulSoup as bs
    resp = rq.get(url)
    soup = bs(resp.text, "html.parser")
    links = soup.select(obj_str)
    return links

url = "https://www.globus.ru/catalog/"
with open('test_catalog.txt','w') as f:
    links=link2dict(url,"a.pim-list-sections__item")
    cdict = {}
    for link in links:
        if link.text.strip():
            cdict[link.text.strip()] = link.attrs['href']
            cjs = json.dumps(cdict, ensure_ascii=False, indent=2)
    f.write(cjs)

