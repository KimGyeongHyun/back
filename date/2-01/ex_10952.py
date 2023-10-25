result_dict = {}

if __name__ == "__main__":

    i = 0

    while True:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break

        result_dict[i] = a + b
        i += 1

    for _, value in result_dict.items():
        print(value)