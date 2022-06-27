from datetime import datetime, timedelta

# 기준 날짜 지정--- (1)
base_t  = datetime(2025, 2, 27)
# 3일 후를 계산 --- (2)
t = base_t + timedelta(days=3)
# 결과 표시 --- (3)
print(t.strftime('%Y/%m/%d'))

