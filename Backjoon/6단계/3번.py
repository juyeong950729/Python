"""
날짜 : 2023/01/10
이름 : 조주영
내용 : 백준 6단계 3번 문제, 알파벳 찾기
"""

alpha = [-1 for i in range(1, 27)]

sList = list(map(str, input()))

for i in range(len(sList)):
    if alpha[ord(sList[i])-97] == -1:
        alpha[ord(sList[i])-97] = i
    else:
        pass

printS = ' '.join(str(_) for _ in alpha)

print(printS)