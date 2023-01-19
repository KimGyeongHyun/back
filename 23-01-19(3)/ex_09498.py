if __name__ == "__main__":
    score = int(input())

    if 90 <= score <= 100:
        print('A')
    elif 80 <= score:
        print('B')
    elif 70 <= score:
        print('C')
    elif 60 <= score:
        print('D')
    else:
        print('F')