import requests
from _MyPath import URL

# 서버에 요청 보내기
url = URL+'today'
response = requests.get(url)

# response의 타입 출력 --- (1)
print("type=", type(response))

# 요청 성공 여부 출력 --- (2)
print("ok=", response.ok)

# 요청에 성공했다면 텍스트 출력--- (3)
if response.ok:
    print("text=", response.text)

# 상태 코드 출력 --- (4)
print("status_code=", response.status_code)
