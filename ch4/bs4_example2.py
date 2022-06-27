# import문으로 라이브러리 불러오기
from bs4 import BeautifulSoup 

# HTML 파일 읽기 --- (1)
hfile = 'input/scraping.html'
with open(hfile, encoding='utf-8') as fp:
  html_str = fp.read()
  
# Beautiful Soup 객체 --- (2)
soup = BeautifulSoup(html_str, 'html5lib')

# div의 요소 및 텍스트 취득 --- (3)
e = soup.div
result =[
    e.name,
    e.h1['id'],
    e.h1.attrs,
    e.h1.string,
    list(e.strings)[0:2],
    e.text
    ]
for r in result :
    print(r)
    print('----------------------')

