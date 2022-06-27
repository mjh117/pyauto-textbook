import openpyxl as excel

# 워크북을 읽을 때 수식이 계산된 값을 읽어오도록 지정
book = excel.load_workbook(
  "input/monthly_sales.xlsx",
  data_only=True)

sheet = book.active

# A3에서 F9 범위의 셀 가져오기 --- (1)
rows = sheet["A3":"F9"]
for row in rows:
    # 셀의 값을 리스트에 저장 --- (2)
    values = [cell.value for cell in row]
    # 리스트 출력 --- (3)
    print(values)
