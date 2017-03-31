from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://qwme.org/")
bsObj = BeautifulSoup(html.read(), "html.parser")
print(bsObj.h1)
print("=====")
print(html.read)
