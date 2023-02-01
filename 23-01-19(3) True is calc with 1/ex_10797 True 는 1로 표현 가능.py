if __name__ == "__main__":
    day_number = int(input())
    car1, car2, car3, car4, car5 = map(int, input().split())

    count = 0

    if day_number == car1:
        count += 1

    if day_number == car2:
        count += 1

    if day_number == car3:
        count += 1

    if day_number == car4:
        count += 1

    if day_number == car5:
        count += 1

        # count += (day_number == car1) 도 사용 가능

    print(count)
