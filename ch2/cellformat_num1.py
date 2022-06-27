import openpyxl as xl
# 워크북을 생성하고 시트 가져오기
book = xl.Workbook()
sheet = book.active

# A1, B1, C1에 동일한 값을 설정 --- (1)
val = 3.14159
sheet.append([val, val, val])

# 소수점 이하를 생략하여 표시 --- (2)
sheet["A1"].number_format = '0'
# 소수점 이하 둘 째 자리까지 표시 --- (3)
sheet["B1"].number_format = '0.00'
# 소수점 이하 넷 째 자리까지 표시 --- (4)
sheet["C1"].number_format = '0.0000'

# 파일 저장
book.save("output/cellformat_num1.xlsx")
