class WordCount {
  final wordFilter = RegExp(
    r"^\'(\w+)\'$",
  );

  final wordBoundaries = RegExp(
    r'[\s\,]',
  );

  static int codeUnit(String s) => s.codeUnitAt(0);

  static Iterable<int> _range(
    int beg,
    int end,
  ) =>
      [
        for (int i = beg; i <= end; i++) i,
      ];

  final validCharCodes = <int>{
    ..._range(
      codeUnit('0'),
      codeUnit('9'),
    ),
    ..._range(
      codeUnit('a'),
      codeUnit('z'),
    ),
    codeUnit("'"),
  };

  Map<String, int> countWords(
    String s,
  ) =>
      s
          .toLowerCase()
          .split(
            wordBoundaries,
          )
          .where(
            (
              element,
            ) =>
                element.isNotEmpty,
          )
          .map(
            (
              word,
            ) =>
                word
                    .split(
                      '',
                    )
                    .where(
                      (letter) => validCharCodes.contains(
                        codeUnit(
                          letter,
                        ),
                      ),
                    )
                    .join(),
          )
          .map(
        (
          word,
        ) {
          final w = wordFilter.firstMatch(
            word,
          );
          return w == null
              ? word
              : w.group(
                  1,
                );
        },
      ).fold(
        {},
        (
          acc,
          e,
        ) {
          acc.update(
            e!,
            (
              value,
            ) =>
                value + 1,
            ifAbsent: () => 1,
          );
          return acc;
        },
      );
}
