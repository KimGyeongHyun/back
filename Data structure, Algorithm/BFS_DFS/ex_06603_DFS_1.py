def dfs(v, depth):
    if depth == 6:
        print(*out)
        return

    for i in range(v, N):
        out.append(S[i])
        dfs(i + 1, depth + 1)
        out.pop()


while True:
    arr = list(map(int, input().split()))
    N = arr[0]
    S = arr[1:]
    out = []
    dfs(0, 0)
    if N == 0:
        exit()
    print()