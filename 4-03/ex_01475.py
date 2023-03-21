from sys import stdin
import math


if __name__ == "__main__":
    n = stdin.readline()
    number_list = [0 for _ in range(9)]

    for char in n[:-1]:
        number = ord(char) - 48
        if number == 9:
            number = 6

        number_list[number] += 1

    number_list[6] = math.ceil(number_list[6]/2)

    print(max(number_list))