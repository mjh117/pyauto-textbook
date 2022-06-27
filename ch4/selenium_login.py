from selenium import webdriver
import os, time, datetime
from selenium.webdriver.common.by import By
from _MyPath import URL, DRIVER as d

# URL 및 로그인 정보 지정 --- (1)
url = URL+'book'
user_id, user_pw = ('ID', 'PW')

# 메인 처리 --- (2)
def print_cookie():
    # 사이트 접속하기 --- (3)
    driver = webdriver.Chrome(d)
    driver.implicitly_wait(10) #--- (3a)
    driver.get(url)
    # 로그인 후 쿠키 출력 --- (4)
    result = try_login(driver)
    if result:
        print(driver.get_cookie('session')) #--- (4a)
    # 드라이버 닫기
    time.sleep(5)
    driver.quit()

# 로그인하기 --- (5)
def try_login(driver):
    # 로그인 페이지 열기 --- (5a)
    driver.find_element_by_link_text('로그인').click()
    # 아이디, 패스워드 입력 --- (5b)
    user = driver.find_element_by_name('id')    
    user.send_keys(user_id)
    pw = driver.find_element_by_name('pw')
    pw.send_keys(user_pw)
    pw.submit()
    # 로그인 성공 확인 --- (6)
    for i in range(10):
        if driver.current_url == url: #--- (6a)
            print("로그인 성공")
            return True
        time.sleep(1)
    print("로그인 실패")
    return False    

if __name__ == '__main__':
    print_cookie()
