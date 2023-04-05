import sys
input = sys.stdin.readline


l = []

# 1. input_right >= l[i][0]
# input_right 가 l[i] 의 left 랑 닿았거나 더 크다면
# input_left 부분을 모두 영역으로 설정해야 함
# input_left 가 l[i]의 right 보다 크다면 무시
# l[i] right 보다 input_left 가 크다면 따로 추가해야 함
# 1) input_left 가 l[k] 안에 포함한다면
#   l[k] left, l[i] right 의 튜플을 삽입
#   k ~ i 까지의 튜플 삭제
# 2) 포함하는 튜플이 없다면
#   input_left, l[i] right 의 튜플을 삽입
#   input_left 보다 큰 값을 가진 left l 튜플을 모두 삭제

# 2. l[i][1] >= input_left
# input_left 가 l[i] 의 right 랑 닿았거나 더 크다면
# input_right 부분을 모두 영역으로 설정해야 함
# input_right 가 l[i] 의 right 보다 작다면 무시
# input_right 보다 l[i] left 가 크다면 따로 추가해야 함
# 이미 위에서 처리 했으므로 할 필요 없음
# 1) input_right 가 l[k] 안에 포함한다면
#   l[i] left, l[k] right 의 튜플을 삽입
#   i ~ k 까지의 튜플 삭제
# 2) 포함하는 튜플이 없다면
#   l[i] left, input_right 의 튜플을 삽입
#   input_right 보다 작은 값을 가진 right l 튜플을 모두 삭제

# 위의 과정으로 풀이 결과 시간 초과 발생


def add_line(left, right):
    if len(l) != 0:

        first, second, l_right, l_left = 0, 0, 0, 0

        # first : right 를 포함하거나 작은 수를 가지는 l 의 인덱스
        for i in range(len(l)):
            if right >= l[i][0]:
                # left, right 가 l[i] 안에 있는 경우 무시
                # if left >= l[i][0]:
                #     return
                if l[i][1] < left:
                    l.insert(i+1, (left, right))
                    return
                first = i
                break

        l_right = l[first][1]

        # second : left 를 포함하거나 큰 수를 가지는 l 의 인덱스
        for i in range(first, -1, -1):
            if left <= l[i][1]:
                second = i
                break

        if l[second][0] <= left:
            l_left = l[second][0]
        else:
            l_left = left

        for _ in range(first - second + 1):
            del l[second]

        l.insert(second, (l_left, l_right))

        first, second, l_right, l_left = 0, 0, 0, 0

        for i in range(len(l)):
            if l[i][1] >= left:
                if right <= l[i][1]:
                    return
                first = i

        l_left = l[first][0]
        for i in range(first, len(l)):
            if right >= l[i][0]:
                second = i
                break

        if right <= l[second][1]:
            l_right = l[second][1]
        else:
            l_right = right

        for _ in range(second - first + 1):
            del l[first]

        l.insert(first, (l_left, l_right))

        # print("right :", l)

    else:
        l.append((left, right))


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        x, y = map(int, input().split())
        add_line(x, y)

    sum = 0
    for left, right in l:
        sum += right - left

    print(sum)