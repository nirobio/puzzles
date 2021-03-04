students = []
nameScore = []

for _ in range(int(input())):

    temp = []

    name = input()
    score = float(input())

    temp.append(name)
    temp.append(score)

    nameScore.append(score)
    students.append(temp)

nameScore = list(dict.fromkeys(nameScore))
nameScore.sort()

if len(students) >= 2:
    second_lowest_students = []
    second_lowest_score = nameScore[1]

    for i in students:
        if second_lowest_score in i:
            # print(i[0])
            second_lowest_students.append(i[0])
        else:
            pass
    print('\n'.join(sorted(second_lowest_students, key=lambda second_lowest_students: second_lowest_students)))

else:
    print(students[0][0])
