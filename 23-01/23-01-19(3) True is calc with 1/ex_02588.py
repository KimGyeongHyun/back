if __name__ == "__main__":
    a = int(input())
    b = int(input())

    mul = a * b

    b1 = b % 10
    b = b // 10
    mul1 = a * b1

    b2 = b % 10
    b = b // 10
    mul2 = a * b2

    b3 = b
    mul3 = a * b3

    print(mul1)
    print(mul2)
    print(mul3)
    print(mul)