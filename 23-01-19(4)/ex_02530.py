if __name__ == "__main__":
    hours, minutes, seconds = map(int, input().split())
    cook_time = int(input())

    seconds += cook_time

    minutes += seconds // 60
    seconds %= 60

    hours += minutes // 60
    minutes %= 60

    hours %= 24

    print(hours, minutes, seconds)