class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.parent = None


class BinarySearchTree:

    def search(self, root, key):
        if root is None or root.value == key:
            return root

        if root.value < key:
            return self.search(root.right, key)

        return self.search(root.left, key)

    def insert(self, root, node):
        if root is None:
            root = node
        else:
            if root.value < node.value:
                if root.right is None:
                    root.right = node
                    node.parent = root
                else:
                    self.insert(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                    node.parent = root
                else:
                    self.insert(root.left, node)

    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.value)
            self.in_order(root.right)

    def pre_order(self, root):
        if root:
            print(root.value)
            self.pre_order(root.left)
            self.pre_order(root.right)

    def post_order(self, root):
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.value)

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def max_value_node(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    def delete_node(self, root, val):
        if root is None:
            return root

        if val < root.value:
            root.left = self.delete_node(root.left, val)

        elif val > root.value:
            root.right = self.delete_node(root.right, val)

        else:
            if root.left is None:
                temp = root.right
                temp.parent = root.parent
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                temp.parent = root.parent
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete_node(root.right, temp.value)

        return root


if __name__ == "__main__":
    x = BinarySearchTree()
    root = Node(10)
    x.insert(root, Node(7))
    x.insert(root, Node(12))
    x.insert(root, Node(5))
    x.insert(root, Node(18))
    x.insert(root, Node(13))
    x.in_order(root)
    print()
    x.delete_node(root, 12)
    x.in_order(root)
