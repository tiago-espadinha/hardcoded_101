/**
 * Iterator pattern implementation for a Tree structure
 * ES2022 Node.js environment
 */

class TreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

class BinaryTree {
  #root;

  constructor(root = null) {
    this.#root = root;
  }

  get root() { return this.#root; }

  /**
   * Custom Symbol.iterator for in-order traversal.
   * Uses a generator to yield values.
   */
  *[Symbol.iterator]() {
    yield* this._traverseInOrder(this.#root);
  }

  *_traverseInOrder(node) {
    if (node) {
      yield* this._traverseInOrder(node.left);
      yield node.value;
      yield* this._traverseInOrder(node.right);
    }
  }
}

// Client Code
const root = new TreeNode(10);
root.left = new TreeNode(5);
root.right = new TreeNode(15);
root.left.left = new TreeNode(3);
root.left.right = new TreeNode(7);
root.right.left = new TreeNode(12);
root.right.right = new TreeNode(20);

const tree = new BinaryTree(root);

console.log("In-order traversal of the tree:");
for (const value of tree) {
  console.log(value);
}

// Spreading values into an array
const values = [...tree];
console.log("Values as array:", values);
