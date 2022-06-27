# 이름을 설정하는 함수
def set_name(new_name):
    global name
    name = new_name

# 인사를 출력하는 함수
def say_hello():
    global name
    print(name, '님 안녕하세요!')

# 함수 사용하기
set_name('제이펍')
say_hello()

# 결과→ 제이펍 님 안녕하세요!

