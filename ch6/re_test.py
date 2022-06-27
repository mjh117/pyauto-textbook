import re

# 정규식으로 문자열 검색하기
target = r'all dog art pot apple' # --- (1)
pattern = r'a..' # --- (2)
a = re.findall(pattern, target)

# 결과 출력
print(a)
