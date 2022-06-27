import time, subprocess, platform
import pyautogui as pa

# 조작할 앱의 화면 이미지(↓자신이 캡처한 이미지를 지정) --- (1)
calc_png = 'input/calc.png'
calc_root = 'input/calc_root.png'

# Windows 경로 지정하고 실행 --- (2)
if platform.system() == 'Windows':
    app = [r'c:\Windows\System32\calc.exe']
    subprocess.Popen(app)
# macOS 경로 지정하고 실행 --- (3)
elif platform.system() == 'Darwin':
    app = ['open',
        '/System/Applications/Calculator.app']
    time.sleep(3)
    subprocess.Popen(app)
    time.sleep(3)
    pa.hotkey('command', '2', interval=0.25)

# 계산기가 실행될 때까지 대기 --- (4)
pos = None
for i in range(10):
    pos = pa.locateOnScreen(calc_png,
        grayscale=True, confidence=0.8)
    if pos is None: # --- (4a)
        time.sleep(1)
        print('찾고 있습니다')
        continue
    break
if pos is None:
    pa.alert('찾지 못했습니다')
    quit()
print('찾았습니다! 계산기:', pos) # --- (4b)

# 키를 입력하여 계산 수행하기 --- (5)
pa.write('3*3=', interval=0.3)
r_btn=pa.locateCenterOnScreen(calc_root,
          grayscale=True, confidence=0.8) #--- (5a)
print('버튼:',r_btn)
time.sleep(3)
if platform.system() == 'Windows':
    pa.click(r_btn) #--- (5b)
else:
    pa.click(r_btn.x/2, r_btn.y/2) #--- (5c) 레티나가 아니라면 pa.click(r_btn)

print('키 입력 완료') 
