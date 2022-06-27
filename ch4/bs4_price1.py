from bs4 import BeautifulSoup
hfile = 'server/templates/book_static.html'

# HTML 파일 읽고 BeautifulSoup 객체 생성 --- (1)
with open(hfile, encoding='utf-8') as fp:
  html_str = fp.read()
soup = BeautifulSoup(html_str, 'html5lib')

# 후손 검색으로 가격 찾기 --- (2)
item = soup.find(id='b1', class_='item')
for e in item.descendants:
    if e.name=='div':
        if 'price' in e['class']:
            print(e.string)
