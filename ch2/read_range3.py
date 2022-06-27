import openpyxl as excel

# 워크북을 열어서 시트 가져오기
book = excel.load_workbook("output/write_cellname.xlsx")
sheet = book.active

# 이터레이터 얻기 --- (1)
it = sheet.iter_rows(
        min_row=2, min_col=2,
        max_row=4, max_col=4)

# for문과 조합하여 셀의 값 얻기 --- (2)
for row in it:
    r = []
    for cell in row:
        r.append(cell.value)
    print(r)

