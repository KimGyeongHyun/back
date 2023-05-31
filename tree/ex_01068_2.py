from sys import stdin


class Node:

    def __init__(self, input_data):
        self.data = input_data
        self.childs = []

    def add_child(self, input_node):
        self.childs.append(input_node)

    def del_child(self, input_index):
        del self.childs[input_index]

    def get_data(self):
        return self.data


class Tree:

    leaf_count = 0

    def __init__(self):
        self.root = None

    def add_node(self, start_data, parent_data, input_node):
        if self.root is None:
            self.root = Node(0)
            return

        if input_node.get_data() == parent_data:
            input_node.add_child(Node(start_data))

        for child in input_node.childs:
            self.add_node(start_data, parent_data, child)

    def del_node(self, del_data, input_node):

        # print("del_node")
        # print("input_node:", input_node.get_data())

        if del_data == 0:
            self.root = None
            return

        for i in range(len(input_node.childs)):
            if input_node.childs[i].get_data() == del_data:
                input_node.del_child(i)
                return

        for child in input_node.childs:
            self.del_node(del_data, child)

    def count_leaf(self, input_node):
        if input_node is None:
            self.leaf_count = 0
            return

        if len(input_node.childs) == 0:
            self.leaf_count += 1
            return

        for child in input_node.childs:
            self.count_leaf(child)

    def pre_order(self, input_node):
        if input_node is None:
            return
        print(input_node.get_data(), end=' ')
        for child in input_node.childs:
            self.pre_order(child)


if __name__ == "__main__":
    n = int(stdin.readline())
    l = list(map(int, stdin.readline().split()))
    tree = Tree()
    g = [[] for _ in range(n+1)]
    for i in range(n):
        tree.add_node(i, l[i], tree.root)
    del_data = int(stdin.readline())

    tree.pre_order(tree.root)
    tree.count_leaf(tree.root)
    print()
    print(tree.leaf_count)
    print()

    tree.del_node(del_data, tree.root)
    tree.leaf_count = 0
    tree.pre_order(tree.root)
    print()
    tree.count_leaf(tree.root)
    print(tree.leaf_count)


