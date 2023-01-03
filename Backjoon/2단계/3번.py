"""
날짜 : 2023/01/03
이름 : 조주영
내용 : 백준 2단계 3번 문제, 윤년
"""

year = int(input())

if year % 4 == 0 and year % 100 != 0:
    print('1')
elif year % 400 == 0:
    print('1')
else:
    print('0')