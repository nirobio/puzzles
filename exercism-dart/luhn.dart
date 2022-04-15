import 'package:collection/collection.dart';

class Luhn {
  bool valid(
    String num,
  ) {
    if (num.length < 2) {
      return false;
    }

    const digits = {
      '0',
      '1',
      '2',
      '3',
      '4',
      '5',
      '6',
      '7',
      '8',
      '9',
    };

    final List<String> cleaned = num.split(
      '',
    )
        .where(
          (
            e,
          ) =>
              digits.contains(
            e,
          ),
        )
        .toList()
        .reversed
        .toList();

    final output = <int>[];
    for (int i = 1; i < cleaned.length + 1; i++) {
      if (i % 2 == 0) {
        int x = int.parse(
              cleaned[i],
            ) *
            2;

        output.add(
          x > 9 ? x - 9 : x,
        );
      }
    }
    return output.sum % 10 == 0;
  }
}
