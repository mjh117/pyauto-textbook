#import urllib.request as urlreq
import requests, os
from bs4 import BeautifulSoup

# 바탕화면에 저장할 결과 파일
save_file = os.path.expanduser('~/Desktop/날씨.txt')

# XML 데이터 가져오기
url ="https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
text = requests.get(url).text
soup = BeautifulSoup(text, 'html.parser')

# 각 지역 날씨 가져오기
title = soup.item.title.string
forecast = {}
for loc in soup.find_all("location"):
    prov = loc.find("province").string
    if prov not in forecast:
        forecast[prov] = []
    city = loc.find("city").string
    wf = loc.find("wf").string
    forecast[prov].append(city+":"+wf)

# 파일에 저장하기
with open(save_file, 'wt', encoding='utf-8') as f:
    f.write('=='+title+'==\n')
    for prov, wfinfo in forecast.items() :
        f.write('\n-----'+prov+'-----\n')
        for string in wfinfo:
            f.write(string+'\n')
    f.close()
