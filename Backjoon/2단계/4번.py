"""
날짜 : 2023/01/03
이름 : 조주영
내용 : 백준 2단계 4번 문제, 사분면 고르기
"""

x = int(input())
y = int(input())

if x>0 and y>0:
    print('1')
elif x<0 and y>0:
    print('2')
elif x<0 and y<0:
    print('3')
elif x>0 and y<0:
    print('4')
else:
    pass