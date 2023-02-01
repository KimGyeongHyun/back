if __name__ == "__main__":
    N, M = map(int, input().split())

    if 3 <= M <= N:
        print('OLDBIE!')
    elif M <= 2:
        print('NEWBIE!')
    else:
        print('TLE!')
