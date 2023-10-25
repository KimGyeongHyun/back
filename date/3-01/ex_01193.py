from sys import stdin


if __name__ == "__main__":
    X = int(stdin.readline())
    x = ((8*X + 1)**(1/2) - 1) / 2
    if x%1 != 0.0:
        x += 1
    x = int(x)
    X -= int(x*(x-1)/2) + 1
    # print(X, x)

    if x%2 == 0:
        print("{}/{}".format(1+X, x-X))
    else:
        print("{}/{}".format(x-X, 1+X))