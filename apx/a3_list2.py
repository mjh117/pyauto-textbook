# 리스트 초기화
a_list = [0, 1, 22]

# 끝에 값 추가
a_list.append(3)
print( a_list ) # 결과→[0,1,22,3]

# 다른 리스트의 요소를 끝에 추가
a_list += [4, 5]
print( a_list ) # 결과→[0,1,22,3,4,5]

# 특정 부분을 추출
print( a_list[3:5] ) # 결과→[3,4]

# 리스트 길이 조사
print( len(a_list) ) # 결과→6

# 리스트 요소 삭제
del a_list[2]
print( len(a_list) ) # 결과→5

