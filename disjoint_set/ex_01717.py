import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def find(x):
    par = parent[x]
    if par == x:
        return x
    parent[x] = find(par)
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    # rank a > rank b
    if rank[x] > rank[y]:
        a, b = x, y
    else:
        a, b = y, x

    # b 가 깊이가 작은 트리
    # 트리끼리 붙일 때는 깊이가 작은 트리를
    # 트리가 긴 트리의 루트에 붙이는 게
    # 깊이가 안 깊어지는 방향임
    # 따라서 b 트리를 a 의 루트에 붙이는 작업을 함
    # a, b 가 깊이가 같다면 b+1 의 트리 구조 나옴
    # 아니라면 a 트리의 깊이를 그대로 가져감
    if rank[x] == rank[y]:
        rank[b] += 1

    parent[b] = a


if __name__ == "__main__":
    n, m = map(int, input().split())
    parent = [i for i in range(n+1)]
    rank = [1 for i in range(n+1)]
    for _ in range(m):
        f, a, b = map(int, input().split())

        if f == 0:
            union(a, b)
        elif f == 1:
            if find(a) == find(b):
                print("YES")
            else:
                print("NO")
        elif f == 2:
            print(find(a), find(b))

        print(*parent)
        print(*rank)
        print()