import requests
import os, time
from _MyPath import URL

# 저장 폴더 지정 --- (1)
save_dir = './output/requests_img_all'

# 이미지 기본 URL 지정 --- (2)
base_url = URL+'static/img/book{0}.png'

# 이미지 연속 다운로드 --- (3)
def download_all():
    # 저장 폴더 생성 --- (3a)
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    # 연속 다운로드 --- (3b)
    for id in range(1, 9):
        download_file(id)
        time.sleep(1) # 대기 --- (3c)

# 이미지 한 장 다운로드 --- (4)
def download_file(id):
    # 이미지 URL과 저장 위치를 동적으로 결정 --- (4a)
    url = base_url.format(id)
    save_file = save_dir + '/book' + str(id) + '.png'
    # URL 리소스 얻기 --- (4b)
    res = requests.get(url)
    # 요청 성공 여부 체크--- (4c)
    if not res.ok:
        print("실패:", res.status_code)
        return
    # 데이터를 파일로 저장 --- (4d)
    with open(save_file, 'wb') as fp:
        fp.write(res.content)
    print("save:", save_file)

if __name__ == '__main__':
    download_all()

