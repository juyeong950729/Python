"""
날짜 : 2023/01/03
이름 : 조주영
내용 : 백준 2단계 7번 문제, 주사위 세개
"""

a, b, c = map(int, input().split())

if a == b == c:
    print(10000+a*1000)
elif a == b:
    print(1000+a*100)
elif a == c:
    print(1000+a*100)
elif b == c:
    print(1000+b*100)
else:
    print(max(a,b,c)*100)