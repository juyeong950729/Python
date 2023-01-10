"""
날짜 : 2023/01/10
이름 : 조주영
내용 : 백준 6단계 5번 문제, 단어 공부
"""

alpha = [0 for i in range(1, 27)]

noun = map(str, input())
for i in range(len(noun)):
    ord(noun[i])