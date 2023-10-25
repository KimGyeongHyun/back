if __name__ == "__main__":
    N, X = map(int, input().split())
    a = map(int, input().split())

    for item in a:
        if item < X:
            print(item, end=' ')