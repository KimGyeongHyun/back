if __name__ == "__main__":
    pyear, pmonth, pday = map(int, input().split())
    syear, smonth, sday = map(int, input().split())

    man = syear - pyear
    if pyear == syear:
        man = 0
    elif pmonth > smonth:
        man -= 1
    elif pmonth == smonth:
        if pday > sday:
            man -= 1

    sen = syear - pyear + 1

    yeon = syear - pyear

    print(man, sen, yeon)