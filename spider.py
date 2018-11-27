#coding=utf-8

import urllib.request,os
from PIL import Image

headers = {'User_Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11','Cookie':'JSESSIONID=XnL7b6hQ8SPl71fv1gjkKPD1DrJ8klFR4kmXnTdJkQ2vhgLWRr2B!1042589498'}

for i in range(1000,2001):
    response = urllib.request.Request('http://***/pyxx/grxx/xszphd/zp/xj/'+'201826'+str(i).rjust(4,'0'), headers=headers)
    img = urllib.request.urlopen(response)
    image = Image.open(img)
    image.save('../nimage/'+'201826'+str(i).rjust(4,'0')+'.jpg')


#图片重命名
filelist=os.listdir("./nimage/")
f=open('nameall','r',encoding='utf-8')
name={}
for line in f:
    line=line.split('\n')
    tmp=line[0].split(' ')
    name[str(tmp[0])]=str(tmp[1])

#匹配学号和姓名
for file in filelist:
    filename=str(file.split('.')[0])
    if(filename in name):
        os.rename('./nimage/'+file,'./himage/'+filename+'+'+name[filename]+'.jpg')
