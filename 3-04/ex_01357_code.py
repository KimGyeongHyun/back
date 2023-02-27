from sys import stdin


def rev(n):
    res = 0

    # 작은 수부터 시작
    # 작은 수를 res 에 대입하고 10을 곱해 왼쪽으로 옮김
    # 파라미터 n을 10으로 나눠 n이 0일 때까지 반복
    while n:
        res *= 10
        res += n % 10
        n //= 10

    return res


if __name__ == "__main__":
    x, y = map(int, stdin.readline().split())
    print(rev(rev(x) + rev(y)))