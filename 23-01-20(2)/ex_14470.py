if __name__ == "__main__":
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    if A <= B <= 0:
        print(C * (B-A))
    elif 0 <= A <= B:
        print(E * (B-A))
    else:
        print(A*C*-1 + D + B*E)
