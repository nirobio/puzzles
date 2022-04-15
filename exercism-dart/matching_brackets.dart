class MatchingBrackets {
  bool isPaired(String s) {
    int parenCount = 0;
    int bracketCount = 0;
    int braceCount = 0;
    for (final letter in s.split(
      '',
    )) {
      switch (letter) {
        case '(':
          parenCount++;
          break;
        case '[':
          bracketCount++;
          break;
        case '{':
          braceCount++;
          break;
        case ')':
          parenCount--;
          break;
        case ']':
          bracketCount--;
          break;
        case '}':
          braceCount--;
          break;
        default:
          continue;
      }
    }

    return parenCount == 0 && bracketCount == 0 && braceCount == 0;
  }
}
