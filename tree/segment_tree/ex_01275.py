import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


class SegmentTree:

    def __init__(self, input_l) -> None:
        self.l = input_l
        self.tree = [0 for _ in range(len(self.l) * 4)]
        self._set_tree(0, len(self.l) - 1, 1)

    def _set_tree(self, start, end, tree_idx):
        if start == end:
            self.tree[tree_idx] = self.l[start]
            return self.tree[tree_idx]
        mid = (start + end) // 2
        left = self._set_tree(start, mid, tree_idx * 2)
        right = self._set_tree(mid + 1, end, tree_idx * 2 + 1)
        self.tree[tree_idx] = left + right
        return self.tree[tree_idx]

    def get_sum(self, left, right, start, end, tree_idx):
        if left > end or right < start:
            return 0

        if left <= start and end <= right:
            return self.tree[tree_idx]

        mid = (start + end) // 2
        v_left = self.get_sum(left, right, start, mid, tree_idx * 2)
        v_right = self.get_sum(left, right, mid + 1, end, tree_idx * 2 + 1)
        return v_left + v_right

    def update(self, idx, dif, start, end, tree_idx):

        if idx < start or end < idx:
            return

        self.tree[tree_idx] += dif

        if start == end:
            return

        mid = (start + end) // 2
        self.update(idx, dif, start, mid, tree_idx * 2)
        self.update(idx, dif, mid + 1, end, tree_idx * 2 + 1)


if __name__ == "__main__":
    n, q = map(int, input().split())
    l = list(map(int, input().split()))
    seg = SegmentTree(l)
    for _ in range(q):
        x, y, a, b = map(int, input().split())
        if x <= y:
            print(seg.get_sum(x-1, y-1, 0, n-1, 1))
        else:
            print(seg.get_sum(y-1, x-1, 0, n-1, 1))
        seg.update(a-1, b-seg.l[a-1], 0, n-1, 1)
        seg.l[a-1] = b
