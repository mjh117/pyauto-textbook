from bs4 import BeautifulSoup
import os

hfile = '../../templates/book_static.html'

def gen_booklist_reset():
    # HTML 파일 읽고 BeautifulSoup 객체 생성 --- (*1)
    with open(hfile, encoding='utf-8') as fp:
      html_str = fp.read()
    soup = BeautifulSoup(html_str, 'html5lib')

    # CSS 선택자로 책 목록 얻기 --- (*2)
    booklist = []
    # 갤러리에서 item 얻기
    item_list = soup.select('#gallery-section > .item')
    for item in item_list:  
        # item 아래에서 제목, 가격 얻기 --- (*4)
        idnum = item['id']
        title = get_title(item.select('.title')[0])
        date = item.select('.date')[0].text
        price = item.select('.price')[0].text
        # article 아래에서 이미지 정보 얻기 --- (*3)
        img = os.path.basename(item.img['src'])
        # 결과 출력하고 리스트에 담기 --- (*5)
        bookstr = idnum, title, date, price, img
        print(bookstr)
        booklist.append(bookstr)

    # 결과를 CSV로 저장 --- (*6)
    import csv
    with open('booklist_reset_gen.csv', 'wt', encoding='utf-8', newline='') as fp:
        csv.writer(fp).writerows(booklist)

# 책 제목 구하기
def get_title(title):
    titlestr=""
    if(len(title.contents)==1):
        titlestr = title.string
    else:
        for child in title.contents:
            tmp=child.string.strip() 
            if tmp:
                titlestr+=tmp + "\\"
        titlestr = titlestr[:-1]
    return titlestr

if __name__ == '__main__':
    gen_booklist_reset()
