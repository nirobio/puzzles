import 'package:collection/collection.dart';

class Minesweeper {
  late final List<List<String>> _board;

  Minesweeper(
    List<String> board,
  ) {
    _board = board
        .map(
          (
            s,
          ) =>
              s
                  .split(
                    '',
                  )
                  .toList(),
        )
        .toList();
  }

  String _inRange(
    int y,
    int x,
  ) =>
      (y < 0 || y > _board.length || x < 0 || x > _board[0].length)
          ? ' '
          : _board[y][x];

  int _count(
    int y,
    int x,
  ) {
    return [
      _inRange(y + 1, x),
      _inRange(y + 1, x + 1),
      _inRange(y, x + 1),
      _inRange(y - 1, x + 1),
      _inRange(y - 1, x),
      _inRange(y - 1, x - 1),
      _inRange(y, x - 1),
      _inRange(y + 1, x - 1),
    ]
        .map(
          (
            c,
          ) =>
              c == '*' ? 1 : 0,
        )
        .sum;
  }

  List<String> get annoted {
    if (_board.isEmpty) {
      return [];
    }
    final height = _board.length;
    final width = _board[0].length;

    for (int y = 0; y < height; y++) {
      for (int x = 0; x < width; x++) {
        final current = _board[y][x];
        if (current == '*') {
          continue;
        } else {
          final count = _count(
            y,
            x,
          );
          _board[x][y] = (count == 0 ? ' ' : '$count');
        }
      }
    }

    return _board.map((list) => list.join()).toList();
  }
}
