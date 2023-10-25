from sys import stdin


if __name__ == "__main__":
    n = int(stdin.readline())
    l = [i for i in range(1, n+1)]

    burry_flag = True

    while len(l) >= 2:
        if burry_flag:
            temp_l = [l[i] for i in range(1, len(l), 2)]
        else:
            temp_l = [l[i] for i in range(0, len(l), 2)]
        if len(l) % 2 != 0:
            burry_flag = not burry_flag
        l = temp_l

    print(l[0])