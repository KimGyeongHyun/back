import sys
sys.setrecursionlimit(10**6)

# 이진 탐색 트리에서 pre-order 순회한 결과로 post-order 를 찾는 문제

# 1) 시간 복잡도의 문제
# 이진 탐색 트리의 삽입, 탐색 시간복잡도 평균은 logN 이지만
# 극단적인 경우 N 의 시간복잡도를 가진다
# 따라서 노드가 N개인 경우 모든 노드를 삽입할 시 최대 N**2 의 시간복잡도를 가지고
# N = 10000 이라면 1억번의 연산이 필요하므로
# 초당 2천만번 연산하는 Python 3 성능상 시간 초과가 발생할 수 있다
# 따라서 직접 이진 탐색 트리를 구현하면 시간 초과가 발생한다

# 2) pre-order 배열을 마음대로 수정할 수 없는 문제
# 이진 탐색 트리의 경우 데이터 삽입 순서에 따라 구성이 달라질 수 있다
# 따라서 pre-order 배열을 임의로 정렬하려 하면 원래의 이진 탐색 트리의 형태를 잃어버린다

# 3) 직접 이진 탐색 트리를 사용하지 않고 pre-order 에서 post-order 를 직접 뽑아내기
# 1. pre-order 로부터 부분 트리를 인덱싱으로 뽑아낼 수 있다
# 2. 부분 트리를 뽑아낼 수 있으면 post-order 순회가 가능하다

# 들어가기 전 정리
# 1. 인덱싱 된 pre-order 의 배열은 전체 이진 검색 트리의 부분 트리이다
# 2. 인덱싱 된 pre-order 의 배열의 첫 요소는 해당 부분 트리의 루트 노드이다
# 3. 루트 노드를 기준으로 부분 트리를 뽑아낸다

# pre-order 배열로부터 부분 트리 인덱싱하기
# 50 30 24 5 28 45 98 52 60 의 경우
# 1. 루트 노드보다 크고 제일 앞에 있는 요소를 찾는다 (루트:50 / 제일 앞에 있는 큰 수:98)
# 2. 제일 앞에 있는 큰 요소의 인덱스를 a라고 할 때 두 개의 부분 트리는
#   1 ~ a-1 / a ~ 끝 인덱스   (30 24 5 28 45 / 98 52 60)
#   으로 볼 수 있다
#   30 24 5 28 45 / 98 52 60
# 3. 해당 부분 트리의 자식이 없을 때까지 부분 트리를 탐색한다 (post-order)
#   30 24 5 28 45 -> 24 5 28 / 45
#   24 5 28 -> 5 / 28
#   98 52 60 -> 52 60
#   52 60 -> 60
# 재귀 함수를 통해 먼저 부분 트리를 순회한 후 루트 노드를 출력한다


def get_post(first_index, end_index):
    """
    pre-order 배열의 인덱싱으로 부분 트리를 뽑아내며 post-order 수행하는 메소드\n
    :param first_index: 부분 트리의 시작 인덱스
    :param end_index: 부분 트리의 끝 인덱스
    :return: None
    """

    # 부분 트리의 자식 노드가 없다면 해당 부분 트리의 루트 노드를 출력하고 탈출
    if first_index == end_index:
        print(l[first_index])
        return

    # 인덱싱이 반대로 되었을 경우 예외 처리
    if end_index < first_index:
        return

    val = l[first_index]    # 루트 노드 값
    mid = end_index+1       # 부분 트리를 쪼갤 인덱스

    # 루트 노드보다 크고 제일 앞에 있는 요소를 찾는다
    for i in range(first_index+1, end_index+1):
        if val < l[i]:  # 해당 요소를 찾았다면
            # 부분 트리를 쪼갤 인덱스 갱신
            mid = i
            break

    # 부분 트리 순회
    get_post(first_index + 1, mid - 1)
    get_post(mid, end_index)

    # 부분 트리 순회가 끝나면 루트 노드 출력 (post-order)
    print(val)


if __name__ == "__main__":
    l = []
    while True:
        a = sys.stdin.readline()
        if a == "":
            break
        l.append(int(a))

    get_post(0, len(l)-1)
