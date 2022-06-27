import time, subprocess, platform
import pyautogui as pa
import pyperclip

# Windows에서 메모장 열기 --- (1)
if platform.system() == 'Windows':
    subprocess.Popen(r'c:\Windows\notepad.exe')
    time.sleep(2) # 2초간 대기
    pa.write('Hello, Python!') #영문 입력--- (1a)
    pa.press('enter')
    pyperclip.copy("[Windows]에서 실행") #한글 입력--- (1b)
    pa.hotkey('ctrl', 'v')

# macOS에서 텍스트 편집기 열기 --- (2)
if platform.system() == 'Darwin':
    subprocess.Popen(['open',
        '/System/Applications/TextEdit.app'])
    time.sleep(2) # 2초간 대기
    pa.write('Hello, Python!\n') #영문 입력--- (2a)
    pa.press('enter')
    pyperclip.copy("[macOS]에서 실행") #한글 입력--- (2b)
    pa.hotkey('command', 'v')
