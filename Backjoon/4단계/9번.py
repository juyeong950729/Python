"""
날짜 : 2023/01/06
이름 : 조주영
내용 : 백준 4단계 9번 문제, 평균은 넘겠지
"""

n = int(input())

for _ in range(n):
    score = list(map(int, input().split()))
    avg = sum(score[1:]) / score[0]

    count = 0
    for i in score[1:]:
        if i > avg:
            count += 1
    
    rate = (count/score[0]) * 100
    print('{0:0.3f}%'.format(rate))
