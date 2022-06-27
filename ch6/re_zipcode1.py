import re

# 데이터 파일 읽어오기 --- (1)
with open('input/address.txt', 'rt', encoding='utf-8') as f:
    text = f.read()

# 정규식으로 텍스트 얻기 --- (2)
a = re.findall(r'㉾\d{5}', text)
print(a)
