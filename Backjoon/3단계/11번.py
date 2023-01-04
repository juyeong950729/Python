"""
날짜 : 2023/01/04
이름 : 조주영
내용 : 백준 3단계 11번 문제, A+B - 4
"""

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)

    except EOFError:
        break