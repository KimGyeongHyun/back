if __name__ == "__main__":

    repeat = int(input())
    scores = map(int, input().split())

    current_score = 1
    sum = 0

    for item in scores:
        if item == 1:
            sum += current_score
            current_score += 1
        else:
            current_score = 1

    print(sum)