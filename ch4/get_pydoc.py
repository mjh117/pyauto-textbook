import requests, urllib, os, time, re, shutil
from bs4 import BeautifulSoup

# 저장 위치 --- (1)
save_dir = './output/pydoc'
# 기준 URL --- (2)
pydoc_url = 'https://docs.python.org/ko/3/tutorial/'
# 다운로드한 페이지를 저장할 딕셔너리 --- (3)
visited = {}

# 페이지 다운로드 --- (4)
def download_pydoc(input_url):
    # 다운로드할 대상인지 조사 --- (5)
    down_url = prepro_URL(input_url)
    if not down_url : return
    print('=====',down_url,'탐색 =====')
    # 페이지 텍스트 가져오기 --- (6)
    res = requests.get(down_url)
    res.encoding = res.apparent_encoding #--- (6a)
    html = res.text
    # HTML 파일 다운로드 --- (7)
    save_file(down_url, html)
    # Beautiful Soup 객체 생성 --- (8)
    soup = BeautifulSoup(html, 'html5lib')
    #HTML 찾기  --- (9)
    for a in soup.find_all('a', href =True): 
        href = a['href'].strip() #--- (9a)
        a_url = urllib.parse.urljoin(down_url, href) #--- (9b)
        download_pydoc(a_url) #--- (9c)

# URL 검사 및 폴더 생성  --- (10)
def prepro_URL(before_url): 
    # URL 전처리 --- (11)
    pResult = urllib.parse.urlparse(before_url) # --- (11a)
    path = pResult.path # --- (11b)
    if os.path.basename(path) =='' : # --- (11c)
        path+='index.html' 
    after_url = urllib.parse.urljoin(before_url, path) # --- (11d)
    # URL 검사 --- (12)
    checkResult = check_URL(after_url) # --- (12a)
    if not checkResult : return False # --- (12b)
    # 폴더 만들기 --- (13)
    dirname = save_dir+ os.path.dirname(path) # --- (13a)
    if not os.path.exists(dirname): # --- (13b)
        print('[폴더 생성]', dirname)
        os.makedirs(dirname)
    return after_url # --- (14)

# 다운로드할 URL인지 확인  --- (15)
def check_URL(url):
    # 형식 검사 --- (15a)
    if pydoc_url not in url: return False
    # 중복 검사 --- (15b)
    if url in visited: return False
    # 방문 처리 --- (15c)
    visited[url] = True
    return True

# 파일 다운로드 --- (16)
def save_file(url, text):
    # 파일 경로 결정 --- (16a)
    fname = save_dir + urllib.parse.urlparse(url).path
    #파일 저장 --- (16b)
    with open(fname, "wt", encoding="utf-8") as f:
        f.write(text)
    print('[파일 저장] ::' ,fname)
    time.sleep(1) # 대기

if __name__ == '__main__':
    download_pydoc(pydoc_url) # 최초 페이지 탐색 --- (17)
