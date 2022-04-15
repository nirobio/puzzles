enum Tri { notATriangle, equilateral, isosceles, scalene }

class Triangle {
  Tri _triType(
    num a,
    num b,
    num c,
  ) {
    if (a == 0 || b == 0 || c == 0) {
      return Tri.notATriangle;
    } else if (a + b >= c && b + c >= a && c + a >= b) {
      if (a == b && b == c) {
        return Tri.equilateral;
      } else if (a == b || b == c || c == a) {
        return Tri.isosceles;
      } else if (a != b && b != c && c != a) {
        return Tri.scalene;
      }
    }
    return Tri.notATriangle;
  }

  bool equilateral(
    num a,
    num b,
    num c,
  ) =>
      _triType(a, b, c) == Tri.equilateral;

  bool isosceles(
    num a,
    num b,
    num c,
  ) =>
      _triType(a, b, c) == Tri.isosceles;

  bool scalene(
    num a,
    num b,
    num c,
  ) =>
      _triType(a, b, c) == Tri.scalene;
}
