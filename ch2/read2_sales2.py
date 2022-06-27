import openpyxl as excel

# 매출 내역 문서를 열고 시트 가져오기
book = excel.load_workbook("input/monthly_sales.xlsx")
sheet = book.active

# A3에서 F9 범위의 셀 가져오기 --- (1)
rows = sheet["A3":"F9"]
for row in rows:
    # 셀의 값을 리스트에 저장 --- (2)
    values = [] 
    for cell in row:
        values.append(cell.value)
    # 리스트 출력 --- (3)
    print(values)
