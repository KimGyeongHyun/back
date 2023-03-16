from sys import stdin


if __name__ == "__main__":
    sang = int(stdin.readline())
    jung = int(stdin.readline())
    ha = int(stdin.readline())
    cola = int(stdin.readline())
    cider = int(stdin.readline())

    hamburger_list = [sang, jung, ha]
    drink_list = [cola, cider]

    print(min(hamburger_list) + min(drink_list) - 50)
