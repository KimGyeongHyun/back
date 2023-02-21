if __name__ == "__main__":
    repeat = int(input())
    temp_value = repeat

    for i in range(repeat-1):
        for j in range(repeat+i-1):
            if j == temp_value-1:
                pass
                print('*', end='')
            else:
                pass
                print(' ', end='')
        temp_value -= 1
        print('*')

    for i in range(2*repeat-1):
        print('*', end='')
