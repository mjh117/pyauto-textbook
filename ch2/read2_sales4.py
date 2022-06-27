import openpyxl as excel

# 매출 내역 문서를 열고 시트 가져오기
book = excel.load_workbook(
    "input/monthly_sales.xlsx", data_only=True)
sheet = book.active

# A3부터 F999(적당히 큰 범위)를 얻기 --- (1)
rows = sheet["A3":"F999"]
for row in rows:
    # 셀의 값을 리스트로 얻기 --- (2)
    values = [cell.value for cell in row]
    # 비어있는 셀이면 읽기를 종료 --- (3)
    if values[0] is None: break
    # 리스트를 출력
    print(values)
