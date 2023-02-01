if __name__ == "__main__":
    N, M, K = map(int, input().split())

    print(N - (M - K if M >= K else K - M))