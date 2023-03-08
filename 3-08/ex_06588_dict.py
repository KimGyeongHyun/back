from sys import stdin
import time


if __name__ == "__main__":

    prime_dict = {i: True for i in range(3, 1000001, 2)}

    for i in range(3, 1001, 2):
        if prime_dict[i] is True:
            for j in range(3 * i, 1000001, 2 * i):
                prime_dict[j] = False

    start = time.time()
    count = 1

    while count <= 100000:
    # while True:

        # n = int(stdin.readline())
        n = 1000000

        if n == 0:
            break

        odd = 3

        while odd <= n // 2:
            if prime_dict[odd] and prime_dict[n-odd]:
                print("{} = {} + {}".format(n, odd, n - odd))
                break
            odd += 2

        if n // 2 < odd:
            print("Goldbach's conjecture is wrong.")

        count += 1

    print(time.time()-start)
