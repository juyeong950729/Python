"""
날짜 : 2023/01/04
이름 : 조주영
내용 : 백준 3단계 12번 문제, 더하기 사이클
"""

n1 = int(input())
n = n1

ten = n//10
one = n%10

while True:

    newNum = 0
    count = 0

    if newNum == n1:
        break
    elif n >= 10:
        n = ten+one
        newNum = one*10+n
        n = newNum
        count += 1
    elif n < 10:
        n = one
        newNum = one*10
        n = newNum
        count += 1
    else:
        pass

print(count)
