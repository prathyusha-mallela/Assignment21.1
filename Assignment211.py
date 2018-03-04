# -*- coding: utf-8 -*-
"""
Assignment 21.1
@Author: Prathyusha Mallela
"""
from bs4 import BeautifulSoup
import urllib.request;
import nltk;
response=urllib.request.urlopen('http://php.net');
html=response.read();
soup=BeautifulSoup(html,"html5lib");
text=soup.get_text(strip=True);
#print(text);
tokens=[t for t in text.split()];
print(tokens);
freq=nltk.FreqDist(tokens);
for key,val in freq.items():
    print(str(key)+':'+str(val));
freq.plot(20,cumulative=False);