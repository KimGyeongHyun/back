from sys import stdin


def recurr(n):
    return (n%10) * 10 + (n%10 + n//10) % 10


if __name__ == "__main__":

    n = int(stdin.readline())
    correct = n
    count = 1
    while True:
        n = recurr(n)
        if correct == n:
            break
        else:
            count += 1

    print(count)