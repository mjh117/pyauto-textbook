# 주문을 출력하는 함수
def print_order(item, quantity, price, name, address):
    print('제품:',item, '| 수량:',quantity,'| 단가:',price,'| 이름:',name,'| 주소:',address)

# 위치 인수 사용 --- (*1)
print_order('감귤', 15, 500, '김철수', '서울')

# 키워드 인수 사용 --- (*2)
print_order(name='이영희', address= '부산', item='사과', quantity= 10, price = 1000)

# 위치 인수와 키워드 인수를 함께 사용 : 정상 작동 --- (*3)
print_order('딸기', 20, name='박현주', address= '대구', price = 1500)

# 위치 인수와 키워드 인수를 함께 사용 : 에러 --- (*4)
#print_order('단감', 30, price='2000', name='강민규', '경기')
