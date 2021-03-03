def split_and_join(line):
    #print(*(line.split()), sep='-')
    separated = ("-".join(str(x) for x in line.split()))
    return separated


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
