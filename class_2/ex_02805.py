from sys import stdin


def get_sum_tree(input_list, height):
    tree_sum = 0
    for tree in input_list:
        if height < tree:
            tree_sum += height - tree

    return tree_sum


if __name__ == "__main__":
    n, m = map(int, stdin.readline().split())
    l = list(map(int, stdin.readline().split()))

    start = 0
    end = max(l)

    while True:
        mid = (start + end) // 2

        get_tree = get_sum_tree(l, mid)

        if get_tree