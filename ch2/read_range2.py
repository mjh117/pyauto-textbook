import openpyxl as excel

# 워크북을 열고 시트를 가져오기
book = excel.load_workbook("output/write_cellname.xlsx")
sheet = book.active

# 연속 데이터를 읽어서 출력하기
for row in sheet["B2":"D4"]:
    r = []
    for cell in row:
        r.append(cell.value)
    print(r)
