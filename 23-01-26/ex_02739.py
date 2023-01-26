if __name__ == "__main__":
    repeat = int(input())

    for M in range(1, 10):
        print("{} * {} = {}".format(repeat, M, repeat * M))