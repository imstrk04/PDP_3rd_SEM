class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._push_left_chain(root)

    def _push_left_chain(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration

        current_node = self.stack.pop()
        self._push_left_chain(current_node.right)
        return current_node.value


# Function to insert a value into the BST
def insert_into_bst(root, value):
    if not root:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_into_bst(root.left, value)
    else:
        root.right = insert_into_bst(root.right, value)
    return root


# Function to perform inorder traversal and collect values
def inorder_traversal_values(root):
    if not root:
        return []
    return inorder_traversal_values(root.left) + [root.value] + inorder_traversal_values(root.right)


# Test cases
def test_bst_iterator():
    # Construct a BST
    bst_root = None
    values_to_insert = [5, 3, 7, 2, 4, 6, 8]
    for value in values_to_insert:
        bst_root = insert_into_bst(bst_root, value)

    # Initialize the iterator
    iterator = BSTIterator(bst_root)

    # Check that the iterator correctly iterates over values in ascending order
    expected_values = inorder_traversal_values(bst_root)
    for expected_value in expected_values:
        assert next(iterator) == expected_value

    # Ensure that trying to iterate beyond the end raises StopIteration
    try:
        next(iterator)
        assert False  # Should not reach here
    except StopIteration:
        pass

if __name__ == "__main__":
    test_bst_iterator()
    print("All test cases passed.")
