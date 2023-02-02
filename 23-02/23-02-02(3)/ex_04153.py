def sort(a, b, c):

    if a >= b and a >= c:
        return b, c, a
    elif b >= c:
        return a, c, b
    else:
        return a, b, c



if __name__ == "__main__":
    while True:
        ga, gb, gc = map(int, input().split())

        if ga==0 and gb==0 or gc==0:
            break

        a, b, c = sort(ga, gb, gc)

        if a**2 + b**2 == c**2:
            print('right')
        else:
            print('wrong')
