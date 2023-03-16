from sys import stdin
import array as arr


def calc(input_number, n, p):
    return input_number * n % p


def recurr_num(n, p):
    num_arr = arr.array('i')
    result = n

    while True:
        result = calc(result, n, p)
        for i in range(len(num_arr)):
            if num_arr[i] == result:
                return len(num_arr) - i

        num_arr.append(result)


if __name__ == "__main__":
    n, p = map(int, stdin.readline().split())
    print(recurr_num(n, p))
