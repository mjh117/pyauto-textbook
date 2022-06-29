import requests, urllib, os, time, re
from bs4 import BeautifulSoup

# 저장 위치
save_dir = './output/pydoc'
# 기준 URL
pydoc_url = 'https://docs.python.org/ko/3/tutorial/'
static_url = 'https://docs.python.org/ko/3/_static/'
# 다운로드한 페이지를 저장할 딕셔너리
visited = {}

# 페이지 다운로드
def download_pydoc(input_url):
    # 다운로드할 대상인지 조사 --- (1)
    down_url = prepro_URL(input_url)
    if not down_url : return
    print('=====',down_url,'탐색 =====')
    # 페이지 텍스트 가져오기 --- (2)
    res = requests.get(down_url)
    res.encoding = res.apparent_encoding
    html = res.text
    # HTML 파일 다운로드 --- (3)
    save_file(down_url, html)
    # Beautiful Soup 객체 생성 --- (4)
    soup = BeautifulSoup(html, 'html5lib')
    # CSS 찾기 --- (5)
    for link in soup.find_all('link', rel="stylesheet", href =True): #--- (5a)
        css_url = abs_URL(down_url, link['href']) #--- (5b)
        download_static(css_url) #--- (5c)
    # HTML 찾기 
    for a in soup.find_all('a', href =True): 
        a_url = abs_URL(down_url, a['href'])
        download_pydoc(a_url)

# CSS 다운로드  --- (6)
def download_static(input_url):
    # 다운로드할 대상인지 조사 --- (6a)
    down_url = prepro_URL(input_url)
    if not down_url : return
    # CSS 텍스트 가져오기 --- (6b)
    text = requests.get(down_url).text
    # CSS 파일 다운로드 --- (6c)
    save_file(down_url, text)
    # import된 CSS 찾기 --- (7)
    import_urls = re.findall('@import url\(\"([^"]+)\"\)',text) # --- (7a)
    for url in import_urls: 
        css_url =  abs_URL(down_url, url) # --- (7b)
        download_static(css_url) # --- (7c)

# 절대 URL 얻기
def abs_URL(cur, rel):
    tmp = rel.strip()
    url = urllib.parse.urljoin(cur,tmp)
    return url

# URL 검사 및 폴더 생성
def prepro_URL(before_url):
    # URL 전처리
    path = urllib.parse.urlparse(before_url).path
    if os.path.basename(path) =='' :
        path+='index.html'
    after_url = urllib.parse.urljoin(before_url, path)
    checkResult = check_URL(after_url)
    if not checkResult : return False    
    # 폴더 만들기
    dirname = save_dir+ os.path.dirname(path)
    if not os.path.exists(dirname):
        print('[폴더 생성]', dirname)
        os.makedirs(dirname)
    return after_url

# 다운로드할 URL인지 확인 --- (8)
def check_URL(url):
    # 형식 검사 --- (8a)
    if not re.match(pydoc_url+'.+\.html',url):
        if not re.match(static_url+'.+\.css', url):
            return False
    # 중복 검사
    if url in visited: return False
    # 방문 처리 
    visited[url] = True
    return True

# 파일 다운로드
def save_file(url, text):
    # 파일 이름 결정 
    fname = save_dir + urllib.parse.urlparse(url).path
    with open(fname, "wt", encoding="utf-8") as f:
        f.write(text)
    print('[파일 저장] ::' ,fname)
    time.sleep(1) # 대기

if __name__ == '__main__':
    download_pydoc(pydoc_url) # 최초 페이지 탐색
