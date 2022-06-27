# import문으로 라이브러리 불러오기
from bs4 import BeautifulSoup 

# HTML 파일 읽기 --- (1)
hfile = 'input/scraping.html'
with open(hfile, encoding='utf-8') as fp:
  html_str = fp.read()
  
# Beautiful Soup 객체 --- (2)
soup = BeautifulSoup(html_str, 'html5lib')

# head의 조상 확인하기 --- (3)
e = soup.head
result =[
    e.title,
    e.parent,
    e.contents,
    list(e.children),
    e.previous_sibling,
    e.next_siblings,
    e.previous_element,
    e.title.next_element
    ]
for r in result :
    print(r)
    print('----------------------')

