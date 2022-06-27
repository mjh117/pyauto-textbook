import tempfile, subprocess, os

# 임시 폴더 생성 
with tempfile.TemporaryDirectory() as tmp:
    # 임시 폴더에 임시 파일 생성
    fname = os.path.join(tmp, 'test.txt')
    with open(fname, 'wt') as fp:
        fp.write('안녕하세요.\r\n임시 파일입니다.')
    # 메모장에서 열기
    subprocess.run(['notepad', fname])

# 이 시점에서 임시 폴더는 삭제된다
print("ok.")
