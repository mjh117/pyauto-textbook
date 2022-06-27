import requests
from _MyPath import URL

# URL, User-Agent 값 --- (1)
url = URL+'reqinfo'
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'

# 데이터, 쿠키, 헤더 딕셔너리 지정하기 --- (2)
cookie={'mycookie':"it's my cookie"}
header = {'User-Agent':ua,'myheader':"it's my header"}
data1 = {'fir':'queryStr1', 'sec':'queryStr2'}
data2 ={'fir':'bodyData1', 'sec':'bodyData2'}


# GET 요청 보내기 --- (3)
res1 = requests.get(url, params=data1) #--- (3a)
dic1 = res1.json() #--- (3b)

# POST 요청 보내기 --- (4)
res2 = requests.post(url, data=data2, cookies=cookie, headers=header) #--- (4a)
dic2 = res2.json()

# 결과 출력하기 --- (5)
print('---GET Request Info---')    
for i in dic1.items() : print(i)
print('---POST Request Info---')
for i in dic2.items() : print(i)
