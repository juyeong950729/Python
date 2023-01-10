"""
날짜 : 2023/01/10
이름 : 조주영
내용 : 백준 6단계 4번 문제, 문자열 반복
"""

t = int(input())

for i in range(t):
    rs = list(map(str, input().split()))
    r = int(rs[0])
    s = rs[1]

    for i in range(len(s)):
        for j in range(r):
            print(s[i], end='')
    print('')