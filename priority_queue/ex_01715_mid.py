from sys import stdin


def print_dp():
    print(*dp[1:])
    print()


if __name__ == "__main__":
    n = int(stdin.readline())
    l = [0]
    dp = [0 for _ in range(n+1)]

    for i in range(n):
        num = int(stdin.readline())
        l.append(num)

    if n == 1:
        print(0)
        exit()

    l.sort()

    presum = []
    sum = 0
    for num in l:
        sum += num
        presum.append(sum)

    print(*l[1:])
    print(*presum[1:])
    print()

    dp[2] = l[1] + l[2]

    for i in range(3, n+1):
        f = dp[i-1] + presum[i]
        s = dp[i-2] + 2 * presum[i] - presum[i-2]
        if f <= s:
            dp[i] = f
        else:
            dp[i] = s
        print(" >>", i, f, s)
        print_dp()

    print(dp[-1])