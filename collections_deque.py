from collections import deque

storage = deque()
N = int(input())

for i in range(N):
    io = input().split()
    if(io[0] == 'append'):
        storage.append(io[1])
    elif(io[0] == 'popleft'):
        storage.popleft()
    elif(io[0] == 'appendleft'):
        storage.appendleft(io[1])
    elif(io[0] == 'pop'):
        storage.pop()

print(' '.join(storage))