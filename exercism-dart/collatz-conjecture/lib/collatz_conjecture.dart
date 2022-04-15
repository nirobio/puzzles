class CollatzConjecture {
  int steps(int x) {
    if (x < 1) {
      throw ArgumentError(
        'Only positive numbers are allowed',
      );
    }

    int numSteps = 0;
    while (x != 1) {
      numSteps++;
      if (x % 2 == 0) {
        x ~/= 2;
      } else {
        x = 3 * x + 1;
      }
    }
    return numSteps;
  }
}
