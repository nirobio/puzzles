class ResistorColor {
  final codes = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9,
  };

  int colorCode(String color) => codes[color]!;

  List<String> get colors {
    final list = codes.entries.toList();
    list.sort((left, right) => left.value - right.value);
    return list.map<String>((entry) => entry.key).toList();
  }
}
