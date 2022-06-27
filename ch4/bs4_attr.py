from bs4 import BeautifulSoup
hfile = 'server/templates/book_static.html'

# HTML 파일 읽고 BeautifulSoup 객체 생성 --- (1)
with open(hfile, encoding='utf-8') as fp:
  html_str = fp.read()
soup = BeautifulSoup(html_str, 'html5lib')

# id가 b1인 .item 요소 찾기 --- (2)
print(soup.find(id='b1', class_='item')) #--- (2a)
print(soup.find(name='div', attrs={'id':'b1', 'class':'item'})) #--- (2b)
print(soup.find_all('div', class_='item', limit=1)) #--- (2c)
print(soup.select_one('div#b1.item')) #--- (2d)
print('----------')

# 책 제목으로 .title 요소 찾기 --- (3)
print(soup.find(string='도커, 컨테이너 빌드업!')) #--- (3a)
print(soup.find('div', string='도커, 컨테이너 빌드업!')) #--- (3b)
print('----------')

# 책 제목이 나뉘어졌을 때 .title 요소 찾기 --- (4)
ele = soup.find(string='파이썬 머신러닝') 
print(ele) #--- (4a)
print(ele.parent) #--- (4b)
print(ele.parent.parent) #--- (4c)
