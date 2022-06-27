# import문으로 라이브러리 불러오기 --- (1)
from bs4 import BeautifulSoup 

# HTML 파일 읽기 --- (2)
hfile = 'input/scraping.html'
with open(hfile, encoding='utf-8') as fp:
  html_str = fp.read()
  
# Beautiful Soup 객체 --- (3)
soup = BeautifulSoup(html_str, 'html5lib')
print(soup.prettify()+'\n') #--- (3a)

# title 요소 확인하기 --- (4)
title = soup.title
print(title)
print(title.string+'\n')

# bs4 객체 타입 --- (5)
print(type(soup))
print(type(title))
print(type(title.string))
