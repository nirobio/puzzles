import 'package:collection/collection.dart';

class PascalsTriangle {
  List<List<int>> pairs(List<int> input) {
    var len = input.length;
    var size = 2;
    var pairs = <List<int>>[];

    for (var i = 0; i < len; i += size) {
      var end = (i + size < len) ? i + size : len;
      pairs.add(
        input.sublist(
          i,
          end,
        ),
      );
    }

    return pairs;
  }

  List<List<int>> _rows(int depth, [List<List<int>> triangle = const []]) {
    if (depth == 0) {
      return triangle;
    }
    if (depth == 1) {
      triangle.add(
        [
          0,
          1,
          0,
        ],
      );
      return triangle;
    }
    triangle.add(
      [
        0,
        ...pairs(_rows(
          depth - 1,
        )[depth - 1])
            .map(
          (
            pair,
          ) =>
              pair[0] + pair[1],
        ),
        0
      ],
    );

    return triangle;
  }

  List<List<int>> rows(
    int row,
  ) {
    return _rows(
      row,
    )
        .mapIndexed((
          index,
          list,
        ) =>
            list
                .skip(
                  1,
                )
                .take(
                  index,
                )
                .toList())
        .toList();
  }
}
