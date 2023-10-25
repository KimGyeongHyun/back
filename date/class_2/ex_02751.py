from sys import stdin


if __name__ == "__main__":
    n = int(stdin.readline())
    l = []
    for _ in range(n):
        l.append(int(stdin.readline()))

    l.sort()
    for number in l:
        print(number)