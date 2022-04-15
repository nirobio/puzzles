import 'dart:math' as math;

import 'package:collection/collection.dart';

class DifferenceOfSquares {
  Iterable<int> _digits(int x) => '$x'.split('').map((i) => int.parse(i));

  Iterable<List<int>> _uniquePairs(int x) sync* {
    final xs = List.generate(
      _digits(x).length,
      (index) => index + 1,
    );

    xs.forEachIndexed(
      (y, b) {
        xs.forEachIndexed(
          (x, a) sync* {
            if (y < x) {
              yield [a, b];
            }
          },
        );
      },
    );
  }

  int squareOfSum(int x) => math.pow(_digits(x).sum, 2).toInt();

  int sumOfSquares(int x) => _digits(x).map((i) => math.pow(i, 2).toInt()).sum;

  // int differenceOfSquares(int x) => sumOfSquares(x) - squareOfSum(x);
  int differenceOfSquares(int x) =>
      2 *
      _uniquePairs(x)
          .map(
            (p) => p[0] * p[1],
          )
          .sum;
}
