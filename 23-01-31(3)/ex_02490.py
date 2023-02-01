if __name__ == "__main__":
    for _ in range(3):
        a, b, c, d = map(int, input().split())

        if a+b+c+d == 4:
            print('E')
        elif a+b+c+d == 3:
            print('A')
        elif a+b+c+d == 2:
            print('B')
        elif a+b+c+d == 1:
            print('C')
        else:
            print('D')