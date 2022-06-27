import os

# 프로그램의 절대 경로 얻기
script_file = os.path.abspath(__file__)
print('script=', script_file)

# 프로그램이 있는 폴더 경로 얻기
script_dir = os.path.dirname(script_file)
print('script_dir=', script_dir)

# 프로그램과 같은 폴더에 있는 'result.txt' 경로 얻기
result_file = os.path.join(script_dir, 'result.txt')
print('result.txt=', result_file)
