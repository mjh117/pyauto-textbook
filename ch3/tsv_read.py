import csv

# 파일 열기 --- (1)
with open('./input/items3.tsv', encoding='utf-8') as f:
    # 구분 기호를 지정하여 읽기 --- (2)
    reader = csv.reader(f, delimiter='\t')
    # 읽은 데이터를 화면에 출력
    for row in reader:
        print(row)
