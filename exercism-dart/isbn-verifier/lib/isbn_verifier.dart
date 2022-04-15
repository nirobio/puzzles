import 'package:collection/collection.dart';

const numDigitsInIsbn = 10;

bool isValid(String isbn) {
  final digits = <int>{
    ...List<int>.generate(
      numDigitsInIsbn,
      (
        index,
      ) =>
          index,
    ),
  };

  final validCheckDigitCharacters = <String>{
    'x',
    ...digits.map(
      (
        d,
      ) =>
          '$d',
    ),
  };

  final cleaned = isbn
      .toLowerCase()
      .split(
        '',
      )
      .where(
        (
          e,
        ) =>
            validCheckDigitCharacters.contains(
          e,
        ),
      );

  final hasValidLeadingDigits = cleaned
      .take(
        numDigitsInIsbn - 1,
      )
      .every(
        (
          d,
        ) =>
            digits.contains(
          int.parse(d),
        ),
      );

  final hasValidCheckDigit = validCheckDigitCharacters.contains(
    cleaned.last,
  );

  // final isValid =

  final isValid = (IterableZip<dynamic>([
            List<int>.generate(
              numDigitsInIsbn,
              (
                d,
              ) =>
                  numDigitsInIsbn - d,
            ),
            cleaned
          ]).map<int>(
            (
              factorAndDigit,
            ) {
              final digit = factorAndDigit[1] as String;
              print(
                digit,
              );
              print(
                factorAndDigit[0],
              );

              return (factorAndDigit[0] as int) *
                  int.parse(
                    (digit == 'X' ? 10 : digit) as String,
                  );
            },
          )).sum %
          11 ==
      0;

  return (cleaned.length == numDigitsInIsbn) &&
      hasValidLeadingDigits &&
      hasValidCheckDigit &&
      isValid;
}
