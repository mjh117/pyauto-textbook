from datetime import datetime

# 2023/01/01을 지정해 객체 생성
t = datetime(2023, 1, 1)

# 날짜·시간을 표시
print(t.strftime('%Y년 %m월 %d일')) # 결과 예: 2023년 01월 01일
