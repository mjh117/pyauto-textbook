import csv

# 파일을 열어서 reader 가져오기 --- (1)
with open('./input/items2.csv', encoding='ansi') as f:
    reader = csv.reader(f)
    # 헤더 행 건너뛰기 --- (2)
    head = next(reader)
    # 한 행씩 조사하기 --- (3)
    total = 0
    for row in reader:
        # CSV의 한 행의 요소를 각 변수에 담기 --- (4)
        name,price,cnt,subtotal = row
        print(name, price, cnt, subtotal)
        total += int(subtotal)
    # 합계를 출력
    print("합계:", total, "원")

