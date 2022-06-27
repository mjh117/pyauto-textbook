# Selenium 불러오기 --- (1)
from selenium import webdriver
import time
from _MyPath import DRIVER as d

# 크롬 열기 --- (2)
driver = webdriver.Chrome(d)

# 파이썬 페이지 열기 --- (3)
driver.get('https://python.org')

# 3초 후에 크롬 닫기 --- (4)
time.sleep(3)
driver.quit()
