if __name__ == "__main__":
    repeat = int(input())

    for _ in range(repeat):
        a, b = map(int, input().split())
        print(a + b)

