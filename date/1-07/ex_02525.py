if __name__ == "__main__":
    hours, minutes = map(int, input().split())
    cook_time = int(input())

    minutes += cook_time

    hours += minutes // 60
    hours = hours % 24
    minutes = minutes % 60

    print(hours, minutes)