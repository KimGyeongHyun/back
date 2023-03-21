from sys import stdin

wire_list = []


def get_wire_count(wire_range):

    count = 0
    for wire in wire_list:
        count += wire // wire_range

    return count


if __name__ == "__main__":

    k, n = map(int, stdin.readline().split())

    for _ in range(k):
        wire_list.append(int(stdin.readline()))

    start_wire_range = 0
    end_wire_range = max(wire_list)
    mid = 0

    # for i in range(1, 400):
    #     print(i, get_wire_count(i))

    while True:

        # print(start_wire_range, mid, end_wire_range)

        mid = (start_wire_range + end_wire_range) // 2
        count = get_wire_count(mid)

        # print(count, get_wire_count(mid+1))

        if count == n and count - 1 == get_wire_count(mid+1):
            break

        if start_wire_range == mid:
            break

        if count < n:
            end_wire_range = mid
        else:
            start_wire_range = mid

    print(mid)
