from sys import stdin


class Node:

    def __init__(self, data):
        self.data = data
        self.childs = []

    def return_data(self):
        return self.data

    def add_child(self, input_node):
        self.childs.append(input_node)

    def del_child(self, input_index):
        del self.childs[input_index]


class Tree:
    sum = 0

    def __init__(self):
        self.root = None

    def add_node(self, start_data, parent_data, input_node):

        if self.root is None:
            self.root = Node(start_data)
            return

        if input_node.return_data() == parent_data:
            if input_node.left_child is None:
                input_node.add_left_child(BinaryNode(start_data))
            else:
                input_node.add_right_child(BinaryNode(start_data))
        else:
            if input_node.left_child is not None:
                self.add_node(start_data, parent_data, input_node.left_child)
                if input_node.right_child is not None:
                    self.add_node(start_data, parent_data, input_node.right_child)

    def del_node(self, input_data, input_node):
        if input_data == 0:
            self.root = None
        if input_node.left_child is not None:
            if input_node.left_child.return_data() == input_data:
                input_node.left_child = None
                return
            else:
                self.del_node(input_data, input_node.left_child)
        if input_node.right_child is not None:
            if input_node.right_child.return_data() == input_data:
                input_node.right_child = None
                return
            else:
                self.del_node(input_data, input_node.right_child)

    def get_leaf_count(self, input_node):

        if self.root is None:
            return 0

        if input_node.left_child is None and input_node.right_child is None:
            self.sum += 1
            return

        if input_node.left_child is not None:
            self.get_leaf_count(input_node.left_child)
        if input_node.right_child is not None:
            self.get_leaf_count(input_node.right_child)

    def pre_order(self, input_node):
        print(input_node.return_data(), end=' ')
        if input_node.left_child is not None:
            self.pre_order(input_node.left_child)
        if input_node.right_child is not None:
            self.pre_order(input_node.right_child)


    #
    # def in_order(self, input_node):
    #     if input_node.left_child is not None:
    #         self.in_order(input_node.left_child)
    #     print(input_node.return_data(), end='')
    #     if input_node.right_child is not None:
    #         self.in_order(input_node.right_child)
    #
    # def post_order(self, input_node):
    #     if input_node.left_child is not None:
    #         self.post_order(input_node.left_child)
    #     if input_node.right_child is not None:
    #         self.post_order(input_node.right_child)
    #     print(input_node.return_data(), end='')


if __name__ == "__main__":
    n = int(stdin.readline())
    l = list(map(int, stdin.readline().split()))
    tree = Tree()
    for i in range(n):
        tree.add_node(i, l[i], tree.root)
    del_data = int(stdin.readline())

    tree.sum = 0
    # print(tree.sum)
    tree.del_node(del_data, tree.root)
    tree.sum = 0
    tree.get_leaf_count(tree.root)
    print(tree.sum)


