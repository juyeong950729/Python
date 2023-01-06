"""
날짜 : 2023/01/06
이름 : 조주영
내용 : 백준 4단계 8번 문제, OX퀴즈
"""

n = int(input())

for _ in range(n):
    ox = list(input())
    s, ss = 0, 0
    for o in ox:
        if o == 'O':
            s += 1
            ss += s
        else:
            s = 0
    print(ss)
