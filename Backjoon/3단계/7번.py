"""
날짜 : 2023/01/03
이름 : 조주영
내용 : 백준 3단계 7번 문제, A+B - 8
"""

t = int(input())

for i in range(1, t+1):
    a, b = map(int, input().split())
    print('Case #', end=(''))
    print(i, end=(': '))
    print('{} + {} ='.format(a, b), end=(' '))
    print(a+b)