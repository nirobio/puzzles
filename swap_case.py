def swap_case(s):
    converted = ""
    for character in s:
        if (character >= 'a' and character <= 'z'):
            converted += str(character.upper())
        elif (character >= 'A' and character <= 'Z'):
            converted += str(character.lower())
        else:
            converted += str(character)
    return converted

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
