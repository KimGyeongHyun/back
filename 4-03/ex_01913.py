from sys import stdin
import math


if __name__ == "__main__":
    n = int(stdin.readline())
    m = int(stdin.readline())

    number_list = [[0 for _ in range(n)] for _ in range(n)]

    x = n // 2 - 1
    y = n // 2
    if n % 2 == 0:
        y -= 1

    for i in range(1, n+1):

        if i % 2 != 0:
            x += 1
            number_list[x][y] = (i-1)**2 + 1
            for j in range(i-1):
                y -= 1
                number_list[x][y] = number_list[x][y+1] + 1
            for j in range(i-1):
                x -= 1
                number_list[x][y] = number_list[x+1][y] + 1

        else:
            x -= 1
            number_list[x][y] = (i-1)**2 + 1
            for j in range(i-1):
                y += 1
                number_list[x][y] = number_list[x][y-1] + 1
            for j in range(i-1):
                x += 1
                number_list[x][y] = number_list[x-1][y] + 1

    # index : 3 이라면 4 ~ 9 까지의 수를 가짐
    index = m ** (1/2)
    if index % 1 != 0:
        index = math.ceil(index)
    else:
        index = int(index)

    x = n // 2
    y = n // 2
    if n % 2 == 0:
        y -= 1

    if index % 2 != 0:
        move = (index - 1) // 2
        x += move
        y += move
        # print(x, y)
        move = m - (index-1) ** 2 - 1
        # print(move, index)
        if move < index:
            y -= move
        else:
            y -= index - 1
            x -= move - (index - 1)

    else:
        move = (index - 2) // 2
        x -= move + 1
        y -= move
        move = m - (index-1) ** 2 - 1
        if move < index:
            y += move
        else:
            y += index - 1
            x += move - (index - 1)

    for i in range(n):
        for j in range(n):
            print("{} ".format(number_list[i][j]), end="")
        print()

    print(x+1, y+1)
