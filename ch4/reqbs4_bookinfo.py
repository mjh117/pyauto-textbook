import os, requests, csv, urllib
from bs4 import BeautifulSoup
from _MyPath import URL

# 이미지를 가져올 페이지
target_url = URL

# HTML을 읽고 Beautiful Soup로 분석 --- (1)
html = requests.get(target_url).text
soup = BeautifulSoup(html, 'html5lib')

# 메인 처리 --- (2)
def get_bookinfo():
    bookinfo = [] 
    for item in soup.select('.item'): #--- (3)
        # 책 제목 얻기 #--- (3a)
        title = get_title(item.select_one('.title'))
        # 책 가격, 출간일 얻기 #--- (3b)
        price = item.select_one('.price').string
        date = item.select_one('.date').string
        # 책 이미지 사이즈 얻기 #--- (3c)
        imgsize = get_imgsize(item.img['src'])
        # 리스트에 추가 #--- (3d)
        bookstr = title, price, date, imgsize
        bookinfo.append(bookstr)
        print(bookstr)
    #결과를 파일로 저장
    save_file(bookinfo)

# 책 제목 구하기 #--- (4)
def get_title(title):
    titlestr=""
    if(len(title.contents)==1): #--- (4a)
        titlestr = title.string
    else:
        for child in title.contents: #--- (4b) 
            tmp=child.string.strip() 
            if tmp: #--- (4c) 
                titlestr+=tmp + " "
    return titlestr

# 이미지 사이즈 구하기 #--- (5)
def get_imgsize(relurl):
    absurl = urllib.parse.urljoin(target_url, relurl) #--- (5a)
    res = requests.head(absurl) #--- (5b)
    size=res.headers.get('Content-Length') 
    imgsize = os.path.basename(absurl)+"("+size+"byte)" #--- (5c)
    return imgsize

# tsv 파일로 저장하기
def save_file(bookinfo):
    with open('./output/bookinfo.tsv', 'wt', encoding='utf-8', newline='') as fp:
        csv.writer(fp, delimiter='\t').writerows(bookinfo)

if __name__ == '__main__':
    get_bookinfo()
