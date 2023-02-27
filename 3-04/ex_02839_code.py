from sys import stdin


def is_possible(n):
    cnt = 0

    # 먼저 5로 나눠지나를 확인
    # 아니라면 3을 빼서 봉투 +1
    # 반복
    # 설탕이 없어질 때까지 반복
    # 만약 설탕이 -라면 계속 3을 빼면서 5로 나눠지는 수를 찾다가 못 찾은 것
    while n > 0:
        if n % 5 == 0:
            cnt += n // 5
            n = 0
        else:
            n -= 3
            cnt += 1

    if n < 0:
        return -1
    else:
        return cnt


if __name__ == "__main__":
    n = int(stdin.readline())
    print(is_possible(n))