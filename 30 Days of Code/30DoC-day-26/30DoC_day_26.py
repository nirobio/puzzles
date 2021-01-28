actual = str(input()).split(" ")
actualDay = int(actual[0])
actualMonth = int(actual[1])
actualYear = int(actual[2])

expected = str(input()).split(" ")
expectedDay = int(expected[0])
expectedMonth = int(expected[1])
expectedYear = int(expected[2])

fine = 0

if actualYear > expectedYear:
    fine = 10000
elif actualYear == expectedYear:
    if actualMonth > expectedMonth:
        fine = ((actualMonth - expectedMonth) * 500)
    elif (actualMonth == expectedMonth) and (actualDay > expectedDay):
        fine = ((actualDay - expectedDay) * 15)

print(fine)
