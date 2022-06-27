import openpyxl as excel

# 워크북을 열어서 시트 가져오기
book = excel.load_workbook("output/write_cellname.xlsx")
sheet = book.active

# 연속으로 셀의 값 얻기
for row in sheet["B2":"D4"]:
    print([c.value for c in row])
