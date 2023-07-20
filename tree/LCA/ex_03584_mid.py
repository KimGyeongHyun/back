from sys import stdin

# 두 노드에서 루트 노드까지의 조상을 각 리스트로 나열할 수 있음
# 다만 해당 리스트에서 최대한 빨리 공통조상을 찾아야 함
# 시간복잡도 제한은 Nlog(N)

# 끝에서부터 루트 노드이므로 두 리스트를 뒤에서부터 각 리스트 요소 값 비교
# 탐색 중 리스트가 끝났거나 두 값이 다를 경우 그 전 값을 리턴
# (루트 노드 부터 값이 같을 때까지 탐색)


def get_near_parent(input_a, input_b):
    """가장 가까운 공통 조상 리턴"""

    l1, l2 = [], []     # 각 노드 조상 리스트

    # 조상 리스트 구성
    d = input_a
    while True:
        l1.append(d)
        if not g[d]:
            break
        d = g[d]

    d = input_b
    while True:
        l2.append(d)
        if not g[d]:
            break
        d = g[d]

    # 리스트 마지막부터 요소부터 비교
    i = 0
    while True:
        # 탐색 중 리스트가 끝났거나 두 값이 다를 경우 그 전 값을 리턴
        if len(l1) <= i+1 or len(l2) <= i+1 or l1[-1-i-1] != l2[-1-i-1]:
            return l1[-1-i]
        i += 1


if __name__ == "__main__":

    t = int(stdin.readline())

    for _ in range(t):
        n = int(stdin.readline())
        g = [0 for _ in range(n+1)]     # 그래프
        for _ in range(n-1):
            parent, child = map(int, stdin.readline().split())
            g[child] = parent   # 자식 -> 부모

        a, b = map(int, stdin.readline().split())
        print(get_near_parent(a, b))
