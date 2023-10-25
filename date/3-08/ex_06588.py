from sys import stdin

guess_n = None
first_prime = None
last_prime = None


def is_prime(n):
    """소수 판단"""

    for i in range(3, int(n**(1/2)) + 1, 2):
        if n%i == 0:
            return False

    return True


if __name__ == "__main__":

    while True:

        n = int(stdin.readline())

        if n == 0:
            break

        odd = 3

        while odd <= n//2:

            # n이 전과 같은 값이라면 전의 값을 그대로 출력한다
            if n == guess_n:
                print("{} = {} + {}".format(guess_n, first_prime, last_prime))
                break

            if is_prime(odd) and is_prime(n - odd):
                print("{} = {} + {}".format(n, odd, n-odd))
                guess_n = n
                first_prime = odd
                last_prime = n - odd
                break
            odd += 2

        if n//2 < odd:
            print("Goldbach's conjecture is wrong.")