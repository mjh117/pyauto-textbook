import webbrowser, time, platform, subprocess
import pyautogui as pa

try:
    # Windows 그림판 열기  --- (1)
    if platform.system() == 'Windows':
        subprocess.Popen(r'C:\Windows\System32\mspaint.exe')
        time.sleep(2) # 2초간 대기
        pa.hotkey('Alt', 'Space', 'X',interval=0.25)

    # macOS 구글 킵 열기 --- (2)
    if platform.system() == 'Darwin': 
        path = 'open -a /Applications/Google\ Chrome.app %s'
        webbrowser.get(path).open('https://keep.google.com/') #--- (2a)
        time.sleep(3)
        pa.hotkey('command','ctrl','f',interval=0.25)
        btn=pa.locateCenterOnScreen('input/brush.png') # --- (2b)
        print(btn)
        time.sleep(1)
        pa.click(btn.x/2,btn.y/2) #레티나가 아니면 pa.click(btn) --- (2c)
        time.sleep(1)
except:
    #대화상자 띄우기  --- (3)
    pa.alert('페인트 툴이 실행되지 않았다면\n페인트 툴을 직접 실행해주세요.')
    time.sleep(10) 
finally:   
    # 그림을 시작할 좌표와 사각형 폭 지정 --- (4)
    bx = 300
    by = 300
    val = 300

    # 마우스 조작 --- (5)
    pa.moveTo(bx, by) # 지정한 위치로 마우스 이동
    pa.dragTo(bx+val, by+val, 2, button='left') # 2초 동안 그리기
    pa.drag(-val,0, 2, button='left') # 상대 좌표를 지정하여 그리기
    pa.drag(0,-val, 2, button='left') # 상대 좌표를 지정하여 그리기

    # 반복하여 마우스 조작 --- (6)
    sec = 0.1
    for i in range(5):
        d = i * 10 + 10
        pa.moveTo(bx+d, bx+d)
        pa.drag(0, val+d, sec, button='left')
        pa.drag(val+d, 0, sec, button='left')
        pa.drag(0, -val-d, sec, button='left')
        pa.drag(-val-d, 0, sec, button='left')
