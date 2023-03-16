from sys import stdin


if __name__ == "__main__":
    l = []
    flag = False
    for _ in range(10):
        flag = False
        n = int(stdin.readline()) % 42
        for number in l:
            if number == n:
                flag = True
        if not flag:
            l.append(n)

    print(len(l))