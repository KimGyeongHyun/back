import sys
input = sys.stdin.readline

# 인덱싱으로 잘 하면 풀릴듯
# start, end 인덱스로 라인 스위핑 수행하기


def get_sum(start, end):
    if start == 0:
        return presum[end]

    return presum[end] - presum[start-1]


def get_min(n):

    min = int(1e9)

    start, end = 0, 0

    while end < n:
        tsum = get_sum(start, end)
        if tsum < s:
            end += 1
        else:
            if end - start + 1 < min:
                min = end - start + 1
            start += 1

    if min > 100000:
        return 0
    else:
        return min


if __name__ == "__main__":
    n, s = map(int, input().split())
    l = list(map(int, input().split()))

    presum = [l[0]]

    for i in range(1, n):
        presum.append(presum[-1] + l[i])

    print(get_min(n))