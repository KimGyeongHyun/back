if __name__ == "__main__":
    Br, Bc = map(int, input().split())
    Dr, Dc = map(int, input().split())
    Jr, Jc = map(int, input().split())

    JBr = Br - Jr if Br >= Jr else Jr - Br
    JBc = Bc - Jc if Bc >= Jc else Jc - Bc

    JDr = Dr - Jr if Dr >= Jr else Jr - Dr
    JDc = Dc - Jc if Dc >= Jc else Jc - Dc

    B_move = JBr if JBr >= JBc else JBc
    D_move = JDr + JDc

    if B_move < D_move:
        print('bessie')
    elif B_move == D_move:
        print('tie')
    else:
        print('daisy')