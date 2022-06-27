import PySimpleGUI as sg

# 화면 레이아웃 구성 --- (1)
layout = [
    [sg.Text('인치를 센티미터로 변환하기')],
    [sg.Text('인치'), sg.InputText(key='inch')], #--- (1a)
    [sg.Button('변환')],  
    [sg.Text('---', key='info', size=(40,1))],
]
# 창 생성
window = sg.Window('인치→센티미터 변환', layout)

# 이벤트 루프 작성 --- (2)
while True:
    # 이벤트에 대한 매개변수 얻기 --- (2a)
    event, values = window.read()
    if event in ('Exit', 'Quit', None): break # 창 종료 버튼
    # 변환 버튼 클릭 --- (3)
    if event == '변환':
        inch = float(values['inch']) #--- (3a)
        cm = inch * 2.54
        s = '{0}inch = {1}cm'.format(inch, cm)
        # 텍스트 갱신 --- (3b)
        window['info'].update(s)
        
# 창 닫기
window.close()
