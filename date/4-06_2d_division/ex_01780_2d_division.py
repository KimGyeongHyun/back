import sys
input = sys.stdin.readline


minus = 0
zero = 0
plus = 0


def is_one_page(arr, value):

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] != value:
                return False

    return True

def count_recurr(arr, n):

    global minus, zero, plus

    value = arr[0][0]

    if len(arr) == 1:
        if value == -1:
            minus += 1
        elif value == 0:
            zero += 1
        elif value == 1:
            plus += 1

        return

    if not is_one_page(arr, value):
        one = n//3
        two = one * 2
        count_recurr([row[:one] for row in arr[:one]], one)
        count_recurr([row[:one] for row in arr[one:two]], one)
        count_recurr([row[:one] for row in arr[two:]], one)
        count_recurr([row[one:two] for row in arr[:one]], one)
        count_recurr([row[one:two] for row in arr[one:two]], one)
        count_recurr([row[one:two] for row in arr[two:]], one)
        count_recurr([row[two:] for row in arr[:one]], one)
        count_recurr([row[two:] for row in arr[one:two]], one)
        count_recurr([row[two:] for row in arr[two:]], one)

    else:
        if value == -1:
            minus += 1
        elif value == 0:
            zero += 1
        elif value == 1:
            plus += 1


if __name__ == "__main__":
    n = int(input())
    l = []
    for _ in range(n):
        l.append(list(map(int, input().split())))

    count_recurr(l, n)
    print(minus)
    print(zero)
    print(plus)
