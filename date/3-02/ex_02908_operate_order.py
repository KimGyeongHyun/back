from sys import stdin


def print_big(a, b):
    # 100 을 앞에 곱하면 %10 연산에서 날라감
    # 순서 중요
    a = (a%10) * 100 + ((a//10)%10) * 10 + a//100
    b = (b % 10) * 100 + ((b // 10) % 10) * 10 + b // 100

    if a > b:
        return a
    else:
        return b


if __name__ == "__main__":
    a, b = map(int, stdin.readline().split())
    print(print_big(a, b))


