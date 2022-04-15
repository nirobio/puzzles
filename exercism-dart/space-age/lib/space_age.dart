class SpaceAge {
  static const Map<String, double> orbitalPeriod = {
    'Mercury': 0.2408467,
    'Venus': 0.61519726,
    'Earth': 1.0,
    'Mars': 1.8808158,
    'Jupiter': 11.862615,
    'Saturn': 29.447498,
    'Uranus': 84.016846,
    'Neptune': 164.79132,
  };

  static const secondsPerEarthYear = 60 * 60 * 24 * 365.25;

  static double yearsFromSeconds(
    double seconds,
  ) =>
      seconds / secondsPerEarthYear;

  double age({
    required String planet,
    required double seconds,
  }) =>
      double.parse((yearsFromSeconds(
                seconds,
              ) *
              orbitalPeriod[planet]!)
          .toStringAsFixed(
        2,
      ));
}
