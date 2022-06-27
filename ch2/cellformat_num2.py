import openpyxl as xl
book = xl.Workbook()
sheet = book.active

#헤더 설정
sheet.append(["서식", "예시 1", "예시 2"])

# 셀에 값과 서식을 지정하는 함수 정의 --- (1)
def set_cell(cname, value, fmt):
    c = sheet[cname]
    c.value = value
    c.number_format = fmt    

# 천 단위 구분 기호(,) 설정 --- (2)
digit3_fmt = '#,##0'
sheet["A2"] = digit3_fmt
set_cell("B2", 12345, digit3_fmt)
set_cell("C2", 123456789, digit3_fmt)

# 통화 기호 설정 --- (3)
cur_fmt = '"₩"#,##0;"₩"-#,##0' #--- (3a)
sheet["A3"] = cur_fmt
set_cell("B3", 12345, cur_fmt) # 양수 예시
set_cell("C3", -12345, cur_fmt) # 음수 예시

# 음수 값을 붉은 색으로 표시하고 마이너스 기호를 △로 나타내기 --- (4)
num_fmt = '#,##0;[red]"△ "#,##0' #--- (4a)
sheet["A4"] = num_fmt
set_cell("B4", 12345, num_fmt) # 양수 예시
set_cell("C4", -12345, num_fmt) # 음수 예시

# 파일 저장
book.save("output/cellformat_num2.xlsx")
