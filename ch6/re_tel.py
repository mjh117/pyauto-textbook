import re
# 타겟 문자열
tel = r'[전화] 000-1111-2222'

# 검색 패턴
pattern = r'(\d+)-(\d+)-(\d+)' #--- (1)

# 치환 문자열
rep = r'(\1) \2 - \3' #--- (2)

# 치환하기
print(re.sub(pattern, rep, tel)) #--- (3)
