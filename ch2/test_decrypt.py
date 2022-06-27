import msoffcrypto
import openpyxl as excel

# 암호화된 문서를 입력 파일로 지정 --- (1)
fin = open("input/monthly_sales_encrypt.xlsx", "rb")
msfile = msoffcrypto.OfficeFile(fin)

# 패스워드 전달 --- (2)
msfile.load_key(password="abcd")

# 복호화한 파일을 저장 --- (3)
fout = open("output/monthly_sales_decrypt.xlsx", "wb")
msfile.decrypt(fout)

# 복호화한 파일을 열어서 내용 가져오기 --- (4)
book = excel.load_workbook("output/monthly_sales_decrypt.xlsx",data_only=True)
sheet = book.active
for row in sheet["A2:F99"]:
    values = [v.value for v in row]
    if values[0] is None: break
    print(values)

