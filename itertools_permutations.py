from itertools import permutations

S, k = input().split(sep=" ")
perm = (list(permutations(str(S), int(k))))
sortPerm = sorted(perm)

for permutation in sortPerm:
    print("".join(permutation))
