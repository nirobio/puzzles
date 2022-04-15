import 'package:collection/collection.dart';

class Hamming {
  int distance(String left, String right) {
    if (left.length != right.length) {
      if ((left.isEmpty || right.isEmpty)) {
        throw ArgumentError(
          'no strand must be empty',
        );
      }

      throw ArgumentError(
        'left and right strands must be of equal length',
      );
    }

    return IterableZip(
      [
        left.split(
          '',
        ),
        right.split(
          '',
        ),
      ],
    )
        .map(
          (
            pair,
          ) =>
              pair[0] == pair[1] ? 0 : 1,
        )
        .sum;
  }
}
