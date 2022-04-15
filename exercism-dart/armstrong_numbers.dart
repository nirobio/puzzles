import 'dart:math' as math;

import 'package:collection/collection.dart';

class ArmstrongNumbers {
  bool isArmstrongNumber(
    int num,
  ) {
    final digits = '$num'.split('');
    return num ==
        digits
            .map<int>(
              (
                d,
              ) =>
                  math
                      .pow(
                        int.parse(
                          d,
                        ),
                        digits.length,
                      )
                      .round(),
            )
            .sum;
  }
}
