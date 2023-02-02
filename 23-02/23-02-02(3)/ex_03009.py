if __name__ == "__main__":
    aa, ab = map(int, input().split())
    ba, bb = map(int, input().split())
    ca, cb = map(int, input().split())

    da, db = 0, 0

    if aa == ba:
        da = ca
    elif aa == ca:
        da = ba
    else:
        da = aa

    if ab == bb:
        db = cb
    elif ab == cb:
        db = bb
    else:
        db = ab

    print(da, db)
