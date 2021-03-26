for _ in range(int(input())):
    lengthA = input()
    a = set(input().split())
    lengthB = input()
    b = set(input().split())

    print(a.issubset(b))
