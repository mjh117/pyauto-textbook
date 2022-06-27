import openpyxl as excel

# 새 워크북 생성하고 워크시트 가져오기
book = excel.Workbook()
sheet = book.active

# 시트에 99×99 숫자 채우기  --- (1)
for y in range(1,100):
    for x in range(1,100):
        # y행 x열 셀을 취득하고 데이터 쓰기 --- (2)
        cell = sheet.cell(y, x)
        cell.value = x * y

# 파일 저장
book.save("output/write_99x99.xlsx")

