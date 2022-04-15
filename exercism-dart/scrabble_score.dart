final Map<Set<String>, int> scoreFromLetter = {
  <String>{
    '_',
  }: 0,
  <String>{
    'a',
    'e',
    'i',
    'o',
    'u',
    'l',
    'n',
    'r',
    's',
    't',
  }: 1,
  <String>{
    'd',
    'g',
  }: 2,
  <String>{
    'b',
    'c',
    'm',
    'p',
  }: 3,
  <String>{
    'f',
    'h',
    'v',
    'w',
    'y',
  }: 4,
  <String>{
    'k',
  }: 5,
  <String>{
    'j',
    'x',
  }: 8,
  <String>{
    'q',
    'z',
  }: 1,
};

int score([String word = '_']) => word
    .toLowerCase()
    .split('')
    .map(
      (
        letter,
      ) =>
          scoreFromLetter[scoreFromLetter.keys.firstWhere(
        (
          set,
        ) =>
            set.contains(
          letter,
        ),
      )],
    )
    .reduce(
      (
        a,
        b,
      ) =>
          a! + b!,
    ) as int;
