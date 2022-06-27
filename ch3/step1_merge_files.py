import openpyxl as excel
import glob

# 대상 폴더명과 저장할 파일명을 지정
target_dir = './input/salesbooks'
save_file = './output/merge_files.xlsx'

# 메인 처리 --- (1)
def merge_files():
    # 데이터를 취합할 워크북 생성
    book = excel.Workbook()
    main_sheet = book.active
    # 시트에 데이터 취합하기
    enumfiles(main_sheet)
    # 워크북을 파일로 저장 
    book.save(save_file)

# 대상 폴더에서 파일 조회하기 --- (2)
def enumfiles(main_sheet):
    # 엑셀 파일 목록 받아오기 --- (2a)
    files = glob.glob(target_dir + '/*.xlsx')
    # 각 엑셀 문서를 차례로 읽기 --- (2b)
    for fname in files:
        read_book(main_sheet, fname)

# 문서를 열어서 내용을 시트에 복사하기 --- (3)
def read_book(main_sheet, fname):
    print("read:", fname)
    # 엑셀 문서 열기 --- (3a)
    book = excel.load_workbook(fname, data_only=True)
    sheet = book.active
    # 매출 데이터가 있는 범위 읽기 --- (3b)
    rows = sheet["A4":"F999"]
    for row in rows:
        # 행을 리스트에 저장하기 --- (3c)
        values = [cell.value for cell in row]
        if values[0] is None: break
        print(values)
        # 메인 시트에 한 행 복사 --- (3d)
        main_sheet.append(values)

# 메인 프로그램 실행 --- (4)
if __name__ == "__main__":
    merge_files()
