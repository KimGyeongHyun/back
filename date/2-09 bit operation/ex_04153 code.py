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

        # 아래처럼 sort 할 필요 없이 세 가지 경우로 if 취하면 된다
        a, b, c = sort(ga, gb, gc)

        if a**2 + b**2 == c**2:
            print('right')
        else:
            print('wrong')
