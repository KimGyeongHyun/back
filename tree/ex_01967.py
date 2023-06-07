import sys
sys.setrecursionlimit(10**6)    # 최대 recursion 수 확장

# 0) 정리
#   트리의 지름을 구하는 문제

#   트리를 직접 구상할 수도 있지만
#   극단 적인 경우 삽입, 삭제 연산이 시간복잡도 N 을 가지므로
#   초당 2천만번 계산하는 Python 3 특성상 N 이 10,000 이라면 1억번 연산이 필요하므로
#   시간 초과가 발생할 수 있다

#   특정 노드 기준 부분 트리에서 본인을 포함한 최대 지름을 알 수 있다면
#   위의 계산을 모든 노드에 적용하여 그 중 가장 큰 값을 구하면 해당 값이 트리의 최대 지름이 된다
#   위의 계산을 하기 위해선 트리의 말단 노드부터 시작하여 루트 노드까지 계산해야 한다

#   부모 노드 부분 트리중 본인 노드를 포함하는 최대 지름 구하기
#   1. '자식 노드 부분 트리 본인 포함 최대 지름' + '해당 자식 까지의 weight' 를 모은다
#   2. 위의 데이터중 제일 큰 2개(1개면 1개만 적용)의 값을 합산한 것이 부모 노드 부분 트리 본인 포함 최대 지름이다
#   (부분 트리의 루트 노드를 포함하는 최대 지름은 '자식 노드 최대 지름' + 'weight' 중 제일 큰 2개가 연결 된 형태)

# 1) 부모 노드 번호가 작은 것이 먼저 입력되고, 자식 노드 번호가 작은 것이 나중에 입력되므로,
#   부모 노드가 자식 노드보다 무조건 크다고 가정하고 풀었다 (dfs)
#   그에 따라 입력 데이터에 자식 노드가 부모 노드보다 큰 케이스가 없다고 가정,
#   입력 데이터를 뒤집어서 트리의 끝단부터 최대 지름을 갱신하면서 루트 노드까지 올라오게 구성
#   하지만 자식 노드가 부모 노드보다 클 때가 있으므로 오답처리 되었다

# 2) dfs 의 divide and conquer 속성을 활용하여 트리의 말단부터 접근
#   그래프를 활용
#   트리의 끝단부터 최대 지름을 갱신하면서 루트 노드까지 올라오게 구성

total_big = 0   # 트리 최대 지름


def set_total_big(input_value):
    """인풋 값이 트리 최대 지름보다 크다면 트리 최대 지름 갱신"""

    global total_big

    if total_big < input_value:
        total_big = input_value


def dfs(input_idx):
    """
    divide and conquer 방법으로 트리 말단부터 접근 \n
    모든 노드에 대해 최대 지름을 계산, 갱신
    """

    # 자식이 없을 경우 최대 지름 0
    if not g[input_idx]:
        return 0

    # 해당 노드 부분 트리 본인 노드 포함 최대 지름 계산, 갱신
    l = []
    for child, w in g[input_idx]:
        l.append(dfs(child) + w)

    l.sort()
    if len(l) >= 2:
        set_total_big(l[len(l)-1] + l[len(l)-2])
    else:
        set_total_big(l[0])
    return max(l)


if __name__ == "__main__":
    n = int(sys.stdin.readline())   # 노드 갯수
    g = [[] for _ in range(n+1)]    # 그래프

    # 그래프 갱신
    for _ in range(n-1):
        parent, child, w = map(int, sys.stdin.readline().split())
        g[parent].append((child, w))

    dfs(1)

    print(total_big)
    

