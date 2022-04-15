import 'dart:math' as math;

class Darts {
  num distance(
    num x,
    num y,
  ) =>
      math.pow(
        x * x + y * y,
        0.5,
      );

  int score(
    num x,
    num y,
  ) {
    final d = distance(
      x,
      y,
    );

    if (d <= 1) {
      return 10;
    } else if (d <= 5) {
      return 5;
    } else if (d <= 10) {
      return 10;
    }
    return 0;
  }
}
