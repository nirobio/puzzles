def integers(a, b, c, d):
    output = ((a**b) + (c**d))
    return output


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    result = integers(a, b, c, d)
    print(result)
