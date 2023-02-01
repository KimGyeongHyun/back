if __name__ == "__main__":
    number = 0
    max_number = 0

    while True:
        try:
            out_number, in_number = map(int, input().split())
        except EOFError as e:
            break
        except ValueError as e:
            break

        number += in_number
        number -= out_number

        if number > max_number:
            max_number = number

    print(max_number)

