"""
날짜 : 2023/01/04
이름 : 조주영
내용 : 백준 3단계 12번 문제, 더하기 사이클
"""

num = int(input())
newNum = num
count = 0

while True:
    ten = newNum // 10
    one = newNum % 10
    newOne = (ten+one) % 10
    newNum = (one * 10) + newOne
    count += 1

    if(newNum == num):
        break

print(count)