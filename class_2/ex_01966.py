from sys import stdin


if __name__ == "__main__":
    t = int(stdin.readline())
    for _ in range(t):
        n, m = map(int, stdin.readline().split())
        l = list(map(int, stdin.readline().split()))
        count = 0
        index = m

        while True:
            # print(l)
            # print("start index : {}".format(index))
            lmax = max(l)
            max_index = l.index(lmax)
            # print("max index : {}".format(max_index))
            l = l[max_index:] + l[:max_index]
            if index < max_index:
                index += len(l) - max_index
            else:
                index -= max_index

            # print("last index : {}".format(index))

            count += 1
            if index == 0:
                break
            l = l[1:]
            index -= 1

        print(count)