from sys import stdin


if __name__ == "__main__":
    n = int(stdin.readline())

    two = 0
    five = 0

    for i in range(n+1):

        temp = i

        while temp%2 == 0:
            if temp < 2:
                break
            temp //= 2
            two += 1

        while temp%5 == 0:
            if temp < 5:
                break
            temp //= 5
            five += 1

    if two < five:
        print(two)
    else:
        print(five)