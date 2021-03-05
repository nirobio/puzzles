# https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
    N = int(input())
    temp = []

    for _ in range(N):
        cmd = input().split()

        if cmd[0] == "insert":
            temp.insert(int(cmd[1]), int(cmd[2]))

        elif cmd[0] == "print":
            print(temp)

        elif cmd[0] == "remove":
            temp.remove(int(cmd[1]))

        elif cmd[0] == "append":
            temp.append(int(cmd[1]))

        elif cmd[0] == "sort":
            temp.sort()

        elif cmd[0] == "pop":
            temp.pop()

        elif cmd[0] == "reverse":
            temp.reverse()
