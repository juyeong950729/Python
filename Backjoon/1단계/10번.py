"""
날짜 : 2023/01/02
이름 : 조주영
내용 : 백준 1단계 10번 문제 나머지
"""

a, b, c = map(int, input().split())
rs1, rs2, rs3, rs4 = (a+b)%c, ((a%c)+(b%c))%c, (a*b)%c, ((a%c)*(b%c))%c
print(rs1)
print(rs2)
print(rs3)
print(rs4)