import smtplib, ssl
from email.mime.text import MIMEText
import my_gmail_account as gmail # Gmail 계정 정보
import send_gmail # Gmail 발송 모듈

# HTML 데이터 --- (1)
html = '''
    <html><meta charset="utf-8"><body>
    <h1>HTML 메일을 보냅니다</h1>
    <p>업무에 도움이 되는 스티브 잡스 어록</p>
    <ul>
      <li>가장 중요한 결정이란 무엇을 할것인가가 아니라
      무엇을 하지 않을 것인가를 결정하는 것이다</li>
      <li>삶에서 만족을 느끼기 위해선 당신이 위대하다고 생각하는 일을 해야 한다.
      위대한 일을 할 방법은 당신이 하는 그 일을 사랑하는 것이다.</li>
      <li>내가 반복해서 외우는 주문 중 하나는 집중과 단순함이다.
      단순함은 복잡함보다 더 어렵다.</li>
    </ul>
    </body></html>
'''
# HTML 데이터를 MIME 형식으로 작성 --- (2)
msg = send_gmail.make_mime_text(
    mail_to=gmail.account,
    subject='HTML 메일 테스트',
    body=html)

# 메일 송신 --- (3)
send_gmail.send_gmail(msg)
print("ok")
