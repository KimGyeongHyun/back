import sys


def factorial(input_number):
    if input_number == 0:
        return 1

    temp_number = 1
    for i in range(input_number):
        temp_number *= i+1

    return temp_number


if __name__ == "__main__":
    while True:
        get = int(sys.stdin.readline())
        if get == 0:
            break

        dec = 0
        factorial_index = 1

        while get != 0:
            number = get % 10
            dec += number * factorial(factorial_index)
            factorial_index += 1
            get //= 10

        print(dec)