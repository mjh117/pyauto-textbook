import re

# 사전 파일 경로
dict_file = 'input/ejdict-hand-utf8.txt'

# 반복하여 실행 --- (1)
while True:
    # 정규식 입력 받기 --- (2)
    print('정규식을 입력해주세요. (q 입력시 종료)')
    re_str = input()
    if re_str == '': continue
    if re_str == 'q': break
    # 영어 사전에서 정규 표현에 대응하는 단어 검색 --- (3)
    with open(dict_file, 'rt', encoding='utf-8') as f:  #--- (3a)
        cnt = 0
        while True: #--- (3b)
            # 한 행 읽기
            line = f.readline()
            if not line: break #--- (3c) 
            # 영단어 얻기
            word, mean = line.split('\t')
            # 정규식 매치 --- (4)
            if re.search(re_str, word):                
                print(word) # 매치하면 출력
                cnt += 1
                if cnt > 50: break # 최대 50건
