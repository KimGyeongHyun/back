from sys import stdin


def is_in_list(input_sorted_list, input_number):
    l = input_sorted_list
    n = input_number

    start_index = 0
    end_index = len(input_sorted_list) - 1

    while True:

        start_number = l[start_index]
        end_number = l[end_index]

        if end_index - start_index == 1 and start_number < n < end_number:
            return False

        if start_number == n or end_number == n:
            return True

        mid_index = (start_index + end_index) // 2
        mid_number = l[mid_index]

        if mid_number == n:
            return True

        if mid_number > n:
            end_index = mid_index - 1
        else:
            start_index = mid_index + 1

        if len(l) - 1 < start_index or end_index < 0:
            return False

        if end_index <= start_index:
            return False


if __name__ == "__main__":
    n = int(stdin.readline())
    nl = list(map(int, stdin.readline().split()))
    m = int(stdin.readline())
    ml = list(map(int, stdin.readline().split()))

    nl.sort()

    for number in ml:
        if is_in_list(nl, number):
            print(1)
        else:
            print(0)