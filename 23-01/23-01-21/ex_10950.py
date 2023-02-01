result_dict = {}

if __name__ == "__main__":
    repeat = int(input())

    for i in range(repeat):
        a, b = map(int, input().split())
        result_dict[i] = a + b

    for _, value in result_dict.items():
        print(value)