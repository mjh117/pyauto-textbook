from bs4 import BeautifulSoup
hfile = 'server/templates/book_static.html'

# HTML 파일 읽기 --- (1)
with open(hfile, encoding='utf-8') as fp:
  html_str = fp.read()

# Beautiful Soup 객체 생성 --- (2)
soup = BeautifulSoup(html_str, 'html5lib')

#첫 번째 title 요소 출력 --- (3)
print(soup.title)
print(soup.find('title'))
print(soup.select_one('title'))

# 모든 title 요소 출력 --- (4)
print(soup.find_all('title'))
print(soup.select('title'))

