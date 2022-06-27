import openpyxl as excel, json

# 입출력 파일을 지정
in_file = './output/merge_files.xlsx'
out_file = './output/split_data.json'

# 메인 처리 --- (1)
def split_data():
    # 입력 파일을 분류해 딕셔너리에 저장 --- (1a)
    users = read_and_split(in_file)
   # 고객별 데이터 집계 --- (1b)
    result = {}
    for name, rows in users.items():
        result[name] = calc_user(rows)
        print(name, result[name]['total'])
    # 출력 파일(.json)에 결과를 저장 --- (1c)
    with open(out_file, "wt") as fp:
        json.dump(result, fp)

# 고객명을 키로 하는 딕셔너리를 반환 --- (2)
def read_and_split(in_file):
    users = {} # 딕셔너리 변수 초기화
    sheet = excel.load_workbook(in_file).active #문서를 열고 시트 가져오기
    # 시트의 모든 행 읽기 --- (2a)
    for row in sheet.iter_rows(): 
        # 행 데이터를 리스트에 저장 --- (2b)
        values = [col.value for col in row]
        # 고객명이 처음 나왔다면 딕셔너리에 요소 추가(키:고객명, 값:빈 리스트)
        name = values[1] 
        if name not in users: users[name] = []
        # 행 데이터를 딕셔너리의 값인 리스트에 추가 --- (2c)
        users[name].append(values)
    return users

# 고객 한 명의 집계 결과 반환 --- (3)
def calc_user(rows):
    total = 0 # 총 금액을 저장할 int 변수
    items = [] # 거래 내역을 저장할 리스트 변수
    # 금액 집계하기 --- (3a)
    for row in rows:
        # 청구서에 필요한 항목만 추출·가공해 리스트에 추가
        date, _, item, cnt, price, _ = row
        date_s = date.strftime('%m/%d') # --- (3b)
        items.append([date_s, item, cnt, price])
        # 총 금액 계산 --- (3c)
        total += cnt * price
    # 거래 내역 및 거래 금액을 딕셔너리로 반환
    return {'items': items, 'total': total}

if __name__ == "__main__":
    split_data() # 메인 처리를 실행
