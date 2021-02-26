# https://www.hackerrank.com/challenges/list-comprehensions/problem

X = int(input())
Y = int(input())
Z = int(input())
n = int(input())

X += 1
Y += 1
Z += 1

permutations = [[x,y,z] for x in range(X) for y in range(Y) for z in range(Z) if x+y+z != n]
print(permutations)
