def mutate_string(string, position, character):
    list1 = list(s)
    index = int(i)
    list1[index] = c
    string1 = (''.join(map(str, list1)))
    return string1


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
