"""
날짜 : 2023/01/06
이름 : 조주영
내용 : 백준 4단계 5번 문제, 과제 안 내신 분..?
"""

students = [i for i in range(1, 31)]

for _ in range(28):
    num = int(input())
    students.remove(num)

print(min(students))
print(max(students))