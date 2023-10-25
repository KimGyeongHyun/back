import sys
sys.setrecursionlimit(10**6)

# 자식이 없는 자식 노드를 가지고 있는 부모 노드가 있을 때
# 모든 자식 노드가 얼리 어답터인 것보다,
# 부모가 얼리 어답터, 자식 노드가 얼리 어답터가 아닌 것이 얼리 어답터가 적다
# 위의 방식으로 자식이 없는 말단 노드부터 위로 올라가면서 얼리 어답터를 갱신할 때
# 모든 자식 노드에 대해 얼리 어답터가 하나라도 없으면 부모 노드는 무조건 얼리 어답터 이어야 한다

# 위의 방식대로 자식 노드부터 탐색해야 하므로 dfs 를 이용한 divide and conquer 방식을 사용한다
# 얼리 어답터를 True 라고 표현하다면
# 1. 자식이 없는 모든 노드는 False 가 되어야 하고
# 2. 하나의 자식이라도 False 라면 부모 노드는 True 가 되어야 한다

count = 0   # 얼리 어답터 갯수


def dfs(input_idx):
    """
    모든 노드에 대해 얼리 어답터 여부를 결정하고 총 얼리 어답터 갯수를 갱신 \n
    divide and conquer 방식으로 트리의 말단 노드부터 루트 노드까지 순회
    """

    # 자식이 없으면 얼리 어답터가 아니다
    if not g[input_idx]:
        return False

    # 방문한 부모 노드를 방문 처리
    visit[input_idx] = True
    # 모든 자식 노드가 얼리 어답터인지 확인하는 flag 변수
    temp_flag = True

    # 모든 자식 노드 순회
    for idx in g[input_idx]:
        if visit[idx]:  # 부모 노드는 스킵
            continue
        # 자식 노드 중 하나라도 얼리 어답터가 아니라면 flag 는 False
        temp_flag &= dfs(idx)

    if not temp_flag:   # 하나의 자식이라도 얼리 어답터가 아니면 해당 노드는 얼리 어답터
        global count
        count += 1      # 얼리 어답터 갯수 갱신
        return True
    else:   # 모든 자식이 얼리 어답터라면 해당 노드는 얼리 어답터가 아님
        return False


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    g = [[] for _ in range(n+1)]
    for _ in range(n-1):
        d1, d2 = map(int, sys.stdin.readline().split())
        g[d1].append(d2)
        g[d2].append(d1)

    visit = [False for _ in range(n+1)]

    dfs(1)
    print(count)