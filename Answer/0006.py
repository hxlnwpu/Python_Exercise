#coding=utf-8
#!usr/bin/python3

import os

def getWord(filename):
    f=open(filename,'r',encoding='utf-8')
    lines=f.readlines()
    words=[]
    for line in lines:
        line=line.upper()
        line=line.replace(',',' ')
        line=line.replace('.',' ')
        line=line.strip()
        wo=line.split(' ')
        words.extend(wo)
    return words

filelist=os.listdir("../Data/")   #读取文件夹下所有文件名
for filename in filelist:
    print(filename)
    words=getWord("../Data/"+filename)
    count={}
    for word in words:
        if(word  not in count):
            count[word]=0
    for word in words:
        if(word  in count):
            count[word]= count[word]+1
    for (k,v) in  count.items(): 
        print ("count[%s]=" % k,v )
    print(filename+"中最重要的词是："+max(count,key=count.get))



    
