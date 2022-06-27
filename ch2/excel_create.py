# 라이브러리 불러오기 --- (1)
import openpyxl as excel

# 새 워크북 생성 --- (2)
book = excel.Workbook()

# 활성화된 워크시트 가져오기 --- (3)
sheet = book.active

# A1 셀에 값 입력 --- (4)
sheet["A1"] = "안녕하세요"

# 파일 저장 --- (5)
book.save("./output/hello.xlsx")
