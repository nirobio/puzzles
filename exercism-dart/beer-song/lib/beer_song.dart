class SentenceFragments {
  SentenceFragments(
    this.numBottlesOne,
    this.numBottlesTwo,
    this.numBottlesThree, {
    this.pluralOne = true,
    this.pluralTwo = true,
    this.secondSentencePrefix = 'Take one down and pass it around',
  });

  final String numBottlesOne;
  final String numBottlesTwo;
  final String numBottlesThree;
  final bool pluralOne;
  final bool pluralTwo;
  final String secondSentencePrefix;
}

class BeerSong {
  static const maxBottles = 99;

  String _take(
    String s,
  ) =>
      'Take $s down and pass it around';

  SentenceFragments _fragments(
    int verseIndex,
  ) {
    switch (verseIndex) {
      case 0:
        return SentenceFragments(
          'No',
          'no',
          '99',
          secondSentencePrefix: 'Go to the store and buy some more',
        );
      case 1:
        return SentenceFragments(
          '$verseIndex',
          '$verseIndex',
          'no',
          pluralOne: false,
          secondSentencePrefix: _take(
            'it',
          ),
        );
      default:
        return SentenceFragments(
          '$verseIndex',
          '$verseIndex',
          '${verseIndex - 1}',
        );
    }
  }

  List<String> _verse(
    int verseIndex,
  ) {
    final fragments = _fragments(
      verseIndex,
    );
    return [
      '${fragments.numBottlesOne} bottle${fragments.pluralOne ? 's' : ''} of beer on the wall, ${fragments.numBottlesTwo} bottles of beer.',
      '${fragments.secondSentencePrefix}, ${fragments.numBottlesThree} bottles of beer on the wall.'
    ];
  }

  Iterable<List<String>> _build(
    int verseIndex,
    int numVerses,
  ) sync* {
    for (int i = 0; i < numVerses - 1; i++) {
      yield _verse(
        verseIndex,
      );
      yield [
        '',
      ];
      verseIndex--;
    }
    yield _verse(
      verseIndex,
    );
  }

  List<String> recite(
    int verseIndex,
    int numVerses,
  ) {
    return _build(
      verseIndex,
      numVerses,
    )
        .expand(
          (
            s,
          ) =>
              s,
        )
        .toList();
  }
}
