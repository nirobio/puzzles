class PhoneNumber {
  final matcher = RegExp(
    r'^.*(1?).*([2-9]).*(\d).*(\d).*([2-9]).*(\d).*(\d).*(\d).*(\d).*(\d).*(\d).*$',
  );

  final letters = RegExp(
    r'[a-z]',
  );
  final punctuation = RegExp(
    r'\@\:\!',
  );

  final digit = RegExp(
    r'\d',
  );

  final nonDigit = RegExp(
    r'[^\d]',
  );

  final invalidChars = RegExp(
    r'([^0-9\(\)\-\+\ \.])',
  );

  String? clean(
    String number,
  ) {
    final ds = number
        .replaceAll(
          nonDigit,
          '',
        )
        .split(
          '',
        );

    if (matcher.hasMatch(
      number,
    )) {
      if (ds.length < 10) {
        throw FormatException(
          'incorrect number of digits',
        );
      } else if (ds.length > 11) {
        throw FormatException(
          'more than 11 digits',
        );
      } else if (ds.length == 11 && ds[0] != '1') {
        throw FormatException(
          '11 digits must start with 1',
        );
      }
      return digit
          .allMatches(
        number,
      )
          .map((
        match,
      ) {
        return match.group(
          0,
        );
      }).join();
    } else {
      if (letters.hasMatch(
        number,
      )) {
        throw FormatException(
          'letters are not permitted',
        );
      }

      if (punctuation.hasMatch(
        number,
      )) {
        throw FormatException(
          'punctuations not permitted',
        );
      }

      if (ds.length == 10) {
        if (ds[ds.length - 7] == '0') {
          throw FormatException('exchange code cannot start with zero');
        }
        if (ds[ds.length - 7] == '1') {
          throw FormatException(
            'exchange code cannot start with one',
          );
        }
      } else if (ds.length == 11) {
        if (ds[0] == '0') {
          throw FormatException(
            'area code cannot start with zero',
          );
        } else if (ds[0] == '1') {
          throw FormatException(
            'area code cannot start with one',
          );
        }
        if (ds[1] == '0') {
          throw FormatException(
            'area code cannot start with zero',
          );
        } else if (ds[1] == '1') {
          throw FormatException(
            'area code cannot start with one',
          );
        }

        if (ds[ds.length - 7] == '0') {
          throw FormatException(
            'exchange code cannot start with zero',
          );
        } else if (ds[ds.length - 7] == '1') {
          throw FormatException(
            'exchange code cannot start with one',
          );
        }
      }
    }
  }
}
