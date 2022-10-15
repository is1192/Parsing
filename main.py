# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

    # Use a breakpoint in the code line below to debug your script.
    # Press Ctrl+F8 to toggle the breakpoint.

from bs4 import BeautifulSoup as bs
import requests as rq
import json
url = "https://www.globus.ru/catalog/"
resp = rq.get(url)
soup = bs(resp.text,"html.parser")
links = soup.select("a.pim-list-sections__item")
cat = []
cdict = {}
print(cat)
for link in links:
    if link.text.strip():
        cat.append(link.text.strip())
        cdict[link.text.strip()] = link.attrs['href']
        cjs=json.dumps(cdict, ensure_ascii=False, indent=2)
print(cat)
print(cdict)
print(cjs)


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
