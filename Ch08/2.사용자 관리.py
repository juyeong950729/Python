"""
날짜 : 2023/01/13
이름 : 조주영
내용 : 파이썬 사용자 관리 프로그램 실습
"""

import pymysql

# 데이터베이스 접속
conn = pymysql.connect(host='127.0.0.1',
                        user='root',
                        password='1234',
                        db='java2db', 
                        charset='utf8')

while True:
    print('0:종료, 1:등록, 2:조회, 3:검색, 4:삭제')
    answer = 0
    
    try:
        answer = int(input('선택 : '))
    except:
        print('숫자를 입력하세요.')
        continue

    if answer == 0:
        pass
    elif answer == 1:
        pass
    elif answer == 2:
        pass
    elif answer == 3:
        pass
    elif answer == 4:
        pass
    else:
        pass

# 데이터베이스 종료
conn.close()
print('프로그램 종료...')