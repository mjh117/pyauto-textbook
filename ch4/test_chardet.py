import chardet, requests

# 아오조라분코 > 달려라 메로스
url = 'https://www.aozora.gr.jp/cards/000035/files/1567_14913.html'
# 바이너리로 다운로드 --- (1)
bindata = requests.get(url).content
# 문자 인코딩 판정 --- (2)
r = chardet.detect(bindata)
# 결과 출력
print(r)
