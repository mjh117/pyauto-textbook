import requests

# 액세스 토큰 설정★ --- (1)
acc_token = '발급받은 토큰을 여기 넣습니다'

def send_sticker_line(msg, package_id, sticker_id):
    # 서버에 보낼 파라미터를 준비 --- (2)
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + acc_token}
    payload = {
        'message': msg,
        'stickerPackageId': package_id,
        'stickerId': sticker_id,
        }
    # 서버에 송신 --- (3)
    requests.post(url, headers=headers, params=payload)

if __name__ == '__main__':
    send_sticker_line('Python에서 스티커와 메시지를 보냅니다.', 4, 303)
    print('ok')
