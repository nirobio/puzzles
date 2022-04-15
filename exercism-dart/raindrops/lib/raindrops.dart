class Raindrops {
  String convert(
    int x,
  ) {
    String sound = '';
    if (x % 3 == 0) {
      sound += 'Pling';
    }
    if (x % 5 == 0) {
      sound += 'Plang';
    }
    if (x % 7 == 0) {
      sound += 'Plong';
    }
    if (sound.isEmpty) {
      return '$x';
    }
    return sound;
  }
}
