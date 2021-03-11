def print_rangoli(n):
    alnum = "abcdefghijklmnopqrstuvwxyz"
    data = [alnum[i] for i in range(n)]
    elements = list(range(n))
    elements = elements[:-1] + elements[::-1]
    for i in elements:
        temp = data[-(i + 1):]
        row = temp[::-1] + temp[1:]
        print("-".join(row).center(n * 4 - 3, "-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
