if __name__ == "__main__":
    plus, minus = map(int, input().split())

    # 먼저 2로 나누는 게 아니라 2배가 아닐 경우 걸러내는 것이 좋음
    a = (plus + minus) / 2
    b = (plus - minus) / 2

    if a % 1 != 0 or b % 1 != 0 or b < 0:
        print(-1)
    else:
        print(int(a), int(b))

