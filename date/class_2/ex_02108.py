from sys import stdin


if __name__ == "__main__":
    n = int(stdin.readline())
    l = []
    for _ in range(n):
        l.append(int(stdin.readline()))

    l.sort()

    first = sum(l)/n

    second = l[len(l)//2]

    int_dict = {}
    for number in l:
        if number not in int_dict.keys():
            int_dict[number] = 1
        else:
            int_dict[number] += 1

    max_number = 0
    max_index = None
    max_list = []
    for key, value in int_dict.items():
        if max_number < value:
            max_index = key
            max_number = value
            max_list = [key]
        elif max_number == value:
            max_list.append(key)

    if len(max_list) == 1:
        third = max_index
    else:
        max_list.sort()
        third = max_list[1]

    fourth = l[-1] - l[0]

    print(int(round(first, 0)))
    print(second)
    print(third)
    print(fourth)