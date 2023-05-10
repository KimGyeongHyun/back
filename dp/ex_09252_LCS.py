import sys
input = sys.stdin.readline

# LCS 알고리즘


def print_dp():
    for line in dp[1:]:
        print(*line[1:])
    print()


def set_dp(f, s):

    for i in range(1, len(f)):
        for j in range(1, len(s)):
            # print(i, j)

            if f[i-1] == s[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = dp[i-1][j] if dp[i-1][j] >= dp[i][j-1] else dp[i][j-1]

            # print_dp()


def get_index_of_dp(f, s):

    i, j = len(f)-1, len(s)-1
    l = []

    while True:

        if i == 0 and j == 0:
            break

        if i >= 1 and dp[i-1][j] == dp[i][j]:
            i -= 1
        elif j >= 1 and dp[i][j-1] == dp[i][j]:
            j -= 1
        else:
            l.append(i)
            i -= 1
            j -= 1

    l.reverse()
    return l


if __name__ == "__main__":
    f = input()
    s = input()

    n = len(f) - 1
    dp = [[0 for _ in range(len(s))] for _ in range(len(f))]

    set_dp(f, s)

    index_list = get_index_of_dp(f, s)

    print(len(index_list))
    for idx in index_list:
        print(f[idx-1], end='')