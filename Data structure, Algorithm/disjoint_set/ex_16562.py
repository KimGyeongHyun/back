import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def find(n):
    """분리 집합 루트 노드 찾는 함수"""

    if par[n] == n:
        return n

    # find 최적화 5248ms -> 68ms
    # ==============================
    par[n] = find(par[n])
    return par[n]
    # ==============================

    # return find(par[n])


def union(x, y):
    """
    분리 집합 두 노드 합치는 함수\n
    두 노드의 루트 노드의 가격을 비교하고 저렴한 가격을 합치는 루트 노드에 갱신\n
    """
    # 합쳐진 후 최종 루트 노드를 두 루트 노드 중 저렴한 가격을 갱신하는 방법을 사용하면
    # 전체 연결 요소 중 제일 저렴한 값을 루트 노드에 갱신할 수 있다

    x = find(x)
    y = find(y)

    if x == y:
        return

    # union 최적화 5248ms -> 5740ms
    # 트리의 편향을 막기 위해 트리의 깊이를 확인하고 어떻게 트리를 붙일지 결정
    # 데이터에 편향 트리가 없었는지 오히려 실행 시간이 늘어난 것을 확인
    # ==============================
    if rank[x] < rank[y]:
        a, b = y, x
    else:
        a, b = x, y

    if rank[x] == rank[y]:
        rank[b] += 1

    ap = price[a]
    bp = price[b]
    # ==============================

    par[a] = b
    price[b] = min(ap, bp)


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    price = list(map(int, input().split()))     # 친구 가격
    par = [i for i in range(n)]     # 부모 노드
    rank = [1 for _ in range(n)]    # 트리 깊이
    for _ in range(m):
        a, b = map(int, input().split())
        union(a-1, b-1)

    visit = [False for _ in range(n)]   # 해당 분리 집합 조회 여부
    min_sum = 0     # 모든 친구비 합친 가격
    for i in range(n):  # 모든 노드 순회
        idx = find(i)   # 분리 집합 루트 노드 조회
        if visit[idx]:  # 해당 분리 집합 조회했으면 넘어감
            continue
        min_sum += price[idx]   # 해당 분리 집합의 최소 친구 가격을 친구비에 더함
        visit[idx] = True       # 해당 분리 집합 조회

    if min_sum <= k:
        print(min_sum)
    else:
        print("Oh no")