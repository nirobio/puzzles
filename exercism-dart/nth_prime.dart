class NthPrime {
  int prime(int nth) {
    if (nth < 1) {
      throw ArgumentError(
        'There is no zeroth prime',
      );
    }

    List<int> xs = List.generate(
      104741,
      (
        index,
      ) =>
          index + 2,
    );

    for (int i = 1; i < nth; i++) {
      xs = xs
          .skip(
            i,
          )
          .where(
            (
              x,
            ) =>
                x % xs[i - 1] != 0,
          )
          .toList();
    }
    return xs[nth - 1];
  }
}
