from datetime import datetime

# 현재 시각을 받아와서 특정 형식으로 출력하기
t = datetime.now()
fmt = t.strftime('%Y년%m월%d일 %H시%M분%S초')
print(fmt)

