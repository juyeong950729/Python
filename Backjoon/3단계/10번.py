"""
날짜 : 2023/01/03
이름 : 조주영
내용 : 백준 3단계 10번 문제, A+B - 5
"""

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a+b)