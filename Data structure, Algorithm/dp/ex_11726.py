def get_tile_num(n):
    t = [0, 1, 2]

    for i in range(3, n+1):
        t.append(t[i-2] + t[i-1])

    return t[n]


if __name__ == "__main__":
    n = int(input())
    print(get_tile_num(n)%10007)