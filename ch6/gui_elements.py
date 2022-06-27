import PySimpleGUI as sg
from datetime import datetime

# 화면 레이아웃 구성 --- (1)
layout = [
    [sg.Frame('입력', size= (200, 280), layout=[
            [sg.Text('0'),sg.InputText('초기 텍스트', size=(20,1))],
            [sg.Text('1'),sg.Checkbox('체크박스', True)],
            [sg.Text('2'),sg.Radio('라디오', group_id='gid')],
            [sg.Text('3'),sg.Spin([i for i in range(1, 100)], 5, size=(20, 1))],
            [sg.Text('4'),sg.Listbox(['Listbox'+str(i) for i in range(1,10)],'Listbox1', size=(20,3))],
            [sg.Text('5'),sg.Slider((1,100), 5, orientation='h')],
            [sg.Text('6'),sg.Combo(('Combobox 1', 'Combobox 2'), 'Combox1', size=(20, 1))]
        ]),
     sg.Frame('결과', size= (200, 280), layout=[
            [sg.Text('0. InputText:'), sg.Text('-----', key='re0')],
            [sg.Text('1. Checkbox:'), sg.Text('-----', key='re1')],
            [sg.Text('2. Radio:'), sg.Text('-----', key='re2')],
            [sg.Text('3. Spin:'), sg.Text('-----', key='re3')],
            [sg.Text('4. Listbox:'), sg.Text('-----', key='re4')],
            [sg.Text('5. Slider:'), sg.Text('-----', key='re5')],
            [sg.Text('6. Combobox:'), sg.Text('-----', key='re6')],
        ]),
     ], 
    [sg.Button('값 표시')],
]
# 윈도우 생성
window = sg.Window('다양한 입력 요소', layout)

# 이벤트 루프 작성 --- (2)
while True:
    event, values = window.read()
    if event in ('Exit', 'Quit', None): break
    # 버튼 클릭 시 결과 출력 --- (3)
    if event == '값 표시':
        print(event, values) #--- (3a)
        for i in range(7): 
            window['re'+str(i)].update(values[i]) #--- (3b)
            
# 윈도우 닫기
window.close()
