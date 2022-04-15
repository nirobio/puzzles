class Anagram {
  List<String> findAnagrams(
    String word,
    List<String> candidates,
  ) {
    final mapOfLists = <String, List<String>>{};
    for (final letter in word.toLowerCase().split('')) {
      mapOfLists.update(
        letter,
        (
          list,
        ) {
          list.add(
            letter,
          );
          return list;
        },
        ifAbsent: () => [
          letter,
        ],
      );
    }

    final anagrams = <String>[];
    for (final c in candidates) {
      final copy = {...mapOfLists};
      final containsAllLetters = c
          .split(
        '',
      )
          .map(
        (
          letter,
        ) {
          if (!copy.containsKey(
            letter,
          )) {
            return false;
          }
          return copy[letter]!.remove(
            letter,
          );
        },
      ).every(
        (e) => e == true,
      );
      if (containsAllLetters &&
          copy.values
              .map(
                (
                  list,
                ) =>
                    list.isEmpty,
              )
              .every(
                (
                  e,
                ) =>
                    e == true,
              )) {
        anagrams.add(
          c,
        );
      }
    }
    return anagrams;
  }
}
