M = int(input())
m = set(map(int, input().split()))
N = int(input())
n = set(map(int, input().split()))

m_diff = m.difference(n)
n_diff = n.difference(m)

x = m_diff.union(n_diff)
for i in sorted(list(x)):
    print(i)