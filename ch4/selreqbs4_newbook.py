import re
from selenium import webdriver
import os, requests, csv, urllib, time
from bs4 import BeautifulSoup
from _MyPath import URL, DRIVER as d
import selenium_upload as upload # --- (1)

url_store = 'https://search.kyobobook.co.kr/search?keyword=%EC%A0%9C%EC%9D%B4%ED%8E%8D&gbCode=TOT&target=kyobo'
url_book = URL+'book'

# 책 스크레이핑 후 업로드하기 --- (2)
def import_book():
    # 책 리스트 가져오기 --- (2a)
    booklist = get_bookinfo()
    print(booklist)
    # 책 업로드하기 --- (2b)
    driver = webdriver.Chrome(d)
    driver.get(url_book)
    upload.login_upload(driver, booklist)

# 책 리스트 가져오기 --- (3)
def get_bookinfo():
    html = requests.get(url_store).text
    soup = BeautifulSoup(html, 'html5lib')
    slist = soup.select_one('ul.prod_list') #--- (3a)
    infolist =[]
    # li 태그 4개만 가져오기 --- (4)
    for li in slist.select('li.prod_item', limit=4):
        info ={}
        # 책 제목
        title = li.select_one('span:not([class])[id]').string.strip()
        info['title'] = title
        # 저자
        #contents = li.select_one('div.prod_author_group>div>div').contents
        #author = ' '.join(map(lambda t: t.text, list(filter(lambda c: hasattr(c, 'text'), contents))))
        # 출간일 --- (4a)
        info['date'] = li.select_one('span.date').string[:-3]
        # 가격
        info['price'] = li.select_one('span.price_normal>s').string[:-1]
        # 이미지 --- (4b)
        save_file = './output/{}.jpg'.format(re.sub(r'[/\\?%*:|"<>]', '_', title))
        info['img']= os.path.abspath(save_file)
        # 이미지 파일로 저장 --- (4c)
        src = 'https://contents.kyobobook.co.kr/pdt/' + li.img['data-kbbfn-bid'] + '.jpg'
        res = requests.get(src)
        with open(save_file, 'wb') as fp:
            fp.write(res.content)
        time.sleep(1)
        # 리스트에 딕셔너리 추가
        infolist.append(info)
    return infolist

if __name__ == '__main__':
        import_book()  
