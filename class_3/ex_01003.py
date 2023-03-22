from sys import stdin


if __name__ == "__main__":
    t = int(stdin.readline())

    tuple_list = [(1, 0), (0, 1)]

    for i in range(2, 41):
        tuple_list.append((tuple_list[i-2][0] + tuple_list[i-1][0],
                           tuple_list[i-2][1] + tuple_list[i-1][1]))

    for _ in range(t):

        a, b = tuple_list[int(stdin.readline())]

        print(a, b)