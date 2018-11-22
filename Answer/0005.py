#coding=utf-8
#!usr/bin/python3

import os
from PIL import Image

filelist=os.listdir("../image/0005")   #读取文件夹下所有文件名
os.mkdir("../image/0005h")   #c创建文件夹
for i in range(len(filelist)):
    #print(filelist[i])
    pass
size = (128, 128)
for i in range(len(filelist)):
    im=Image.open("../image/0005/"+filelist[i])
    im.thumbnail(size)
    #im.show()
    im.save("../image/0005h/"+(filelist[i].split('.'))[0]+".jpeg","JPEG")
    
