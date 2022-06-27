# 딕셔너리 초기화
a_dict = {'apple': 280, 'banana': 150, 'orange': 220}

# 키 포함 여부 확인
print( 'banana' in a_dict ) # 결과→True
print( 'mango' in a_dict ) # 결과→False

# 키의 목록 조회
print( a_dict.keys() ) 
# 결과→dict_keys(['apple', 'banana', 'orange'])

# 키와 값 목록 조회
print(a_dict.items())
# 결과→dict_items([('apple', 280), ('banana', 150), ('orange', 220)])

# 딕셔너리에 다른 딕셔너리 데이터를 추가
a_dict.update({'grape': 900, 'pear': 450})
print(a_dict['grape']) # 결과→900

# 2차원 딕셔너리
b_dict = {'딕셔너리1':a_dict, '딕셔너리2':{'grape': 900, 'pear': 450}}
print(b_dict['딕셔너리2']['pear']) #결과→450
