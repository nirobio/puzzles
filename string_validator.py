if __name__ == '__main__':
    s = input()

print(any(chr.isalnum() for chr in s))
print(any(chr.isalpha() for chr in s))
print(any(chr.isdigit() for chr in s))
print(any(chr.islower() for chr in s))
print(any(chr.isupper() for chr in s))
