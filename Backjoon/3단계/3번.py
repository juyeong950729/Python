"""
날짜 : 2023/01/03
이름 : 조주영
내용 : 백준 3단계 3번 문제, 합
"""

n = int(input())
total, i = 0, 0

while i<=n:
    total += i
    i += 1

print(total)