import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

# 노드는 우수 마을인지 아닌지 2가지의 상태를 가진다
# 자식 노드들이 '본인이 우수 마을인지 아닌지에 따라 본인을 포함한 부분트리에서 우수 마을 최대 사람 수'의 정보를 각각 가지고 있다면
# 부모 노드는 본인이 우수 마을인지 아닌지 2가지의 경우로 '본인을 포함한 부분트리의 우수 마을 최대 사람 수'를 알 수 있다
# 1. 본인이 우수 마을일 경우
#   자식 노드들은 우수 마을이 될 수 없다
#   따라서 우수 마을이 아닌 자식 노드들의 최대 사람 수를 적용시킨다
# 2. 본인이 우수 마을이 아닐 경우
#   자식 노드들은 우수 마을이거나 아닐 수 있다
#   최대 사람 수를 구해야 하므로 2개의 사람 수 중에서 큰 값을 적용시킨다

# 트리의 말단부터 최대 사람 수를 계산해야 하므로 dfs 의 divide and conquer 방식을 적용
# 트리의 말단부터 루트 노드까지 우수 마을 최대 사람 수를 계산한다
# 모든 계산을 마치면 루트 노드가 우수 마을인지 아닌지에 따라 우수 마을 최대 사람 수가 각각 나오게 된다


def get_tree(start, end):
    """간선으로부터 부모 -> 자식 의 방향성을 가진 트리 구성"""

    if visit[end]:
        return
    visit[end] = True
    g[start].append(end)

    for e_end in ig[end]:
        get_tree(end, e_end)


def set_most(input_node):
    """마을이 우수 마을인지 아닌지에 따라 본인을 포함하는 부분트리의 우수 마을 사람 최대 수를 반환"""

    # 본인이 우수 마을, 본인이 우수 마을이 아닐 때 우수 마을 최대 사람 수
    yes, no = l[input_node], 0

    # 자식 노드 순회
    for dest in g[input_node]:
        y, n = set_most(dest)   # 자식 노드 부분트리의 우수 마을 사람 최대 사람 수를 구함
        yes += n                # 본인이 우수 마을일 경우 자식 노드가 우수 마을이 아닐 경우만 적용한다
        no += max(y, n)         # 본인이 우수 마을이 아닐 경우 자식 노드 부분트리의 우수 마을 최대 사람 수를 적용한다

    return yes, no


if __name__ == "__main__":
    n = int(input())
    l = [0] + list(map(int, input().split()))
    ig = [[] for _ in range(n+1)]   # 방향성이 없는 그래프
    g = [[] for _ in range(n+1)]    # 트리
    visit = [False for _ in range(n+1)]

    for _ in range(n-1):
        a, b = map(int, input().split())
        ig[a].append(b)
        ig[b].append(a)

    get_tree(0, 1)  # 부모 -> 자식 의 방향성을 가진 트리 구성

    print(max(set_most(1)))     # 트리의 우수 마을 최대 사람 수 출력
