class Pangram {
  static const alphabetLength = 26;

  final letters = List.generate(
    alphabetLength,
    (
      index,
    ) =>
        String.fromCharCode(
      'a'.codeUnitAt(
            0,
          ) +
          index,
    ),
  );

  bool isPangram(
    String s,
  ) {
    final letterCounts = <String, int>{};

    for (final letter in s.toLowerCase().split(
          '',
        )) {
      letterCounts.update(
        letter,
        (
          count,
        ) =>
            count + 1,
        ifAbsent: () => 1,
      );
    }

    return letters.every(
      (
        l,
      ) =>
          letterCounts[l] == 1,
    );
  }
}
