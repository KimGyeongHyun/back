if __name__ == "__main__":
    aa, ab, ac, ad = map(int, input().split())
    ba, bb, bc, bd = map(int, input().split())

    a = aa + ab + ac + ad
    b = ba + bb + bc + bd

    print(a if a >= b else b)