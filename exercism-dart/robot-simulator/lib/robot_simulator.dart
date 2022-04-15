import 'orientation.dart';
import 'position.dart';

class Robot {
  Robot(
    this.position,
    this.orientation,
  );

  Position position;
  Orientation orientation;

  void move(
    String movements,
  ) {
    for (final m in movements.split(
      '',
    )) {
      switch (m) {
        case 'A':
          switch (orientation) {
            case Orientation.west:
              position = Position(
                position.x - 1,
                position.y,
              );
              break;
            case Orientation.east:
              position = Position(
                position.x + 1,
                position.y,
              );
              break;
            case Orientation.north:
              position = Position(
                position.x,
                position.y + 1,
              );
              break;
            case Orientation.south:
              position = Position(
                position.x,
                position.y - 1,
              );
              break;
          }
          break;
        case 'L':
          switch (orientation) {
            case Orientation.west:
              orientation = Orientation.south;
              break;
            case Orientation.east:
              orientation = Orientation.north;
              break;
            case Orientation.north:
              orientation = Orientation.west;
              break;
            case Orientation.south:
              orientation = Orientation.east;
              break;
          }
          break;
        case 'R':
          switch (orientation) {
            case Orientation.west:
              orientation = Orientation.north;
              break;
            case Orientation.east:
              orientation = Orientation.south;
              break;
            case Orientation.north:
              orientation = Orientation.east;
              break;
            case Orientation.south:
              orientation = Orientation.west;
              break;
          }
          break;
      }
    }
  }
}
