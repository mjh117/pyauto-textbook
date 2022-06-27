import csv, openpyxl as excel

# 설정
in_file = './input/name_addr.csv'
template_file = './input/card-template.xlsx'
save_file = './output/csv_card.xlsx'

# CSV 파일 읽기 --- (1)
def read_csv(fname):
    with open(fname, encoding='ansi') as f:
        reader = csv.reader(f)
        next(reader) # 헤더 건너뛰기
        return [v for v in reader]

# 엑셀 파일 읽기 --- (2)
book = excel.load_workbook(template_file)

# 템플릿 시트 가져오기 --- (3)
sheet_tpl = book['Sheet']

# CSV에서 고객 목록을 가져오고 한 명씩 처리 --- (4)
for i, person in enumerate(read_csv(in_file)):
    # CSV의 한 행을 각 변수에 저장 --- (4a)
    name, zipnum, addr = person
    # 이름표 10개가 다 차면 시트를 추가 --- (4b)
    idx = i % 10
    if idx == 0:
        # 템플릿 시트를 복사
        sheet = book.copy_worksheet(sheet_tpl)
        sheet.title = 'Page'+str(i//10)
    # 데이터를 쓸 위치를 결정 --- (4c)
    row = 4 * (idx % 5) + 2
    col = 2 * (idx // 5) + 2
    #print(person)
    #print('idx % 5:{}, row:{}, idx // 5:{}, col:{}'.format(idx % 5, row, idx // 5, col))
    
    # 셀에 데이터 쓰기 --- (4d)
    sheet.cell(row=row+0, column=col, value=name)
    sheet.cell(row=row+1, column=col, value=zipnum)
    sheet.cell(row=row+2, column=col, value=addr)

# 템플릿 시트를 삭제하고 문서를 저장 --- (5)
book.remove(sheet_tpl)
book.save(save_file)
