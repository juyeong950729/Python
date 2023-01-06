"""
날짜 : 2023/01/06
이름 : 조주영
내용 : 백준 4단계 4번 문제, 최댓값
"""

nList = []

for i in range(9):
    nList.append(int(input()))

maxNum = max(nList)
print(maxNum)
print(nList.index(maxNum)+1)