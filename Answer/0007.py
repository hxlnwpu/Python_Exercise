#coding=utf-8
#!usr/bin/python3

import os

filelist=os.listdir('../Answer/')
count={'comment':0,'blank':0,'code':0}
for file in filelist:
    f=open(file,'r',encoding='utf-8')
    lines=f.readlines()
    for line in lines:
        #print(line)
        if line.strip()==' ':
            count['blank']=count['blank']+1
        elif '#' in line:
            count['comment']=count['comment']+1
        else:
            count['code']=count['code']+1
print('代码行数为：'+str(count['code'])+'\n'+'空行数为：'+str(count['blank'])+'\n'+'注释行数为：'+str(count['comment']))



