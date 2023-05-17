from sys import stdin
import matplotlib.pyplot as plt


MONTH_DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAYS_SUM = 365

flowers = []


def print_flowers():

    print("="*10)
    print("flowers")

    for start, end in flowers:
        print(start, end)
    print("="*10)


def print_flowers_with_graph():

    for i in range(len(flowers)):
        print(i+1, flowers[i][0], flowers[i][1])
        plt.hlines(i+1, flowers[i][0], flowers[i][1])

    plt.vlines(365, 1, len(flowers)+1, color='red',
                linestyle='--', linewidth=2)
    plt.vlines(get_days_from_0(3, 1), 1, len(flowers) + 1, color='blue',
               linestyle='--', linewidth=2)
    plt.vlines(get_days_from_0(11, 30), 1, len(flowers) + 1, color='blue',
               linestyle='--', linewidth=2)
    plt.show()


def get_days_from_0(month, day):
    print(month, "/", day)

    days = day
    for i in range(1, month):
        days += MONTH_DAYS[i]

    return days


def get_flowers(f, s):

    print("input :", f, s)
    print_flowers()

    for ff, fs in flowers:
        if ff <= f and s <= fs:
            print("erased in", ff, fs)
            return

    erase_list = []

    for i in range(len(flowers)):
        if f <= flowers[i][0] and flowers[i][1] <= s:
            print("number in", flowers[i][0], flowers[i][1])
            erase_list.append(i)

    erase_list.reverse()

    for idx in erase_list:
        del flowers[idx]

    flowers.append((f, s))


if __name__ == "__main__":
    n = int(stdin.readline())
    for _ in range(n):
        fm, fd, sm, sd = map(int, stdin.readline().split())
        f = get_days_from_0(fm, fd)
        s = get_days_from_0(sm, sd)
        flowers.append((f, s))
        print()

    flowers.sort(key=lambda x: (x[0]))
    print_flowers()

    print(get_days_from_0(3, 1))
    print(get_days_from_0(11, 30))

    print_flowers_with_graph()


