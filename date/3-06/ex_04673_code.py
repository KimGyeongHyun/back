def d(n):
    sum = n
    while n:
        sum += n % 10
        n //= 10
    return sum


# 오래 걸리지만 단순한 방법
def has_creator(n):
    for i in range(n-1, 0, -1):
        if d(i) == n:
            return True
    return False


if __name__ == "__main__":
    for i in range(1, 10001):
        if not has_creator(i):
            print(i)