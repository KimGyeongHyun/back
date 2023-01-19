if __name__ == "__main__":
    N, W, H, L = map(int, input().split())

    print(min(N, (W//L) * (H//L)))
