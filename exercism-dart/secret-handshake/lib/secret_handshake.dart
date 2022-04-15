class SecretHandshake {
  int _intFromBinaryString(
    String s,
  ) =>
      int.parse(
        s,
        radix: 2,
      );

  void _addEvent(
    int x,
    String binary,
    String event,
    List<String> handshake,
  ) {
    if (x &
            _intFromBinaryString(
              binary,
            ) >
        0) {
      handshake.add(
        event,
      );
    }
  }

  List<String> commands(int x) {
    final handshake = <String>[];
    _addEvent(
      x,
      '1',
      'wink',
      handshake,
    );
    _addEvent(
      x,
      '10',
      'double blink',
      handshake,
    );
    _addEvent(
      x,
      '100',
      'close your eyes',
      handshake,
    );
    _addEvent(
      x,
      '1000',
      'jump',
      handshake,
    );
    if (x &
            _intFromBinaryString(
              '10000',
            ) >
        0) {
      return handshake.reversed.toList();
    }
    return handshake;
  }
}
