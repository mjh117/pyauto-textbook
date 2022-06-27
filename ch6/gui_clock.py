import PySimpleGUI as sg
from datetime import datetime

# 화면 레이아웃 구성 --- (1)
layout = [
    [sg.Text('디지털 시계')],
    [sg.Text('00:00:00',key='clock',font=('Helvetica', 72))]
]
# 창 생성
window = sg.Window('시계', layout)

# 이벤트 루프 작성 --- (2)
while True:
    # 이벤트에 대한 매개변수 얻기 --- (3)
    event, values = window.read(timeout=100)
    if event in ('Exit', 'Quit', None): break
    # 현재 시각을 갱신 --- (4)
    s = datetime.now().strftime('%H:%M:%S')
    window['clock'].update(s)

# 창 닫기
window.close()
