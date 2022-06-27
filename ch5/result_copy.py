import pyperclip

# 클립보드에 복사
pyperclip.copy('클립 보드에 복사할 텍스트')

# 클립보드에서 내용 취득
text = pyperclip.paste()
print(text)
