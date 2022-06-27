import os, requests, csv, urllib
from bs4 import BeautifulSoup
from _MyPath import URL

# 결과를 가져올 페이지
book_url = URL
method_url = URL+'method'

# 책 페이지에서 책의 권 수 가져오기 --- (1)
html = requests.get(book_url).text
soup = BeautifulSoup(html, 'html5lib') #--- (1a)
cnt = soup.select_one('#cnt') #--- (1b)

# 메서드 페이지에서 결과 가져오기 --- (2)
html = requests.get(method_url).text
soup = BeautifulSoup(html, 'html5lib') #--- (2a)
gResult = soup.select_one('#gResult') #--- (2b)

# 결과 출력하기 --- (3)
print("책 권수:",cnt.string)
print("GET 결과:",gResult.string)
