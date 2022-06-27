import os, time, requests, urllib
from bs4 import BeautifulSoup
from _MyPath import URL
import reqbs4_2_CSV as CSV #--- (1)

# URL 및 로그인 정보 --- (2)
url = URL+'book'
login_data = {'id':'ID', 'pw':'PW'}

# 책 정보 지정 --- (3)
img_file ='./input/book_img1.jpg'
bookinfo = {
    'ntitle':'그림으로 공부하는\TCP/IP 구조',
    'ndate':'2021년 10월',
    'nprice':'30,000',
    }

# 메인 처리 --- (4) 
def main_book():
    # Requests 세션 객체 생성 --- (5) 
    session = requests.Session()
    
    # Soup 객체에서 URL 얻기1 --- (6) 
    res = session.get(url)
    soup = BeautifulSoup(res.text, 'html5lib')
    login_url = CSV.get_link(soup, '로그인') #--- (6a) 
    csv_url = CSV.get_link(soup, 'CSV') 
    print('[책 권수]현재 %s 권'%len(soup.select('.item'))) #--- (6b) 
    
    # 로그인 --- (7) 
    res_login = try_login(session, login_url)
    if not res_login : return

    # Soup 객체에서 URL 얻기2 --- (8) 
    soup_login = BeautifulSoup(res_login.text, 'html5lib')
    form_url = soup_login.form['action'] # --- (8a)
    add_url  = CSV.get_abs(form_url, url, '책 추가')
    reset_url = CSV.get_link(soup_login, '초기화') # --- (8b)
    
    # 책 초기화 후 책 추가 --- (9) 
    try_reset(session, reset_url)
    try_add(session, add_url)
    
    # CSV 다운로드 --- (10) 
    CSV.try_download(csv_url)

# 로그인 및 결과 확인 --- (11) 
def try_login(session, login_url):
    res = session.post(login_url, data=login_data) # --- (11a) 
    if(res.ok and res.url == url) : # --- (11b) 
        print('[%s] 로그인 성공'%res.status_code)
        cookie = session.cookies.get('session') # --- (11c)
        print('{name=session,: value=%s}'%cookie) 
        return res
    else : 
        print('[%s] 로그인 실패'%res.status_code)
    return False

# 책 초기화하기 --- (12) 
def try_reset(session, reset_url):
    res = session.get(reset_url)
    if res.ok :
        print('[%s] 책 초기화 성공'%res.status_code)
    else :
        print('[%s] 책 초기화 실패'%res.status_code)

# 책 추가하기 --- (13) 
def try_add(session, add_url):
    res = session.post(add_url, files={'file':open(img_file,'rb')},data=bookinfo)
    if res.ok :
        print('[%s] 책 추가 성공'%res.status_code)
    else:
        print('[%s] 책 추가 실패'%res.status_code)
            
if __name__ == '__main__':
    main_book()
