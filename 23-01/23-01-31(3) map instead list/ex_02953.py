if __name__ == "__main__":
    a = sum(map(int, input().split()))
    b = sum(map(int, input().split()))
    c = sum(map(int, input().split()))
    d = sum(map(int, input().split()))
    e = sum(map(int, input().split()))

    if a>b and a>c and a>d and a>e:
        print(1, a)
    elif b>c and b>d and b>e:
        print(2, b)
    elif c>d and c>e:
        print(3, c)
    elif d>e:
        print(4, d)
    else:
        print(5, e)