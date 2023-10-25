from sys import stdin

# 적게 버티는 줄은 상황에 따라 버려야 한다
# 줄을 버리는 순서는 버틸 수 있는 하중이 작은 순서이다

# ex)
# [1, 2, 3, 4, 5] 의 줄이 있다면
# [1, 2, 3, 4, 5], [2, 3, 4, 5], [3, 4, 5], [4, 5], [5]
# 의 규칙으로 버틸수 있는 하중의 최대 크기를 구한다
# 버틸 수 있는 하중의 최대 크기는 '버틸 수 있는 하중이 제일 작은 줄의 하중 * 총 줄 갯수'
# 1*5, 2*4, 3*3, 4*2, 5*1
# 즉 [3, 4, 5] 일 때 최대 하중 9를 버틸 수 있다


def get_biggest_weight(ropes):

    ropes_weight = []

    for i in range(len(ropes)):
        ropes_weight.append(ropes[i] * (len(ropes) - i))

    return max(ropes_weight)


if __name__ == "__main__":
    n = int(stdin.readline())
    ropes = []
    for _ in range(n):
        ropes.append(int(stdin.readline()))
    ropes.sort()

    print(get_biggest_weight(ropes))