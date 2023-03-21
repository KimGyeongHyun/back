from sys import stdin


if __name__ == "__main__":
    n_str = stdin.readline()
    n_list = []
    for char in n_str[:-1]:
        n_list.append(char)

    n_list.sort(reverse=True)

    for char in n_list:
        print(char, end="")
