import openpyxl as excel

# 새 워크북 생성 --- (1)
book = excel.Workbook()
# 활성화된 워크시트 가져오기 --- (2)
sheet = book.active

# 시트에 구구단 숫자 채우기 --- (3)
for y in range(1,10):
    for x in range(1,10):
        # y행 x열 셀을 취득 --- (4)
        cell = sheet.cell(row=y, column=x)
        # 셀에 데이터 쓰기 --- (5)
        cell.value = x * y

# 파일 저장 --- (6)
book.save("output/write_9x9.xlsx")

