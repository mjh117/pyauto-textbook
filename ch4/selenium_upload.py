from selenium import webdriver
import os, time, datetime
from _MyPath import URL, DRIVER as d
import selenium_login as login #로그인 모듈 추가--- (1)

#입력 정보 지정--- (2)
url = URL+'book'
bookinfo1 = {
    'title':'그림으로 공부하는\TCP/IP 구조',
    'date':'2021년 10월',
    'price':'30,000',
    'img':os.path.abspath('./input/book_img1.jpg')
    }
bookinfo2 = {
    'title':'유튜브 영상 편집을 위한\파이널 컷 프로 X',
    'date':'2021년 09월',
    'price':'29,800',
    'img':os.path.abspath('./input/book_img2.jpg')
    }
booklist = [bookinfo1, bookinfo2]

# 메인 처리 --- (3)
def mainpro():
    # 사이트 접속
    driver = webdriver.Chrome(d)
    driver.get(url)
    driver.implicitly_wait(10)
    # 로그인 및 책 업로드 --- (4)
    login_upload(driver, booklist)
    # 드라이버 종료
    time.sleep(3)
    driver.quit()

# 로그인 성공하면 업로드 시작 --- (5)
def login_upload(driver, booklist) :
    if login.try_login(driver):
        add_booklist(driver, booklist)

# 책 리스트 추가 --- (6)
def add_booklist(driver, booklist):
    # 책 권수 확인  --- (6a)
    cnt = count_book(driver)
    cnt_after = cnt + len(booklist)
    # 책 추가하기  --- (6b)
    for bookinfo in booklist:
        add_book(driver, bookinfo)
        print('<{}> 추가'.format(bookinfo['title']))
        time.sleep(1)
    # 책 권수로 확인  --- (6c)
    if(count_book(driver)==cnt_after):
        print('책 추가 성공')

# 현재 책 권수 확인 --- (7)
def count_book(driver):
    div = driver.find_element_by_id('cnt') #--- (7a)
    num = div.text
    print('현재 '+num+'권')
    return int(num) #--- (7b)

# 책 한 권 추가 --- (8)
def add_book(driver, bookinfo):
    driver.find_element_by_css_selector('label.mainbtn').click() #--- (8a)
    driver.find_element_by_name('ntitle').send_keys(bookinfo['title']) #--- (8b)
    driver.find_element_by_name('nprice').send_keys(bookinfo['price'])
    driver.find_element_by_name('ndate').send_keys(bookinfo['date'])
    driver.find_element_by_name('file').send_keys(bookinfo['img'])
    driver.find_element_by_css_selector('label.subbtn').click() #--- (8c)
        
if __name__ == '__main__':
        mainpro()  
