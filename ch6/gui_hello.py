import PySimpleGUI as sg

# 화면 레이아웃 구성 --- (1)
layout = [
    [sg.Text('간단한 GUI 앱입니다.')],
    [sg.Text('버튼을 클릭해보세요.')],
    [sg.Button('Hello'), sg.Button('Close')]
]
# 창 생성 --- (2)
window = sg.Window('샘플', layout, size=(200, 100))

# 이벤트 루프 작성 --- (3)
while True:
    # 이벤트에 대한 매개변수 얻기 --- (3a)
    event, values = window.read()
    # 버튼 클릭 이벤트 처리--- (3b)
    if event in ('Exit', 'Quit', None): break # 창 종료 버튼 클릭 
    if event == 'Hello': print('Hello 버튼 클릭')
    if event == 'Close': print('Close 버튼 클릭'); break

# 창 닫기 --- (4)
window.close()
