import docx
import datetime

template_file = './input/letter-template.docx'
save_file = './output/letter-kim2.docx'
now = datetime.datetime.now()

# 바꿔 넣을 내용 작성
new_data = {
  '★★★ 요청문': '송금 확인 요청문',
  '[[회사명]]': 'JY전자정밀',
  '[[수신인]]': '김진우',
  '[[제품명]]': 'M-123',
  '[[발행일]]': now.strftime('%Y년%m월%d일')
}

# 서식을 입힐 부분 지정 --- (1)
cstyle = {
  '★★★ 요청문': True
}

# 워드 파일 열기
doc = docx.Document(template_file)

# 내용을 바꿔 쓰기
for p in doc.paragraphs: 
    # 텍스트 교체 --- (2)
    for k,v in new_data.items():
        if p.text.find(k) >= 0:
            p.text = p.text.replace(k, v)
            # 서식 설정 --- (3)
            if k in cstyle:
                font = p.runs[0].font
                font.bold = True
                font.underline = True
                font.size = docx.shared.Pt(20)

# 워드 파일 저장
doc.save(save_file)
