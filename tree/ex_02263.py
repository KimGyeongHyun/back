import sys
sys.setrecursionlimit(int(10e6))
input = sys.stdin.readline


def slicing(start, end, w):
    # post order 를 기준으로 인덱싱 수행
    # post 의 마지막 노드는 부분 트리 기준 루트 노드이며 이를 in order 에서 찾음
    # in order 에서 찾은 루트 노드를 기준으로 부분 트리를 나눔 (왼쪽 / 루트 / 오른쪽)
    # pre order 순서에 맞게 재귀 함수 수행
    # w 는 오른쪽 자식을 재귀 탐색할 경우 post 와 in 간에 한 칸씩 밀리는 것을 방지
    # 오른쪽 자식으로 재귀 실행할 때마다 w+1 하여 post 와 in 의 부분 트리를 동기화

    # print("input", start, end)

    if start > end:
        return []

    if start < 0 or end < 0:
        return []

    # 루트 노드 값
    root = post_order[end]

    # 루트 노드 밖에 없을 경우 루트 노드 리턴
    if start == end:
        return [root]

    # post 와 in 의 오른쪽 노드가 같다면 오른쪽 자식이 없다는 의미이므로
    # 왼쪽 / 루트 관계 리턴
    if root == in_order[end+w]:
        return [root] + slicing(start, end-1, w)

    # 루트 노드가 in 의 맨 왼쪽 노드와 같다면 왼쪽 자식이 없다는 의미이므로
    # 루트 / 오른쪽 관계 리턴
    if root == in_order[start+w]:
        return [root] + slicing(start, end-1, w+1)

    # 루트 노드 인덱스를 찾기 위한 변수
    root_idx = -1

    # in order 를 탐색하여 루트 노드를 찾음
    for idx in range(end-1, start, -1):
        if in_order[idx+w] == root:     # 루트 노드를 찾으면 해당 인덱스를 받고 탈출
            root_idx = idx
            break

    # 왼쪽 / 루트 / 오른쪽 관계 리턴
    return [root] + slicing(start, root_idx-1, w) + slicing(root_idx, end-1, w+1)


if __name__ == "__main__":

    n = int(input())

    in_order = list(map(int, input().split()))
    post_order = list(map(int, input().split()))

    print(*slicing(0, n-1, 0))
