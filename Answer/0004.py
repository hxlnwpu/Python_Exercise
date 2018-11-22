#coding=utf-8
#!usr/bin/python3

def getWord(filename):
    f=open(filename)
    lines=f.readlines()
    words=[]
    for line in lines:
        line=line.upper()
        line=line.replace(',',' ')
        line=line.replace('.',' ')
        #print(line)
        line=line.strip()
        wo=line.split(' ')
        words.extend(wo)
    return words

words=getWord("../Data/test1.txt")
#print(words)
count={}
for word in words:
    if(word  not in count):
        count[word]=0
for word in words:
    if(word  in count):
        count[word]= count[word]+1
for (k,v) in  count.items(): 
        print ("count[%s]=" % k,v )
    



