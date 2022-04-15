class Node {
  Node(
    String this.data,
  );

  final String data;
  Node? left;
  Node? right;
}

class BinarySearchTree {
  BinarySearchTree(String rootData) : root = Node(rootData);
  final Node root;

  void _insert(String data, Node node) {
    if (data.compareTo(node.data) <= 0) {
      if (node.left == null) {
        node.left = Node(
          data,
        );
        return;
      } else {
        _insert(data, node.left!);
      }
    } else {
      if (node.right == null) {
        node.right = Node(
          data,
        );
        return;
      } else {
        _insert(data, node.right!);
      }
    }
  }

  void insert(String data) {
    _insert(
      data,
      root,
    );
  }

  Iterable<String?> _traverse(Node? node) sync* {
    if (node == null) {
      yield null;
    } else {
      _traverse(
        node.left,
      );
      yield node.data;

      _traverse(
        node.right,
      );
    }
  }

  List<String> get sortedData => _traverse(
        root,
      )
          .where(
            (
              e,
            ) =>
                e != null,
          )
          .toList() as List<String>;
}
