#coding='utf-8'

from xlrd import open_workbook

path=r"C:\Workspace\Python\Python_Exercise\Data\net.xls"
wb = open_workbook(path)
time=0
for s in wb.sheets():
    for row in range(11):
        if row>0:
            time=time+int(s.cell(row,9).value)
print(time)