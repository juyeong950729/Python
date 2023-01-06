"""
날짜 : 2023/01/06
이름 : 조주영
내용 : 백준 4단계 2번 문제, X보다 작은 수
"""

n, x = map(int, input().split())
nList = list(map(int, input().split()))

for i in nList:
    if i < x:
        print(i, end=" ")