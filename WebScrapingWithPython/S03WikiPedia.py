from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError
import re

def getBsObj(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        return None
    try:
        bsObj = BeautifulSoup(html, "html.parser")
        return bsObj
    except AttributeError as e:
        print('Unable to get the HTML')
        return None

bsObj = getBsObj("http://en.wikipedia.org/wiki/Kevin_Bacon")
try:
    for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
        if 'href' in link.attrs:
            print(link.attrs['href'])
except bsObj is None as e:
    print('bsObj is None')
