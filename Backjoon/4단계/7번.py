"""
날짜 : 2023/01/06
이름 : 조주영
내용 : 백준 4단계 7번 문제, 평균
"""

n = int(input())
score = list(map(int, input().split()))
maxNum = max(score)

avg = sum(score)/n
newAvg = avg/maxNum*100
print(newAvg)
