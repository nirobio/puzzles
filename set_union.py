n = int(input())
English = set(list(input().split()))
b = int(input())
French = set(list(input().split()))

print(len(English.union(French)))
