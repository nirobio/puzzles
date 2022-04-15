class Bob {
  String response(
    String sentence,
  ) {
    final isYelling = sentence == sentence.toUpperCase();

    if (sentence.isEmpty) {
      return 'Fine. Be that way';
    }

    if (sentence
            .split(
              '',
            )
            .last ==
        '?') {
      if (isYelling) {
        return "Calm down, I know what I'm doing!";
      } else {
        return 'Sure.';
      }
    } else if (isYelling) {
      return 'Whoa, chill out!';
    }
    return 'Whatever.';
  }
}
