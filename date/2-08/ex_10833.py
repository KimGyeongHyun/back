if __name__ == "__main__":
    N = int(input())
    sum = 0

    for _ in range(N):
        a, b = map(int, input().split())
        sum += b % a

    print(sum)