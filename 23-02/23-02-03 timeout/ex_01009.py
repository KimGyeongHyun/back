if __name__ == "__main__":

    T = int(input())
    for _ in range(T):
        a, b = map(int, input().split())
        a %= 10

        if a == 0:
            print(10)

        elif a == 1 or a == 5 or a ==6:
            print(a)

        elif a == 2:
            b %= 4
            if b == 1:
                print(2)
            elif b == 2:
                print(4)
            elif b == 3:
                print(8)
            elif b == 0:
                print(6)

        elif a == 3:
            b %= 4
            if b == 1:
                print(3)
            elif b == 2:
                print(9)
            elif b == 3:
                print(7)
            elif b == 0:
                print(1)

        elif a == 4:
            b %= 2
            if b == 1:
                print(4)
            elif b == 0:
                print(6)

        elif a == 7:
            b %= 4
            if b == 1:
                print(7)
            if b == 2:
                print(9)
            if b == 3:
                print(3)
            if b == 0:
                print(1)

        elif a == 8:
            b %= 4
            if b == 1:
                print(8)
            if b == 2:
                print(4)
            if b == 3:
                print(2)
            if b == 0:
                print(6)

        elif a == 9:
            b %= 2
            if b == 1:
                print(9)
            elif b == 0:
                print(1)