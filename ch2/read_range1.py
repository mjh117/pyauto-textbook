import openpyxl as excel

# 워크북을 열어서 시트 가져오기 --- (1)
book = excel.load_workbook("output/write_cellname.xlsx")
sheet = book.active

# 연속 데이터를 읽어와서 출력하기 --- (2)
for y in range(2, 5):
    r = []
    for x in range(2, 5):
        v = sheet.cell(row=y, column=x).value
        r.append(v)
    print(r)
