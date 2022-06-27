import smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import send_gmail # Gmail 발송 모듈
import my_gmail_account as gmail # Gmail 계정 정보

# 메일 데이터 작성 --- (1)
msg = MIMEMultipart()
msg['Subject'] = 'ZIP 파일 첨부'
msg['From'] = gmail.account
msg['To'] = gmail.account
    
# 본문 텍스트 작성 --- (2)
txt = MIMEText('ZIP 파일 첨부 테스트입니다.')
msg.attach(txt)

# ZIP 파일 첨부 --- (3)
zip_part = MIMEBase('application', 'zip') # --- (3a)
with open('input/test.zip', 'rb') as fp: # --- (3b)
    zip_part.set_payload(fp.read())
encoders.encode_base64(zip_part) # --- (3c)
zip_part.add_header('Content-Disposition',
'attachment', filename='test.zip') # --- (3d)
msg.attach(zip_part) # --- (3e)

# 메일 발송 --- (4)
send_gmail.send_gmail(msg)
print("ok")
