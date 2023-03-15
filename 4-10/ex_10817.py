from sys import stdin


def middle(input_list):
    a = input_list[0]
    b = input_list[1]
    c = input_list[2]

    if a <= b <= c or c <= b <= a:
        return b
    elif b <= c <= a or a <= c <= b:
        return c
    else:
        return a


if __name__ == "__main__":
    number_list = list(map(int, stdin.readline().split()))
    print(middle(number_list))