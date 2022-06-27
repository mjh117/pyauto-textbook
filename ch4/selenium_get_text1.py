from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from _MyPath import URL, DRIVER as d

# 책 소개 사이트 열기 --- (1)
driver = webdriver.Chrome(d)
driver.get(URL)

# h1 요소의 텍스트 출력하기 --- (2)
ele = driver.find_element_by_tag_name('h1')
print('h1:', ele.text)

# id가 cnt인 요소의 텍스트 출력하기 --- (3)
ele = driver.find_element_by_id('cnt')
print('#cnt:', ele.text)

time.sleep(3)
driver.quit()
