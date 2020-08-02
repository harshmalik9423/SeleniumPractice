import openpyxl

path = r"C:\Users\harsh\Desktop\test2.xlsx"
workbook = openpyxl.load_workbook(path)
sheet = workbook.active

for r in range(1,6):
    for c in range(1,4):
        sheet.cell(row=r, column=c).value = "init"

workbook.save(path)