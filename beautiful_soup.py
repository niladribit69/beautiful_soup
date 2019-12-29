from __future__ import division
import nltk, re, pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup 
page = urlopen("https://en.wikipedia.org/wiki/Machine_learning")
conten=page.read()
conten[:1999]

soup=BeautifulSoup(conten)
print(soup.text)
//THIS ALLOWS TO GET THE TEXT FROM THE PROVIDED WEBSITE
