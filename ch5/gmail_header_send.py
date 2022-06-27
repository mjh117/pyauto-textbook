import smtplib, ssl
from email.mime.text import MIMEText
import send_gmail # Gmail 발송 모듈
import my_gmail_account as gmail # Gmail 계정 정보


# 메일 데이터 작성 --- (1)
msg = MIMEText('안녕하세요. CC 및 Reply-To 테스트입니다')
msg['Subject'] = 'CC 테스트'
msg['To'] = gmail.account
msg['From'] = gmail.account
msg['Cc'] = gmail.account
# msg['Bcc'] = ''
msg.add_header('reply-to', 'test@example.com') # --- (1a)

# 메일 송신 --- (2)
send_gmail.send_gmail(msg)
print("ok")
