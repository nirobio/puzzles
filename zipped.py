
n, x = map(int, input().split())
tests = []
for _ in range(x):
    tests.append(map(float, input().split()))

for i in zip(*tests):
    print(sum(i)/len(i))