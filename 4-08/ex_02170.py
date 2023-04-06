import sys
input = sys.stdin.readline

# 선분 리스트를 x 순으로 정렬, x가 같다면 y 순으로 정렬
# 정렬 시간복잡도 : nlog(n)
# n 이 1,000,000 이라 했을 때 20,000,000 정도의 계산이 필요
# Python 3 이 20,000,000번의 계산이 1초 정도 걸리므로 시간 초과가 나지 않음

# 알고리즘 순서   (선분 리스트가 정렬 되었다는 조건 하)
# 첫번째의 x값 가져옴
# 해당 x값의 제일 큰 y 값까지 index 이동 후 y_big 에 저장
# y_big < x 까지 y_big 갱신하면서 index 이동
# 더 이상 없다면 y_big - 첫번째 x 값을 sum 에 더함
# 위의 과정 반복

if __name__ == "__main__":
    n = int(input())
    l = []
    for _ in range(n):
        l.append(tuple(map(int, input().split())))

    # x 순으로 정렬 후 y 순으로 정렬
    l = sorted(l, key=lambda x: (x[0], x[1]))

    index = 0   # 탐색할 인덱스
    sum = 0     # 총 거리

    while index < n:

        # 첫번째 x값 가져옴
        x = l[index][0]

        while True:
            # x 가 달라질 때까지 index 이동
            index += 1
            # 마지막 선분일 경우 탈출
            if index >= n:
                break
            # index-1 에서 같은 x 값에서 최대 y값 나옴
            if x != l[index][0]:
                break

        # x가 같은값을 가지는 선분의 마지막 선분인 경우
        # 마지막 선분은 제일 큰 y 값을 가지고 있음
        # 따라서 (마지막 y 값 - x) 가 최종 선분 길이
        # 해당 길이를 sum 에 더하고 탈출
        if index >= n:
            sum += l[n-1][1] - x
            break

        # x 에서 제일 큰 y 값을 구함
        y_big = l[index-1][1]

        # y_big < x 까지 y_big 갱신하면서 index 이동
        while y_big >= l[index][0]:
            if y_big < l[index][1]:
                y_big = l[index][1]
            index += 1
            # 마지막 선분일 경우 탈출
            if index >= n:
                break

        # y_big 보다 작거나 같은 선분이 더이상 없거나 마지막 선분일 경우
        # y_big - x 를 sum 에 더함
        sum += y_big - x

    print(sum)
