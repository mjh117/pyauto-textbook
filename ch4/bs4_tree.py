# import문으로 라이브러리 불러오기
from bs4 import BeautifulSoup 

# HTML 파일 읽기 --- (1)
hfile = 'input/scraping.html'
with open(hfile, encoding='utf-8') as fp:
  html_str = fp.read()
  
# Beautiful Soup 객체 --- (2)
soup = BeautifulSoup(html_str, 'html5lib')

# head의 조상 확인하기 --- (3)
head = soup.head
print('head의 부모:',head.parent.name) #--- (3a)
print('head의 부모의 부모:',head.parent.parent.name) #--- (3b)

#head의 자식 확인하기 --- (4)
print('head의 자식')
for e in head.contents:
    print('[{0}]{1}'.format(type(e),e.name))

