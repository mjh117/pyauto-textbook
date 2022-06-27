from bs4 import BeautifulSoup
import os

hfile = 'server/templates/book_static.html'

# HTML 파일 읽고 BeautifulSoup 객체 생성 --- (1)
with open(hfile, encoding='utf-8') as fp:
  html_str = fp.read()
soup = BeautifulSoup(html_str, 'html5lib')

# id가 gallery-section인 요소 아래에서 img 얻기 --- (2)
img_list = soup.select('#gallery-section img')
imginfo = []
# img 정보 얻기 --- (3)
for img in img_list:
    # 상대 경로 --- (3a)
    relpath = img['src']    
    # Path를 절대 경로로 변환 --- (3b)
    basedir = os.path.dirname(hfile);
    joinpath =os.path.join(basedir, relpath);
    abspath = os.path.abspath(joinpath);
    # 사이즈 계산하기 --- (3c)
    size = str(os.path.getsize(abspath))
    # 결과 출력 --- (3d)
    imgtp = os.path.basename(abspath),size+"byte"
    print(imgtp)
    imginfo.append(imgtp)

# 결과를 CSV로 저장 --- (4)
import csv
with open('output/imginfo.csv', 'wt', encoding='utf-8', newline='') as fp:
    csv.writer(fp).writerows(imginfo)
