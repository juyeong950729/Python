"""
날짜 : 2023/01/06
이름 : 조주영
내용 : 백준 4단계 3번 문제, 최소, 최대
"""

n = int(input())
nList = list(map(int, input().split()))
print(min(nList), max(nList))