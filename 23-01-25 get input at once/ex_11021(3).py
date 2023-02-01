if __name__ == "__main__":
    repeat = int(input())

    for i in range(repeat):
        a, b = map(int, input().split())
        print("Case #{}: {}".format(i+1, a + b))