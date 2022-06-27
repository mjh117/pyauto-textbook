import docx
import datetime

template_file = './input/letter-template.docx'
save_file = './output/letter-kim.docx'
now = datetime.datetime.now()

# 바꿔 넣을 내용 작성 --- (1)
new_data = {
  '★★★ 요청문': '송금 확인 요청문',
  '[[회사명]]': 'JY전자정밀',
  '[[수신인]]': '김진우',
  '[[제품명]]': 'M-123',
  '[[발행일]]': now.strftime('%Y년%m월%d일')
}

# 워드 파일 열기 --- (2)
doc = docx.Document(template_file)

# 내용 바꿔 쓰기 --- (3)
for p in doc.paragraphs:
    # 텍스트 교체하기 --- (4)
    for k,v in new_data.items():
        if p.text.find(k) >= 0:
            p.text = p.text.replace(k, v)

# 워드 파일 저장 --- (5)
doc.save(save_file)


