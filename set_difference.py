n_a = int(input())
a = set(input().split())
n_b = int(input())
b = set(input().split())

diff = ((set(a)).difference(set(b)))
print(len(diff))