import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def set_tree(start, end, tree_idx):

    if end < start:
        return 0

    if start == end:
        tree[tree_idx] = l[start]
        return tree[tree_idx]

    mid = (start + end) // 2
    left = set_tree(start, mid, tree_idx*2)
    right = set_tree(mid+1, end, tree_idx*2+1)
    tree[tree_idx] = left + right
    return tree[tree_idx]


def get_sum(start, end, left, right, tree_idx):
    # print(start, end, left, right)

    if end < left or start > right:
        return 0

    if left <= start and end <= right:
        return tree[tree_idx]

    mid = (start + end) // 2
    left_sum = get_sum(start, mid, left, right, tree_idx*2)
    right_sum = get_sum(mid+1, end, left, right, tree_idx*2+1)
    return left_sum + right_sum


def update_tree(start, end, idx, dif, tree_idx):

    if idx < start or end < idx or end < start:
        return

    tree[tree_idx] += dif

    if start == end:
        return

    mid = (start + end) // 2
    update_tree(start, mid, idx, dif, tree_idx*2)
    update_tree(mid+1, end, idx, dif, tree_idx*2+1)


if __name__ == "__main__":
    n, k, m = map(int, input().split())
    tree = [0 for _ in range(4*n)]
    l = []
    for _ in range(n):
        l.append(int(input()))

    set_tree(0, n - 1, 1)

    for _ in range(m+k):
        t = list(map(int, input().split()))
        if t[0] == 1:
            dif = t[2] - l[t[1]-1]
            update_tree(0, n-1, t[1]-1, dif, 1)
            l[t[1]-1] = t[2]
        elif t[0] == 2:
            print(get_sum(0, n-1, t[1]-1, t[2]-1, 1))
