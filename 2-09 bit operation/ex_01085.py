if __name__ == "__main__":
    x, y, w, h = map(int, input().split())

    if 2 * x >= w:
        x_len = abs(x - w)
    else:
        x_len = abs(x)

    if 2 * y >= h:
        y_len = abs(y - h)
    else:
        y_len = abs(y)

    print(min(x_len, y_len))