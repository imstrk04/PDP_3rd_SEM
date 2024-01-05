class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
        self.parent = None

class BinarySearchTree:
    def createNode(self,data):
        return Node(data)

    def insert(self,node,value):
        if node is None:
            return self.createNode(value)

        if value < node.data:
            node.left = self.insert(node.left, value)
            node.left.parent = node

        if value > node.data:
            node.right = self.insert(node.right, value)
            node.right.parent = node

        return node

    def traverse_inorder(self, root):
        if root is not None:
            self.traverse_inorder(root.left)
            print(root.data, end = " ")
            self.traverse_inorder(root.right)

    def traverse_preorder(self, root):
        if root is not None:
            print(root.data, end = " ")
            self.traverse_preorder(root.left)
            self.traverse_preorder(root.right)

    def traverse_postorder(self, root):
        if root is not None:
            self.traverse_postorder(root.left)
            self.traverse_postorder(root.right)
            print(root.data, end = " ")

    def find_min(self, root):
        if root.left is None:
            return root.data
        return self.find_min(root.left)

    def find_max(self,root):
        if root.right is None:
            return root.data
        return self.find_max(root.right)

    def level_order(self,root):
        q = []
        q.append(root)
        while (len(q) != 0):
            root = q.pop(0)
            print(root.data, end = " ")
            if root.left is not None:
                q.append(root.left)
            if root.right is not None:
                q.append(root.right)

    def find_ele(self,root,ele):
        if root is None:
            return None

        if root.data == ele:
            return root

        left_result = self.find_ele(root.left, ele)
        if left_result is not None:
            return left_result

        right_result = self.find_ele(root.right, ele)
        if right_result is not None:
            return right_result

    def delete_value(self,root,ele):
        return self.delete_node(self.find_ele(root,ele))

    def delete_node(self,node):

        def min_value_node(n):
            current = n
            while current.left is not None:
                current = current.left
            return current

        def num_children(n):
            num_children = 0
            if n.left is not None:
                num_children += 1
            if n.right is not None:
                num_children += 1
            return num_children

        node_parent = node.parent

        node_children = num_children(node)

        if node_children == 0:
            if node_parent.left == node:
                node_parent.left = None
            if node_parent.right == node:
                node_parent.right = None

        if node_children == 1:
            if node.left is not None:
                child = node.left
            if node.right is not None:
                child = node.right

            if node_parent.left == node:
                node_parent.left = child
            else:
                node_parent.right = child
            child.parent = node_parent

        if node_children == 2:
            successor = min_value_node(node.right)

            node.data = successor.data

            self.delete_node(successor)

tree = BinarySearchTree()
root = tree.createNode(10)
tree.insert(root, 5)
tree.insert(root, 15)
tree.insert(root, 12)
tree.insert(root, 20)
tree.insert(root, 8)
tree.insert(root, 2)
tree.insert(root,1)
print("Inorder: ", end = "")
tree.traverse_inorder(root)
print()
print("Preorder: ", end = "")
tree.traverse_preorder(root)
print()
print("Postorder: ", end = "")
tree.traverse_postorder(root)
print()
minimum = tree.find_min(root)
print("Minimum element:", minimum)
maximum = tree.find_max(root)
print("Maximum Element:", maximum)
print("Deleting node(10):")
tree.delete_value(root,10)
tree.traverse_inorder(root)
print()
print("Deleting node(2):")
tree.delete_value(root,2)
tree.traverse_inorder(root)
print()
print("Deleting node(1):")
tree.delete_value(root,1)
tree.traverse_inorder(root)
print()
        