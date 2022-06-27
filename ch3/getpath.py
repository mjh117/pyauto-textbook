import os

# 작업 디렉터리 기준으로 파일의 절대 경로 얻기 --- (1)
path1 = os.path.abspath('./input/name1.xlsx')
print(path1)

# 실행중인 프로그램 경로 기준으로 파일의 절대 경로 얻기 --- (2)
base_dir = os.path.dirname(__file__)
path2 = os.path.join(base_dir, 'input','name1.xlsx')
path2 = os.path.abspath(path2)
print(path2)
