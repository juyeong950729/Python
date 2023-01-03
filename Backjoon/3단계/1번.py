"""
날짜 : 2023/01/03
이름 : 조주영
내용 : 백준 3단계 1번 문제, 구구단
"""

n = int(input())

for i in range(10):
    print('{} * {} = {}'.format(n, i, n*i))
