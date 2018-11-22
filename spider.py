#coding=utf-8

import urllib.request,os
from PIL import Image

headers = {'User_Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11','Cookie':'JSESSIONID=3r1Pb2LpF2LvW0L7NynWhQJ4nL1n2S6GwtrX6psy03d72tQ4ThMG!1042589498'}

for i in range(2035,2173):
    response = urllib.request.Request('http://***/pyxx/grxx/xszphd/zp/xj/'+'201820'+str(i).rjust(4,'0'), headers=headers)
    img = urllib.request.urlopen(response)
    image = Image.open(img)
    image.save('./image/'+'201820'+str(i).rjust(4,'0')+'.jpg')
filelist=os.listdir("./image/")
f=open('name','r',encoding='utf-8')
name={}
for line in f:
    tmp=line.split()
    name[str(tmp[0])]=str(tmp[1])

for file in filelist:
    filename=file.split('.')
    os.rename('./image/'+file,'./nimage/'+filename+'+'+name[filename]+'.jpg')
