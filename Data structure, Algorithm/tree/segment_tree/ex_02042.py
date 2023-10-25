import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


class SegmentTree:

    def __init__(self, input_l) -> None:
        """수 리스트를 받고 세그먼트 트리로 초기화"""
        self.l = input_l
        self.tree = [0 for _ in range(len(self.l) * 4)]
        self._set_tree(0, len(self.l) - 1, 1)

    def _set_tree(self, start, end, tree_idx):
        """

        :param start: 수 리스트 시작 인덱스
        :param end: 수 리스트 끝 인덱스
        :param tree_idx: 트리에 삽입될 인덱스
        :return:
        """
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

        # 부등호가 들어가는 이유는 공백인 노드도 있기 때문
        # 데이터 범위가 늘어나면서 값을 찾기 때문에
        # 찾는 범위가 나올 때 리턴하게 되면
        # 불필요한 데이터 범위가 들어가지 않음
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
    n, m, k = map(int, input().split())
    l = []
    for _ in range(n):
        l.append(int(input()))

    seg = SegmentTree(l)
    for _ in range(m+k):
        a, b, c = map(int, input().split())
        if a == 1:
            seg.update(b-1, c-seg.l[b-1], 0, len(l)-1, 1)
            seg.l[b-1] = c
        elif a == 2:
            print(seg.get_sum(b-1, c-1, 0, len(l)-1, 1))