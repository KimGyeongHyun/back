if __name__ == "__main__":
    repeat = int(input())
    blank_value = repeat
    print_value = 1
    star_flag = True

    for i in range(repeat):
        for j in range(blank_value - 1):
            print(' ', end='')
        for j in range(2*print_value-1):
            if star_flag:
                print('*', end='')
                star_flag = False
            else:
                print(' ', end='')
                star_flag = True
        print()
        blank_value -= 1
        print_value += 1
        star_flag = True


