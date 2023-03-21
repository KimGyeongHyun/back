from sys import stdin


if __name__ == "__main__":
    n = int(stdin.readline())
    word_list = []
    for _ in range(n):
        temp_str = str(stdin.readline())[:-1]
        if (temp_str, len(temp_str)) in word_list:
            continue
        word_list.append((temp_str, len(temp_str)))

    word_list = sorted(word_list, key=lambda x : (x[1], x[0]))

    for word_tuple in word_list:
        print(word_tuple[0])

