import smtplib
from email.mime.text import MIMEText
import my_outlook_account as outlook # 계정 정보

# 메인 처리 --- (1)
def send_test_email():
    # 메일 데이터(MIME) 작성
    msg = make_mime_text(
        mail_to=outlook.account,
        subject='메일 송신 테스트',
        body='안녕하세요. 테스트 메일입니다')
    # 메일 보내기
    send_outlook_mail(msg)

# 메일 데이터(MIME) 생성 --- (2)
def make_mime_text(mail_to, subject, body):
    msg = MIMEText(body, 'plain')
    msg['Subject'] = subject      # 메일 제목
    msg['To'] = mail_to           # 받는 사람
    msg['From'] = outlook.account # 보내는 사람
    return msg

# Outlook 메일 보내기 --- (3)
def send_outlook_mail(msg):
    # Outlook 서버에 접속 --- (3a)
    server = smtplib.SMTP(
        'smtp.office365.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    # 로그인하고 메일 발송
    server.login(
        outlook.account,
        outlook.password)
    server.send_message(msg)

if __name__ == '__main__':
    send_test_email()
    print('ok.')

