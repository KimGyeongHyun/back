if __name__ == "__main__":
    n = int(input())

    for i in range(n):
        a, b, c = map(int, input().split())

        if a**2 + b**2 == c**2 or \
            b**2 + c**2 == a**2 or \
            c**2 + a**2 == b**2:
            right = True
        else:
            right = False

        print('Scenario #{}:'.format(i+1))
        if right:
            print('yes')
        else:
            print('no')

        if i != n:
            print()