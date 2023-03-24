from sys import stdin


if __name__ == "__main__":
    n = int(stdin.readline())
    f_score = 0
    s_score = 0
    f_time = 0
    s_time = 0
    before_time = 0

    l = []

    for _ in range(n):
        a, b = stdin.readline().split()
        team = int(a)
        b = b.split(':')
        time = 60 * int(b[0]) + int(b[1])

        l.append((team, time))

    for i in range(n):
        if f_score < s_score:
            s_time += l[i][1] - before_time
        elif f_score > s_score:
            f_time += l[i][1] - before_time

        if l[i][0] == 1:
            f_score += 1
        elif l[i][0] == 2:
            s_score += 1

        if f_score != s_score:
            before_time = l[i][1]

    if f_score < s_score:
        s_time += 48 * 60 - before_time
    elif f_score > s_score:
        f_time += 48 * 60 - before_time

    print("{:02d}:{:02d}".format(f_time//60, f_time%60))
    print("{:02d}:{:02d}".format(s_time//60, s_time%60))
