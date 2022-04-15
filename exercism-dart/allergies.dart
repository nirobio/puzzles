class Allergies {
  static const foods = [
    'eggs',
    'peanuts',
    'shellfish',
    'strawberries',
    'tomatoes',
    'chocolate',
    'pollen',
    'cats',
  ];

  final foodMap = Map.fromIterables(
    foods,
    List.generate(
      foods.length,
      (
        index,
      ) =>
          '1'.padRight(
        index,
        '0',
      ),
    ),
  );

  bool allergicTo(
    String food,
    int score,
  ) =>
      score &
          int.parse(
            foodMap[food]!,
            radix: 2,
          ) >
      0;

  List<String> list(
    int score,
  ) {
    return foods
        .map(
          (
            food,
          ) =>
              allergicTo(
            food,
            score,
          )
                  ? food
                  : null,
        )
        .where(
          (
            e,
          ) =>
              e != null,
        )
        .toList() as List<String>;
  }
}
