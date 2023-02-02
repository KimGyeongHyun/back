if __name__ == "__main__":
    repeat = int(input())
    column = map(int, input().split())
    index = 1
    punished = 0

    for item in column:
        if index != item:
            punished += 1
        index += 1

    print(punished)