if __name__ == "__main__":
    N, X = map(int, input().split())

    for _ in range(N):
        number = int(input())
        if X > number:
            print(number)