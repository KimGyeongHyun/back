import math

if __name__ == "__main__":
    L = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())

    print(L - max(math.ceil(A / C), math.ceil(B / D)))