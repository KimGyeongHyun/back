import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline


def slicing(start, end, w):
    # print("input", start, end)

    if start > end:
        return

    if start == end:
        pre_order[start] = in_order[start]
        return

    if post_order[end] == in_order[end + w]:
        pre_order[start] = post_order[end]
        slicing(start, end - 1, w)
        return

    root = post_order[end]

    root_idx = -1

    for idx in range(start, end):
        if in_order[idx + w] == root:
            root_idx = idx
            break

    pre_order[start] = root
    if root_idx == -1:
        slicing(start, end - 1, w + 1)
    else:
        slicing(start, root_idx - 1, w)
        slicing(root_idx, end - 1, w + 1)
    return


if __name__ == "__main__":
    n = int(input())

    in_order = list(map(int, input().split()))
    post_order = list(map(int, input().split()))
    pre_order = [0 for _ in range(n)]

    slicing(0, n - 1, 0)
    print(*pre_order)
