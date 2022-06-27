import smtplib, ssl
from email.mime.text import MIMEText
import my_gmail_account as gmail # 계정 정보--- (1)

# 메인 처리 --- (2)
def send_test_email():
    # 메일 데이터(MIME) 작성 --- (2a)
    msg = make_mime_text(
        mail_to=gmail.account,
        subject='메일 송신 테스트',
        body='안녕하세요. 테스트 메일입니다.')
    # 메일 보내기 --- (2b)
    send_gmail(msg)

# 메일 데이터(MIME) 생성 --- (3)
def make_mime_text(mail_to, subject, body):
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject     # 메일 제목
    msg['To'] = mail_to          # 받는 사람
    msg['From'] = gmail.account  # 보내는 사람
    return msg

# Gmail 보내기 --- (4)
def send_gmail(msg):
    # Gmail 서버에 접속
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls() # --- (4a)
    server.ehlo()
    # 로그 출력 --- (5)
    server.set_debuglevel(0) 
    # 로그인하여 메일 발송 --- (6)
    server.login(gmail.account, gmail.password)
    server.send_message(msg)

if __name__ == '__main__':
    send_test_email()
    print('ok.')
