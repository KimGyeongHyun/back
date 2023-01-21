result_dict = {}

if __name__ == "__main__":
    repeat = int(input())

    for i in range(repeat):
        a, b = map(int, input().split())
        result_dict[i] = (a, b, a + b)

    for key, value in result_dict.items():
        print('Case #{}: {} + {} = {}'.format(key+1, value[0], value[1], value[2]))