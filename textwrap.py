import textwrap
import sys

def wrap(string, max_width):

   # for line in (textwrap.wrap(string, width = max_width)):
   #    print(line)
    return "\n".join(textwrap.wrap(string, max_width))


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
