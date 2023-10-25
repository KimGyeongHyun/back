from sys import stdin


def get_biggest_score(n, num):
    if n == 1:
        return num[1]

    if n == 2:
        return num[1] + num[2]

    if n == 3:
        return max(num[2] + num[3], num[1] + num[3])

    t = [0, num[1], 0, num[1] + num[3]]
    f = [0, 0, num[1] + num[2], num[2] + num[3]]

    for i in range(4, n+1):
        t.append(max(t[i-2], f[i-2]) + num[i])
        f.append(t[i-1] + num[i])

    return max(t[n], f[n])


if __name__ == "__main__":
    n = int(stdin.readline())
    num = [0]
    for _ in range(n):
        num.append(int(stdin.readline()))

    print(get_biggest_score(n, num))

