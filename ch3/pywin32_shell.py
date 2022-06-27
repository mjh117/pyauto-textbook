import sys, win32com.client as com

shell = com.Dispatch('WScript.shell')
value = shell.SpecialFolders(4)
print(value)
