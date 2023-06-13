import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline


def slicing(start, end, w):

    print("input", start, end)

    if start > end:
        return []

    if start == end:
        return [post_order[start]]

    if post_order[end] == in_order[end+w]:
        return [post_order[end]] + slicing(start, end-1, w)

    root = post_order[end]

    root_idx = -1

    for idx in range(start, end):
        if in_order[idx+w] == root:
            root_idx = idx
            break

    if root_idx == -1:
        return [root] + slicing(start, end-1, w+1)
    else:
        return [root] + slicing(start, root_idx-1, w) + slicing(root_idx, end-1, w+1)


if __name__ == "__main__":

    n = int(input())

    in_order = list(map(int, input().split()))
    post_order = list(map(int, input().split()))

    print(*slicing(0, n-1, 0))
