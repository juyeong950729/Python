"""
날짜 : 2023/01/03
이름 : 조주영
내용 : 백준 2단계 6번 문제, 오븐 시계
"""

a,b = map(int, input().split())
c = int(input())

if b+c < 60:
    print('{} {}'.format(a, b+c))
elif b+c >= 60:
    int(i = b+c/60)
    if a+i > 24:
        print('{} {}'.format(24-(a+i), (b+c)-60*i))
    else:
        print('{} {}'.format(a+i, (b+c)-60*i))
else:
    pass
