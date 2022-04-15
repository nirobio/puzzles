DateTime add(
  final DateTime birthDate,
) {
  return birthDate.add(
    const Duration(
      seconds: 1000000000,
    ),
  );
}
