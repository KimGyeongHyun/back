if __name__ == "__main__":
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    P = int(input())

    Y = B

    if P > C:
        Y += D * (P - C)

    print(min(A * P, Y))