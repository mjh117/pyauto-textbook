import smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import send_gmail # Gmail 발송 모듈
import my_gmail_account as gmail # Gmail 계정 정보

# 메일 데이터 작성 --- (1)
msg = MIMEMultipart()
msg['Subject'] = '풍경 사진'
msg['From'] = gmail.account
msg['To'] = gmail.account

# 본문 텍스트 작성 --- (2)
txt = MIMEText('어제 산에 가서 찍은 사진입니다.\n첨부 이미지를 확인해주세요.')
msg.attach(txt)

# 이미지 첨부 --- (3)
with open('input/Mountain.jpg', 'rb') as fp:
    img = MIMEImage(fp.read())
    msg.attach(img)

# 메일 발송 --- (4)
send_gmail.send_gmail(msg)
print("ok")
