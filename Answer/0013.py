#coding=utf-8

import os,urllib,string,random
from bs4 import BeautifulSoup
from pathlib import Path
from PIL import Image


url=r"http://tieba.baidu.com/p/2166231880"
webdata=urllib.request.urlopen(url)
soup=BeautifulSoup(webdata.read(),"html.parser")
for link in soup.find_all("img"):
    imgurl=link.get("src")
    imgdata=urllib.request.urlopen(imgurl).read()
    with open("../test/"+imgurl[-11:],"wb") as img:
        img.write(imgdata)

