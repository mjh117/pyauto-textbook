from datetime import datetime

# D-day 날짜를 지정 --- (1)
dday = datetime(2025, 4, 13)
# 오늘 날짜를 지정 --- (2)
now = datetime.now()
# 일수 계산 --- (3)
delta = dday - now
# 결과 출력 --- (4)
print('앞으로'+str(delta.days+1)+'일 남았습니다')
