if __name__ == "__main__":
    K, N, M = map(int, input().split())

    get_money = K * N - M

    print(get_money if get_money >= 0 else 0)