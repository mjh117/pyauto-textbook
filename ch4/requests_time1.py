# requests 모듈 불러오기 --- (1)
import requests
from _MyPath import URL

# 현재 시각을 반환하는 서버에 요청 보내기 --- (2)
url = URL+'today'
response = requests.get(url)

# 결과 출력 --- (3)
print(response.text)