import requests
from _MyPath import URL

# 이미지 파일 URL
url = URL+'static/img/book1.png'

# URL 리소스 취득 --- (1)
res = requests.get(url)

# 성공 여부 체크 --- (2)
if not res.ok:
    print("실패 :", res.status_code)
    quit()

# 파일 저장 --- (3)
with open('output/book-image.jpg', 'wb') as fp:
    fp.write(res.content)
print("성공 :", res.status_code)
