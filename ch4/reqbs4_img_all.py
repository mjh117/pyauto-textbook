import os, time, requests, urllib
from bs4 import BeautifulSoup
from _MyPath import URL

# 저장 폴더 지정
save_dir = './output/reqbs4_img_all'
# 이미지를 가져올 웹 사이트
target_url = URL

# 메인 처리 --- (1)
def download_images():
    # 페이지의 HTML 읽기 --- (1a) 
    html = requests.get(target_url).text
    # HTML을 분석하여 이미지 URL 추출 --- (1b)
    urls = get_url(html)
    # URL의 이미지 다운로드 --- (1c)
    request_url(urls)

# 이미지 URL 추출 --- (2)
def get_url(html):
    # Beautiful Soup로 HTML 분석 --- (2a)
    soup = BeautifulSoup(html, 'html5lib')
    res = []
    # img 요소에서 URL 가져오기 --- (3)
    for img in soup.select('#gallery-section img'): 
        # 상대 경로 --- (3a)
        src = img['src'] 
        # URL을 절대 경로로 변환 --- (3b)
        url = urllib.parse.urljoin(target_url, src)
        print('img.src=', url)
        res.append(url) # --- (3c)
    return res

# 연속으로 이미지 다운로드 --- (4)
def request_url(urls):
    # 저장 폴더가 없으면 생성 --- (4a)
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    for url in urls:
        # 파일명 지정 --- (4b)
        fname = os.path.basename(url)
        save_file = save_dir + '/' + fname
        # 이미지 다운로드 --- (4c)
        r = requests.get(url)
        # 파일로 저장 --- (4d)
        with open(save_file, 'wb') as fp:
            fp.write(r.content)
            print("save:", save_file)
        time.sleep(1) # 대기 --- (4e)

if __name__ == '__main__':
    download_images()
