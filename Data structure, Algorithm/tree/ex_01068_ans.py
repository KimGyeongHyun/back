from sys import stdin


# 1. 입력된 인덱스를 dfs함수에 트리 배열과 함께 전달한다.
# 2. dfs함수
#   2-1. 전달받은 인덱스의 배열 값을 삭제한다는 의미로 -2로 바꾼다. (-1은 루트노드와 겹치므로 피한다.)
#   2-2. 배열 전체를 탐색하며, 방금 삭제한 인덱스를 부모노드로 가지는 노드를 찾아 dfs함수를 재귀호출한다.
# 3. 재귀가 끝나면 삭제될 노드들은 전부 -2로 갱신되어있으므로,
#    -2가 아니면서, 다른 노드의 부모노드도 아닌 원소를 찾을 때마다 count를 1씩 늘린다.


# del_idx : 삭제할 노드 인덱스
# del_idx 에 dps 수행, 모든 부모 노드를 -2로 바꾼다
def dfs(del_idx, arr):
    arr[del_idx] = -2   # 삭제할 노드의 부모노드 요소를 -2 로 바꾼다
    for i in range(len(arr)):   # 노드 탐색
        if del_idx == arr[i]:   # 부모 노드가 삭제할 노드라면
            dfs(i, arr)         # 해당 부모 노드를 -2로 설정하고 dfs


if __name__ == "__main__":
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))
    k = int(stdin.readline())

    # 배열 부모 삭제 갱신
    dfs(k, arr)
    count = 0

    for i in range(len(arr)):   # 노드 탐색
        # 자식 노드가 없으면서 부모노드가 -2 가 아닌 수 찾음
        # i not in arr
        # 모든 부모노드를 탐색하여 해당 노드가 없으면 해당 노드는 자식 노드가 없는 것
        if arr[i] != -2 and i not in arr:
            count += 1
    print(count)
