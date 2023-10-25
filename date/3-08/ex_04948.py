from sys import stdin


def is_prime(n):
    """소수 판단"""

    if n == 1:
        return False

    for i in range(2, int(n**(1/2)//1) + 1):
        if n%i == 0:
            return False

    return True


def get_number_of_prime(n):
    """n 초과 2n 이하 소수 갯수 반환"""
    count = 0
    for i in range(n+1, 2*n+1):
        if is_prime(i):
            count += 1

    return count


if __name__=="__main__":
    while True:
        n = int(stdin.readline())
        if n == 0:
            break

        print(get_number_of_prime(n))
