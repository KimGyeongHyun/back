from sys import stdin


if __name__ == "__main__":
    w, h = map(int,stdin.readline().split())
    x, y = map(int,stdin.readline().split())
    t = int(stdin.readline())

    tx = x + t
    ty = y + t

    tx %= 2*w
    ty %= 2*h

    if tx > w:
        tx = 2*w - tx
    if ty > h:
        ty = 2*h - ty

    print(tx, ty)