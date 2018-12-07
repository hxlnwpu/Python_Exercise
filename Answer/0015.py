#coding='utf-8'

import os,xlsxwriter,json

path=r"C:\Workspace\Python\Python_Exercise\Data\city.txt"
workbook = xlsxwriter.Workbook(r"C:\Workspace\Python\Python_Exercise\Data\city.xlsx")
worksheet = workbook.add_worksheet()
row=0
col=0
with open(path,'r',encoding='utf-8') as studentText:
    lines=studentText.readlines()
    for line in lines:
        line=line.strip("\n")
        line=line.strip(" ")
        line=line.strip(',')
        line=line.strip('\t')
        if line=='{' or line=="}":
            pass
        else:
            line=line.split(':')
            num=line[0].strip(" ").strip('"')
            data=line[1].strip(" ").strip('"')
            worksheet.write(row,col,num)
            worksheet.write(row,col+1,data)
            row+=1
workbook.close()
