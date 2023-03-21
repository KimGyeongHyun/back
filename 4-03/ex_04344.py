from sys import stdin


if __name__ == "__main__":
    c = int(stdin.readline())

    for _ in range(c):

        temp_list = list(map(int, stdin.readline().split()))
        n = temp_list[0]
        score_list = temp_list[1:]

        count = 0
        mean = sum(score_list) / len(score_list)

        for score in score_list:
            if mean < score:
                count += 1

        print("{:.3f}%".format(100 * count / len(score_list)))

