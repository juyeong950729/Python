"""
날짜 : 2023/01/06
이름 : 조주영
내용 : 백준 4단계 1번 문제, 개수 세기
"""

n = int(input())
nList = list(map(int, input().split()))
v = int(input())
print(nList.count(v))