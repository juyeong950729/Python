"""
날짜 : 2023/01/06
이름 : 조주영
내용 : 백준 4단계 6번 문제, 나머지
"""

nSet = {}
for _ in range(10):
    num = int(input())
    nSet.append(num % 42)
print (len(nSet))