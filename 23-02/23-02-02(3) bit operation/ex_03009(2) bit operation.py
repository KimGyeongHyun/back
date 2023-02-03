if __name__ == "__main__":
    resx, resy = 0, 0
    for i in range(3):
        x, y = map(int, input().split())

        # XOR 비트연산을 통해 짝수의 값들은 없어지도록 함
        resx ^= x
        resy ^= y

    print('%d %d' % (resx, resy))