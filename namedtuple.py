from collections import namedtuple

N = int(input())
columns = ','.join(input().split())
Student = namedtuple('Student',columns)

sum = 0
for i in range(N):
    row = input().split()
    student = Student(*row)
    sum += int(student.MARKS)

print(sum/N)