class RnaTranscription {
  String toRna(String dna) {
    if (dna.isEmpty) {
      return '';
    }

    final transcribed = StringBuffer();
    for (final n in dna.split(
      '',
    )) {
      switch (n) {
        case 'G':
          transcribed.write(
            'C',
          );
          break;
        case 'C':
          transcribed.write(
            'G',
          );
          break;
        case 'T':
          transcribed.write(
            'A',
          );
          break;
        case 'A':
          transcribed.write(
            'U',
          );
          break;
        default:
          throw Exception(
            'Invalid DNA letter.',
          );
      }
    }
    return transcribed.toString();
  }
}
