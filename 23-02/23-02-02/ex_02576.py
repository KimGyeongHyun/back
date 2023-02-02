if __name__ == "__main__":
    sum = 0
    sum_number = 0
    min = 0

    for i in range(7):
        get = int(input())

        if get % 2 == 1:

            if sum_number == 0:
                min = get
            else:
                if min > get:
                    min = get

            sum += get
            sum_number += 1

    if sum_number == 0:
        print(-1)
    else:
        print(sum, min)