k = int(input())
array = list(map(int, input().split()))

set_array = set(array)

print(((sum(set_array)*k)-(sum(array)))//(k-1))