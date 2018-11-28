#coding=utf-8

import urllib.request,os
from bs4 import BeautifulSoup

headers = {'User_Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'}

request = urllib.request.Request("http://www.runoob.com/python3/python3-file-methods.html", headers=headers)
response = urllib.request.urlopen(request)
#print(response.info())
f=open('../Data/example.html','r',encoding='utf-8')
#f.write(str(response.read().decode('utf-8')))
html=f.read()
soup = BeautifulSoup(html, 'html.parser')
print(soup.get_text())
