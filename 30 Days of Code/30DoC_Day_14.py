# class constructor takes an array of integers as a parameter and saves it to the __elements instance variable.

class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        maxDiff = 0

   # computeDifference method that finds the maximum absolute difference between any 2 numbers in __elements and stores it in the maximumDifference instance variable

        for i in range(len(self.__elements)):
            for j in range(len(self.__elements)):
                absolute = abs(self.__elements[i] - self.__elements[j])
                if absolute > maxDiff:
                    maxDiff = absolute

        self.maximumDifference = maxDiff


# End of Difference class


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
