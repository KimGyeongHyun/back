from sys import stdin
import array as arr


if __name__ == "__main__":
    a = int(stdin.readline())
    b = int(stdin.readline())
    c = int(stdin.readline())

    num_list = arr.array('i', [0 for _ in range(10)])

    mul = a * b * c
    div = 1

    while mul//div != 0:
        num_list[mul//div%10] += 1
        div *= 10

    for number in num_list:
        print(number)
