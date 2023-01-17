"""
날짜 : 2023/01/17
이름 : 조주영
내용 : 파이썬 기상청 날씨 크롤링 실습
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pymysql

# 데이터베이스 접속
conn = pymysql.connect(host='127.0.0.1',
                       user='root',
                       password='1234',
                       db='java2db',
                       charset='utf8')

# SQL 실행객체
cur = conn.cursor()

# 가상 브라우저 실행
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome('./chromedriver.exe', options=chrome_options)

# 페이지 이동
browser.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')

# 지역명 출력
trs = browser.find_elements(By.CSS_SELECTOR, '#weather_table > tbody > tr')

for tr in trs:
    tds = tr.find_elements(By.CSS_SELECTOR ,'td')

    c1 = tds[0].text
    
    if tds[1].text != ' ':
        c2 = tds[1].text
    else:
        c2 = ''

    c3 = tds[2].text

    if tds[3].text != ' ':
        c4 = int(tds[3].text)
    else:
        c4 = 0

    if tds[4].text != ' ':
        c5 = int(tds[4].text)
    else:
        c5 = 0

    c6 = tds[5].text
    c7 = tds[6].text
    c8 = tds[7].text

    if tds[8].text != ' ':
        c9 = float(tds[8].text)
    else:
        c9 = 0

    if tds[9].text != ' ':
        c10 = float(tds[9].text)
    else:
        c10 = 0

    c11 = tds[10].text
    c12 = tds[11].text
    c13 = tds[12].text
    c14 = tds[13].text

    #SQL 실행
    sql = "INSERT INTO `weather` VALUES (%s, %s, %s, %d, %d, %f, %f, %f, %f, %f, %d, %s, %f, %f, NOW())".format(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14)
    cur.execute(sql)
    conn.commit()

# 데이터베이스 종료
conn.close()
print('insert 완료...')

# 가상 브라우저 종료
browser.close()

