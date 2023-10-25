import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def find(n):

    if par[n] == n:
        return n
    par[n] = find(par[n])   # find 최적화 / 시간 초과 -> 2440ms
    return par[n]


def union(x, y):

    x = find(x)
    y = find(y)

    if x == y:
        return

    par[y] = x          # 부모 갱신
    num[x] += num[y]    # 해당 부모에 두 분리 집합의 노드 갯수를 합쳐서 갱신


if __name__ == "__main__":
    n = int(input())
    par = [i for i in range(10**6+1)]   # 부모
    num = [1 for i in range(10**6+1)]   # 분리 집합 노드 갯수
    for _ in range(n):
        l = list(input().split())
        if l[0] == "I":     # 합치기
            a, b = map(int, l[1:3])
            union(a, b)
        if l[0] == "Q":     # 조회
            a = int(l[1])
            print(num[find(a)])

