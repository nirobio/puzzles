class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        total = 0

        for scores in self.scores:
            total += scores

        meanScore = total / len(self.scores)

        if 90 <= meanScore <= 100:
            return "O"
        if 80 <= meanScore < 90:
            return "E"
        if 70 <= meanScore < 80:
            return "A"
        if 55 <= meanScore < 70:
            return "P"
        if 40 <= meanScore < 55:
            return "D"
        else:
            return "T"


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
