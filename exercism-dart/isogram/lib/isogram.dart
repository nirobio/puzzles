class Isogram {
  bool isIsogram(String s) {
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
    return letterCounts.values
        .map(
          (
            count,
          ) =>
              count < 2,
        )
        .every(
          (
            b,
          ) =>
              b,
        );
  }
}
