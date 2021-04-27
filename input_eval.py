# Evaluate whether P(x) = k, where P is a polynomial

x, k = map(int, input().split())
P = input()

y = lambda x:eval(P)
print(y(x) == k)