import 'dart:math' as math;

class Diamond {
  final aIndex = 'A'.codeUnitAt(
    0,
  );

  List<String> _padding(
    int size,
  ) =>
      List.generate(
        size,
        (
          _,
        ) =>
            ' ',
      );

  Iterable<String> _rows(
    String letter,
  ) sync* {
    final letterIndex = (letter.codeUnitAt(
              0,
            ) -
            aIndex) +
        1;
    final size = letterIndex * 2 - 1;
    for (int y = 0; y < letterIndex; y++) {
      final outerPadding = (size - 1) ~/ 2 - y;
      final innerPadding = math.max(
        0,
        y * 2 - 1,
      );
      yield [
        ..._padding(
          outerPadding,
        ),
        String.fromCharCode(
          aIndex + y,
        ),
        ..._padding(
          innerPadding,
        ),
        if (y != 0)
          String.fromCharCode(
            aIndex + y,
          ),
        ..._padding(
          outerPadding,
        ),
      ].join();
    }
  }

  List<String> rows(String letter) {
    final diamond = [..._rows(letter)];
    for (int i = 1; i < diamond.length; i++) {
      diamond.add(
        diamond[diamond.length - i],
      );
    }
    return diamond;
  }
}
