from sys import stdin


def scale():
    a, b, c, d, e, f, g, h = map(int, stdin.readline().split())
    if a==1 and b==2 and c==3 and d==4 and e==5 and f==6 and g==7 and h==8:
        print("ascending")
    elif a==8 and b==7 and c==6 and d==5 and e==4 and f==3 and g==2 and h==1:
        print("descending")
    else:
        print("mixed")


if __name__ == "__main__":
    scale()
