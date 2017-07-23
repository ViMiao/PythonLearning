from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import re

page3 = "http://www.pythonscraping.com/pages/page3.html"

def getTitle(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

def getGreenName(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        return None
    bsObj = BeautifulSoup(html, "html.parser")
    nameList = bsObj.findAll("span", {"class":"green"})
    for name in nameList:
        print(name.get_text())

def getUrl(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        return None
    try:
        bsObj = BeautifulSoup(html, "html.parser")
        return bsObj
    except AttributeError as e:
        return None

def getTree(url):
    bsObj = getUrl(url)
    for child in bsObj.find("table",{"id":"giftList"}).children:
        print(child)
# getTree("http://www.pythonscraping.com/pages/page3.html")
# getGreenName("http://www.pythonscraping.com/pages/warandpeace.html")

def getImageSrc(url):
    bsObj = getUrl(url)
    images = bsObj.findAll("img", {"src": re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
    for image in images:
        print(image["src"])

getImageSrc(page3)