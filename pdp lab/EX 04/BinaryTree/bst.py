from BinaryTree.binarytree import BinaryTree
from BinaryTree.node import Node

class BinarySearchTree(BinaryTree):
    def create_tree(self, iterable):
        for item in iterable:
            self.insert(item)

    def insert(self, data):
        self.root = self._insert_recursively(self.root, data)

    def _insert_recursively(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self._insert_recursively(node.left, data)
        elif data > node.data:
            node.right = self._insert_recursively(node.right, data)
        return node

    def traverse(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.data)
            self._inorder_traversal(node.right, result)
