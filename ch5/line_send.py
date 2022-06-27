import requests

# 액세스 토큰 설정★ --- (1)
acc_token = '발급받은 토큰을 여기 넣습니다'

def send_line(msg):
    # 서버에 보낼 파라미터 작성--- (2)
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + acc_token}
    payload = {'message': msg}
    requests.post(url, headers=headers, params=payload) #--- (2a)

if __name__ == '__main__':
    # 메시지 보내기 --- (3)
    send_line('Python에서 메시지를 보냅니다.')
    print('ok')
