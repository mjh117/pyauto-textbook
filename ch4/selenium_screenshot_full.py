from selenium import webdriver
from _MyPath import DRIVER as d

# 캡처할 페이지 URL
url = 'https://python.org'
# 저장 위치
save_file = 'output/screenshot_full.png'

# 메인 처리 --- (1)
def screenshot_full(url, save_file):
    # 페이지 사이즈 얻기
    w, h = get_page_size(url)
    # 지정 사이즈로 크롬을 기동해서 화면 캡처
    screenshot_size(url, save_file, w, h)

# 페이지 폭과 높이 얻기 --- (2)
def get_page_size(url):
    # 브라우저를 기동해 URL 페이지 접속
    driver = webdriver.Chrome(d)
    driver.get(url)
    # 페이지 폭과 높이 얻기 (JavaScript 실행) --- (2a)
    w = driver.execute_script(
        "return document.body.scrollWidth;")
    h =  driver.execute_script(
        "return document.body.scrollHeight;")
    driver.quit() # 사이즈를 얻고 드라이버 닫기
    print('page_size=', w, h)
    return (w, h)

# 지정 사이즈로 페이지 저장 --- (3)
def screenshot_size(url, save_file, w, h):
    # 옵션 지정 
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    # 화면 사이즈 지정 --- (3a)
    win_size = 'window-size='+str(w)+','+str(h)
    options.add_argument(win_size)
    # 크롬을 기동해서 페이지를 열고 캡처 --- (3b)
    driver = webdriver.Chrome(d, options=options)
    driver.get(url)
    result = driver.save_screenshot(save_file)
    if result : print('캡처 성공')
    driver.quit()

if __name__ == '__main__':
    screenshot_full(url, save_file)
