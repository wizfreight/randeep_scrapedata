from openpyxl import Workbook
import csv


wb = Workbook()
ws = wb.active

with open('mango.csv', 'r') as f:
    for row in csv.reader(f):
        ws.append(row)
wb.save(r"C:\Users\Bindu\Desktop\dummy.xlsx")