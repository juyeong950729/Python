"""
날짜 : 2023/01/03
이름 : 조주영
내용 : 백준 3단계 9번 문제, 별 찍기 - 2
"""

n = int(input())

for i in range(1, n+1):
    for end in range(n-i):
        print(' ', end='')
    print('*' * n)
    