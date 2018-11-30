#coding='utf-8'

import os

f=open('../Data/filtered_words.txt','r',encoding='utf-8')
lines=f.readlines()
filterwords=[]
for line in lines:
    line=line.strip()
    filterwords.append(line)
words=input("请输入关键词：")
if words in filterwords:
    print("Freedom")
else:
    print("Human Rights")
