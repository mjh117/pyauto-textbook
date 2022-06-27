import os, time, requests, urllib
from bs4 import BeautifulSoup
from _MyPath import URL

# URL 및 저장 경로 지정 --- (1)
url = URL+'book'
save_file = './output/download_booklist2.csv'

# 메인 처리 --- (2)
def csv_download():
    # 뷰티플 수프 객체 만들기 --- (2a)
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html5lib')
    # 링크 가져오기 --- (2b)
    csv_url = get_link(soup, 'CSV')
    # CSV 다운로드 --- (2c)
    if csv_url:
        try_download(csv_url)
    
# HTML에서 URL 얻기 --- (3)
def get_link(soup, text):
    relurl = ''
    # URL 가져오기 --- (3a)
    for a in soup.find_all('a', href=True):
        if text in a.text: #--- (3b)
            relurl = a['href']
    # URL 가공하기 #--- (3c)
    absurl = get_abs(relurl, url, text)
    return absurl

# 절대 URL 가져오기
def get_abs(relurl, url, text) :
    if relurl:
        absurl = urllib.parse.urljoin(url,relurl)
        print('[%s URL] : '%text, absurl)
        return absurl
    else:
        print('[%s URL]이 없습니다.'%text)
        return None

# CSV 다운로드 --- (4)
def try_download(csv_url):
    res = requests.get(csv_url)
    res.encoding = res.apparent_encoding
    # 파일 다운로드 --- (4a)
    with open(save_file, 'wt', newline='') as fp:
        fp.write(res.text)
        print(res.text)
    print('CSV 다운로드 완료::%s'%save_file)
    
if __name__ == '__main__':
    csv_download()
