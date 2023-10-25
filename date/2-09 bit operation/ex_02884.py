if __name__ == "__main__":
    hours, minutes = map(int, input().split())

    minutes -= 45

    if minutes < 0:
        hours -= 1

    minutes %= 60
    hours %= 24

    print(hours, minutes)