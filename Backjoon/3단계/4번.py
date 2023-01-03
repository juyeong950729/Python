"""
날짜 : 2023/01/03
이름 : 조주영
내용 : 백준 3단계 4번 문제, 영수증
"""

x = int(input())
n = int(input())
total = 0

for i in range(1, n+1):
    a, b = map(int, input().split())
    total += a*b
    
if total == x:
    print('Yes')
else:
    print('No')