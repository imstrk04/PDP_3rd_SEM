#BST
class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self._push_left_children(root)

    def _push_left_children(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def has_next(self):
        return bool(self.stack)

    def next(self):
        if not self.has_next():
            raise StopIteration("No more elements in BST")

        current_node = self.stack.pop()
        self._push_left_children(current_node.right)

        return current_node.value

def build_bst():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    return root

if __name__ == "__main__":

    bst_root = build_bst()

    bst_iterator = BSTIterator(bst_root)

    expected_result = [2,3,4,5,6,7,8,9]

    result = []
    while bst_iterator.has_next():
        result.append(bst_iterator.next())
    print(result)
    
