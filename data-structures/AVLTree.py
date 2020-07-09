from BinarySearchTree import BinarySearchTree, Node


class TreeNode(Node):
    def __init__(self, val):
        super().__init__(val)
        self.height = 1


class AVLTree(BinarySearchTree):
    def __init__(self):
        super().__init__()

    def left_rotate(self, node):
        node2 = node.right
        T = node2.left

        node2.left = node
        node.right = T

        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))
        node2.height = 1 + max(self.get_height(node2.left),
                               self.get_height(node2.right))

        return node2

    def right_rotate(self, node):
        node2 = node.left
        T = node2.right

        node2.right = node
        node.left = T

        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))
        node2.height = 1 + max(self.get_height(node2.left),
                               self.get_height(node2.right))

        return node2

    def get_height(self, root):
        if not root:
            return 0

        return root.height

    def get_balance(self, root):
        if not root:
            return 0

        return self.get_height(root.left) - self.get_height(root.right)

    def insert(self, root, value):
        if not root:
            return TreeNode(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)

        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)

        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete_node(self, root, value):
        if not root:
            return root

        elif value < root.value:
            root.left = self.delete_node(root.left, value)

        elif value > root.value:
            root.right = self.delete_node(root.right, value)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete_node(root.right, temp.value)

        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root


if __name__ == "__main__":
    x = AVLTree()
    root = None
    root = x.insert(root, 7)
    root = x.insert(root, 12)
    root = x.insert(root, 5)
    root = x.insert(root, 18)
    root = x.insert(root, 13)
    x.in_order(root)
    print()
    x.delete_node(root, 12)
    x.in_order(root)
