import sys
input = sys.stdin.readline

# 규칙
# 2**n * 2**n 으로 구성된 배열
# 가로와 세로를 반으로 정확하게 잘라 4개의 배열을 비교하면
# 각각의 배열은 시작하는 수만 다를 뿐 같은 규칙성으로 수가 전개된다

# (c, r) 좌표값 구하기
# 4개로 자른 배열의 시작하는 수를 갱신한다
# 4개로 자른 배열 중 (c, r) 이 속하는 배열을 선택하고 해당 연산을 재귀적으로 반복한다
# 그러면 시작하는 수가 (c, r) 의 좌표값이 된다

number = 0  # 시작값 (최종적으로 (c, r)의 좌표값)


def get_number_with_rc(n, r, c):

    if n == 0:
        return

    global number
    mid = 2**(n-1)
    big = 2**(2 * n - 2)

    # 시작값 갱신
    if r < mid:
        if c >= mid:
            c -= mid
            number += big
    else:
        r -= mid
        if c < mid:
            number += 2 * big
        else:
            c -= mid
            number += 3 * big

    # 재귀 호출
    get_number_with_rc(n-1, r, c)


if __name__ == "__main__":
    n, r, c = map(int, input().split())
    get_number_with_rc(n, r, c)
    print(number)
