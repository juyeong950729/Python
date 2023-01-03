"""
날짜 : 2023/01/03
이름 : 조주영
내용 : 백준 2단계 1번 문제, 두 수 비교하기
"""

a, b = map(int, input().split())

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')