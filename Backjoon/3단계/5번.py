"""
날짜 : 2023/01/03
이름 : 조주영
내용 : 백준 3단계 5번 문제, 빠른 A+B
"""

import sys
t = int(sys.stdin.readline())
for i in range(1, t+1):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)