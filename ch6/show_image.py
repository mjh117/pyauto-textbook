import PySimpleGUI as sg
import sys, os  

# 리소스 폴더에 접근하는 함수 --- (1)
def get_resource(filename):
    if hasattr(sys, "_MEIPASS"): #--- (1a)
        return os.path.join(sys._MEIPASS, filename)
    return filename #--- (1b)

# 화면 레이아웃을 윈도우에 지정 --- (2)
layout = [
    [sg.Text('이미지를 화면에 표시하기')],
    [sg.Image(get_resource('res/data.png'))]
]
win = sg.Window('리소스 사용 예제', layout)

# 이벤트 루프 --- (3)
while True:
    # 이벤트에 대한 파라미터 취득
    event, val = win.read()
    # 윈도우 종료 버튼을 눌렀을 때
    if event in ('Exit', 'Quit', None): break
win.close()

