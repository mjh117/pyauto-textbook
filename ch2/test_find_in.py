# 대상이 되는 문자열
target = '0123456789'

# find로 검색 --- (1)
i = target.find('56')
if i >= 0:
    print('(*1) 0부터 시작해서',i,'번째에 있습니다.')
else:
    print('(*1) 문자열이',target,'안에 없습니다.')

# in으로 검색 --- (2)
if '56' in target:
    print('(*2) 문자열이',target,'안에 있습니다.')
else:
    print('(*2) 문자열이',target,'안에 없습니다.')
