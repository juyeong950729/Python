"""
날짜 : 2023/01/03
이름 : 조주영
내용 : 백준 3단계 2번 문제, A+B - 3
"""

t = int(input())
for i in range(1, t+1):
    a, b = map(int, input().split())
    print(a*b)