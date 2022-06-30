from bs4 import BeautifulSoup
hfile = 'server/templates/book_static.html'

# HTML 파일 읽고 BeautifulSoup 객체 생성
with open(hfile, encoding='utf-8') as fp:
  html_str = fp.read()
soup = BeautifulSoup(html_str, 'html5lib')

# 메서드로 검색하기 --- (1)
item = soup.find('div', id='b1')
p = item.find(class_='price')
print(p.string)

# CSS 선택자로 검색하기 --- (2)
p = soup.select_one('#b1 .price')
print(p.string)
