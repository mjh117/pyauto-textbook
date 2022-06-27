# 딕셔너리 초기화
a_dict = {'apple': 280, 'banana': 150, 'orange': 220}

# 값 추가 및 변
a_dict['grape'] = 400
a_dict['apple'] = 300

# 값 참조
print( a_dict['apple'] ) # 결과→300

# 길이 조사
print( len(a_dict) ) #결과→4

# 데이터 삭제
del a_dict['banana']
print( 'banana' in a_dict ) # 결과→False
