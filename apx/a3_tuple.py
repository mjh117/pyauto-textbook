# 튜플 초기화
a_tuple = (0, 1, 2)

# 튜플 참조
print( a_tuple[2] ) #결과→ 2

# 튜플 길이 조사
print( len(a_tuple) ) #결과→ 3

# 2차원 튜플
b_tuple = ((7, 8), a_tuple) #결과→ (1, 2, (0, 1, 2))
print(b_tuple[1][0]) #결과→ 0

# 튜플은 변경할 수 없다
# a_tuple[2] = 22 # ←에러

