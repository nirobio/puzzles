import 'dart:math' as math;

class PrimeFactors {
  List<int> factors(
    int x,
  ) {
    final fs = <int>[];
    int i = 2;
    while (i <
        math
            .pow(
              x,
              0.5,
            )
            .floor()) {
      if (x % i == 0) {
        fs.add(
          i,
        );
        x ~/= i;
      } else {
        i++;
      }
    }
    return fs;
  }
}
