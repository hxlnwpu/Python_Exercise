#coding='utf-8'

from openpyxl import Workbook
import os,xlsxwriter

path=r"C:\Workspace\Python\Python_Exercise\Data\student.txt"
workbook = xlsxwriter.Workbook(r"C:\Workspace\Python\Python_Exercise\Data\student.xlsx")
worksheet = workbook.add_worksheet()
row=0
col=0
with open(path,'r',encoding='utf-8') as studentText:
    lines=studentText.readlines()
    for line in lines:
        line=line.rstrip("\n")
        line=line.rstrip(" ")
        line=line.rstrip(',')
        line=line.lstrip('\t')
        if line=='{' or line=="}":
            pass
        else:
            line=line.split(':')
            data=line[1].split(',')
            worksheet.write(row,col,line[0].strip('"'))
            worksheet.write(row,col+1,data[0].lstrip('[').strip('"'))
            worksheet.write(row,col+2,data[1])
            worksheet.write(row,col+3,data[2])
            worksheet.write(row,col+4,data[3].rstrip(']'))
            row+=1
workbook.close()