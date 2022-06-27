import requests

# 액세스 토큰 설정★ --- (1)
acc_token = '발급받은 토큰을 여기 넣습니다'
# 이미지 파일 경로를 지정
image_file = 'input/sky.jpg'

def send_line(msg, image_file):
    # 서버에 보낼 파라미터를 준비 --- (2)
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + acc_token}
    payload = {'message': msg}
    # 이미지 읽어오기 --- (3)
    with open(image_file, 'rb') as fp:
        files = {'imageFile': fp}
        # 서버에 송신 --- (4)
        requests.post(url, headers=headers, 
            params=payload, files=files)

if __name__ == '__main__':
    send_line('Python에서 메시지와 사진을 보냅니다.', image_file)
    print('ok')
