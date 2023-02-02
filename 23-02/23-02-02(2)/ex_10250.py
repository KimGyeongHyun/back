if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        H, W, N = map(int, input().split())
        w = N // H + 1
        h = N % H
        if N % H == 0:
            h = H
            w -= 1
        print(h*100 + w)