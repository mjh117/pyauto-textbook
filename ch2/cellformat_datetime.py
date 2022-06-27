import openpyxl as xl
# 워크북을 만들고 시트 가져오기
book = xl.Workbook()
sheet = book.active

# A1,B1,C1,D1에 동일한 일시를 설정 --- (1)
import datetime
dt = datetime.datetime(
      year=2023, month=4, day=5,
      hour=11, minute=22, second=33)
sheet.append([dt, dt, dt, dt])

# 날짜를 'yyyy/mm/dd'형식으로 지정 --- (2)
sheet["A1"].number_format = 'yyyy\/mm\/dd'

# 날짜를 'yyyy년 mm월 dd일'형식으로 지정 --- (3)
sheet["B1"].number_format = 'yyyy년 mm월 dd일'

# 시간을 'hh:mm:ss'형식으로 지정 --- (4)
sheet["C1"].number_format = 'hh:mm:ss'

# 날짜와 시간을 'mm/dd hh:mm:ss'형식으로 지정 --- (5)
sheet["D1"].number_format = 'mm\/dd hh:mm:ss'

# 파일 저장
book.save("output/cellformat_datetime.xlsx")
