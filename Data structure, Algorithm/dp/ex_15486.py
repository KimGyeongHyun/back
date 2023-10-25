from sys import stdin


def get_biggest_cost(n, time, cost):

    l = [0 for _ in range(n)]

    for i in range(n-1, -1, -1):

        if i == n-1:
            if time[i] == 1:
                l[i] = cost[i]
            continue

        if time[i] + i > n:
            l[i] = l[i+1]
            continue

        if time[i] + i == n:
            last = cost[i]
        else:
            last = cost[i] + l[i + time[i]]

        if l[i+1] < last:
            l[i] = last
        else:
            l[i] = l[i+1]

    return l[0]


if __name__ == "__main__":
    n = int(stdin.readline())
    time = []
    cost = []
    for _ in range(n):
        t, c = map(int, stdin.readline().split())
        time.append(t)
        cost.append(c)

    print(get_biggest_cost(n, time, cost))