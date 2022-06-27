import openpyxl as excel

book = excel.Workbook()
sheet = book.active

# 셀 이름에서 행·열 번호 얻기 --- (1)
cell = sheet["C2"]
(row, col) = (cell.row, cell.column)
print("C2=({},{})".format(row, col))

# 행·열 번호에서 셀 이름 얻기 --- (2)
cell = sheet.cell(row=2, column=3)
cdt = cell.coordinate
print("(2,3)={}".format(cdt))



