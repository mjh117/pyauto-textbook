import re

# 데이터 파일 읽어오기
with open('input/address.txt', 'rt', encoding='utf-8') as f:
    text = f.read()

# 정규식으로 텍스트 취득 
pattern = r'(㉾)(\d{5})' #--- (1)
for m in re.finditer(pattern, text): #--- (2)
    print('------------')
    print('매치 위치:', m.span())
    print('매치 문자열:', m.group(0))
    print('첫 번째 그룹:', m.group(1))
    print('두 번째 그룹:', m.group(2))
