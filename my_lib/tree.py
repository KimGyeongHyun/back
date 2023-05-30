from sys import stdin

# 임시 파일임


class BinaryNode:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def return_data(self):
        return self.data

    def add_left_child(self, input_node):
        self.left_child = input_node

    def del_left_child(self):
        self.left_child = None

    def add_right_child(self, input_node):
        self.right_child = input_node

    def del_right_child(self):
        self.right_child = None


class Tree:

    def __init__(self):
        self.root = None

    def select_node(self, data, input_node):
        if data == input_node.return_data():
            return input_node
        if input_node.left_child is not None:
            t = self.select_node(data, input_node.left_child)
            if t is not None:
                return t
        if input_node.right_child is not None:
            t = self.select_node(data, input_node.right_child)
            if t is not None:
                return t

    def add_node(self, sel_data, left_data, right_data):

        if self.root is None:
            self.root = BinaryNode(sel_data)
            if left_data is not None:
                self.root.add_left_child(BinaryNode(left_data))
            if right_data is not None:
                self.root.add_right_child(BinaryNode(right_data))
            return

        sel_node = self.select_node(sel_data, self.root)
        if left_data is not None:
            sel_node.add_left_child(BinaryNode(left_data))
        if right_data is not None:
            sel_node.add_right_child(BinaryNode(right_data))

    def pre_order(self, input_node):
        print(input_node.return_data(), end='')
        if input_node.left_child is not None:
            self.pre_order(input_node.left_child)
        if input_node.right_child is not None:
            self.pre_order(input_node.right_child)

    def in_order(self, input_node):
        if input_node.left_child is not None:
            self.in_order(input_node.left_child)
        print(input_node.return_data(), end='')
        if input_node.right_child is not None:
            self.in_order(input_node.right_child)

    def post_order(self, input_node):
        if input_node.left_child is not None:
            self.post_order(input_node.left_child)
        if input_node.right_child is not None:
            self.post_order(input_node.right_child)
        print(input_node.return_data(), end='')


if __name__ == "__main__":
    n = int(stdin.readline())
    binary_tree = Tree()
    for _ in range(n):
        f, s, t = stdin.readline().split()
        if s == ".":
            s = None
        if t == ".":
            t = None

        binary_tree.add_node(f, s, t)

    binary_tree.pre_order(binary_tree.root)
    print()
    binary_tree.in_order(binary_tree.root)
    print()
    binary_tree.post_order(binary_tree.root)
    print()
