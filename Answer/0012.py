#coding='utf-8'

import os

f=open(r'C:\Workspace\Python\Python_Exercise\Data\filtered_words.txt','r',encoding='utf-8')
lines=f.readlines()
filterwords=[]
for line in lines:
    line=line.strip()
    filterwords.append(line)

sentence=input("请输入：")

for words in filterwords:
    if words in sentence:                           
        replace_str='*'*len(words)
        sentence=sentence.replace(words,replace_str)   #replace返回的是sentence的副本，并未直接修改sentence，所以需要重新赋值给sentence
print(sentence)

