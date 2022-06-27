import os, requests, csv, urllib
from bs4 import BeautifulSoup
from selenium import webdriver
from _MyPath import URL, DRIVER as d

# 이미지를 가져올 페이지
book_url = URL
method_url = URL+'method'

# 헤드리스 모드로 브라우저 띄우기
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(d, options=options)
driver.implicitly_wait(10)

# 책 페이지에서 책의 권 수 가져오기 --- (1)
driver.get(book_url)
print('---',driver.title,'---')
html = driver.page_source
soup = BeautifulSoup(html, 'html5lib') #--- (1a)
cnt = soup.select_one('#cnt') #--- (1b)
print("책 권수:",cnt.string)

# 메소드 페이지에서 결과 가져오기 --- (2)
driver.get(method_url)
print('---',driver.title,'---')
html = driver.page_source
soup = BeautifulSoup(html, 'html5lib') #--- (2a)
gResult = soup.select_one('#gResult') #--- (2b)
print("GET 결과:",gResult.text)

driver.quit()
