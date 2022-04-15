class Acronym {
  final nonLetter = RegExp(
    r'[^a-z]',
  );

  String abbreviate(String s) {
    return s
        .toLowerCase()
        .split(
          nonLetter,
        )
        .map((
      word,
    ) {
      try {
        return word
            .split(
              '',
            )
            .first
            .toUpperCase();
      } on StateError {
        return '';
      }
    }).join();
  }
}
