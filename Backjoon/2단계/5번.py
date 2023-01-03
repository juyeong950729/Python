"""
날짜 : 2023/01/03
이름 : 조주영
내용 : 백준 2단계 5번 문제, 알람 시계
"""

h, m = map(int, input().split())

if m >= 45:
    print('{} {}'.format(h, m-45))
elif h != 0:
    print('{} {}'.format(h-1, m+15))
elif h == 0:
    print('{} {}'.format(23, m+15))
else:
    pass