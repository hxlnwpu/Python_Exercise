#coding='utf-8'

import os,xlsxwriter

path=r"C:\Workspace\Python\Python_Exercise\Data\numbers.txt"
workbook = xlsxwriter.Workbook(r"C:\Workspace\Python\Python_Exercise\Data\numbers.xlsx")
worksheet = workbook.add_worksheet()
row=0
col=0
with open(path,'r',encoding='utf-8') as studentText:
    lines=studentText.readlines()
    for line in lines:
        line=line.strip("\n")
        line=line.strip(" ")
        line=line.strip('\t')
        if line=='[' or line=="]":
            pass
        else:
            line=line.split(',')
            num1=line[0].strip("[").strip(',')
            num2=line[1].strip(",")
            num3=line[2].strip(",").strip(']')
            worksheet.write(row,col,num1)
            worksheet.write(row,col+1,num2)
            worksheet.write(row,col+2,num3)
            row+=1
workbook.close()
