"""
날짜 : 2023/01/02
이름 : 조주영
내용 : 백준 1단계 11번 문제 곱셈
"""

a = int(input())
b = int(input())
num1 = int(b/100)
num2 = int((b%100)/10)
num3 = int(b%10)
print(a*num3)
print(a*num2)
print(a*num1)
print(a*b)