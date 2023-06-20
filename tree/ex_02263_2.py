import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# pre, in, post order 의 순회 정리
# pre order : 부모, 왼쪽 자식, 오른쪽 자식
# in order : 왼쪽 자식, 부모, 오른쪽 자식
# post order : 왼쪽 자식, 오른쪽 자식, 부모

# 특정 노드를 루트 노드로 가지는 부분 트리가 존재한다면
# pre, in, post order 배열은 각 order 안의 부분 트리의 위치만 다를 뿐, 해당 부분 트리의 노드들이 붙어있는 구조를 가지고 있다
# 즉 각 order 배열을 인덱싱하여 부분 트리를 뽑아낼 수 있다
# ex) pre-order 1 / 2 4 5 / 3 6 7
#    in-order 4 2 5 / 1 / 6 3 7
#    post-order 4 5 2 / 6 7 3 / 1
#    2 4 5 를 가지는 부분 트리, 3 6 7 을 가지는 부분 트리는 위치만 다를 뿐 pre, in, post order 에 모두 붙어있는 상태로 존재

# 인덱싱 된 post order 배열의 마지막 노드는 해당 부분 트리의 루트 노드이다
# 인덱싱 된 in order 의 루트 노드는 자식 노드의 부분 트리 사이에 위치한다
# post order 에서 가져온 루트 노드를 in order 에서 찾으면 왼쪽 부분 트리 / 루트 노드 / 오른쪽 부분 트리 의 관계를 찾을 수 있다
# ex) in-order 4 2 5 / 1 / 6 3 7
#   post-order 4 5 2 / 6 7 3 / 1
#   post order 의 마지막 노드는 1번 노드이며 이는 루트 노드
#   in order 에서 1번 노드 기준 양 옆은 각각 왼쪽 자식, 오른쪽 자식의 부분 트리 (4 2 5 / 6 3 7)

# 1번 풀이)    http://boj.kr/2795194b0dd94c2584d1a9f849ec8c2b
#   post order, in order 에서 부분 트리를 가져와 왼쪽 부분 트리 / 루트 노드 / 오른쪽 부분 트리의 관계를 찾고,
#   이를 다시 pre order 로 정렬하여 배열 형식으로 반환하는 재귀 함수 사용
# 왼쪽 부분 트리 / 루트 노드 / 오른쪽 부분 트리 의 관계를 찾을 때
# 오른쪽 부분 트리는 post order 기준 in order 에서 오른쪽으로 한 칸 밀린다
# ex) in-order 4 2 5 / 1 / 6 3 7
#   post-order 4 5 2 / 6 7 3 / 1
#   3 6 7 노드를 가지는 부분 트리는 1번 노드 때문에 post order 기준 in order 에서 뒤로 한 칸 밀린다
# 위의 성질을 이용하여 divide and conquer 방식을 사용하여 부분 트리가 노드 하나만 가지고 있을 때는 해당 노드를 반환하고
# 2개 이상인 경우 pre order 순서로 배열을 재구성하여 반환하는 방식 사용

# 1번 풀이 문제점
# 노드 10만개, 오른쪽 자식 밖에 없는 트리에선 부분 트리의 배열이 10만-1, 10만-2, 10만-3 ... 로 재구성되어 반환된다 (메모리 복잡도 N**2)

# 해당 풀이)
#   배열을 반환하는 대신 post order, in order 에서 찾은 부분 트리의 루트 노드를 pre order 배열에 직접 넣는 방법
# pre order 도 post order, in order 의 관계와 마찬가지로 post order 기준으로 부분 트리가 뒤로 밀린 상태로 존재
# ex) pre-order 1 / 2 4 5 / 3 6 7
#   post-order 4 5 2 / 6 7 3 / 1
#   루트 노드인 1번 노드를 기준으로 pre order 의 부분 트리들이 post order 기준 pre order 에서 모두 뒤로 한 칸씩 밀린다
# 즉, post order, in order 에서 왼쪽 부분 트리 / 루트 노드 / 오른쪽 부분 트리 관계를 찾고
# 해당 부분 트리가 post order 에서 얼마나 밀렸는지 dfs 매개변수로 전달하면 된다


def slicing(start, end, in_w, pre_w):
    """
    post order 를 기준으로 인덱싱하여 루트 노드를 찾고 in order 와 비교하여 트리 관계를 찾아 post order 에 하나씩 대입\n
    :param start: post order 기준 부분 트리의 시작 인덱스
    :param end: post order 기준 부분 트리의 마지막 인덱스
    :param in_w: post order 기준 in order 에서 부분 트리가 밀린 횟수
    :param pre_w: post order 기준 pre order 에서 부분 트리가 밀린 횟수
    :return: None
    """

    # 예외처리
    if start > end or start < 0 or end < 0:
        return

    # post order 의 마지막 노드는 루트 노드
    root = post_order[end]
    # 해당 루트 노드를 pre order 배열에 넣는다
    # pre_w: post order 기준 pre order 에서 부분 트리가 밀린 횟수
    pre_order[start+pre_w] = root

    # 부분 트리가 노드 1개밖에 없다면 종료
    if start == end:
        return

    # pre order 와 in order 의 끝 노드가 같다면, 해당 부분 트리는 오른쪽 자식이 없다
    if root == in_order[end + in_w]:
        # 왼쪽 자식을 재귀 호출할 시 in order 부분 트리는 밀리지 않지만 pre order 부분 트리는 한 칸 밀리므로 pre_w 에 +1
        slicing(start, end - 1, in_w, pre_w + 1)
        return

    # pre order 의 끝 노드가 in order 의 시작 노드와 같다면, 해당 부분 트리는 왼쪽 자식이 없다
    if root == in_order[start + in_w]:
        # 오른쪽 자식을 재귀 호출할 시 in oder, pre order 부분 트리 모두 한 칸씩 밀리므로 in_w, pre_w 에 각각 +1
        slicing(start, end - 1, in_w + 1, pre_w + 1)
        return

    # in order 를 이용하여 트리 구조를 찾음
    root_idx = -1
    for idx in range(end-1, start, -1):
        if in_order[idx + in_w] == root:     # 루트 노드를 찾으면 해당 인덱스를 받고 탈출
            root_idx = idx
            break

    # 왼쪽 자식 부분 트리, 오른쪽 자식 부분 트리에 대해 재귀 호출
    slicing(start, root_idx - 1, in_w, pre_w + 1)
    slicing(root_idx, end - 1, in_w + 1, pre_w + 1)


if __name__ == "__main__":
    n = int(input())

    in_order = list(map(int, input().split()))
    post_order = list(map(int, input().split()))
    pre_order = [0 for _ in range(n)]

    slicing(0, n - 1, 0, 0)     # pre_order 구성
    print(" ".join(map(str, pre_order)))