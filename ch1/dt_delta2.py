from datetime import datetime

# 취침 시간과 기상 시간을 지정 ---(1)
sleep_t = datetime(2023, 1, 1,22, 0, 0)
wakeup_t = datetime(2023, 1, 2, 8,30, 0)

# 시간 계산 ---(2)
delta = wakeup_t - sleep_t
sec = delta.seconds # 수면 시간을 초로 환산 ---(3)
hours = sec / (60 * 60)

# 결과 표시 ---(4)
print('수면 시간은'+str(hours)+'시간입니다.')
