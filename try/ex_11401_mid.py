import sys
sys.setrecursionlimit(10**7)
DIV_NUM = 1000000007


def bio_co(input_n, input_k):

    if input_n - input_k == 1 or input_k == 1:
        return input_n

    if input_k <= 0:
        return 1

    return bio_co(input_n, input_k-1) * (input_n - input_k + 1) / input_k

if __name__ == "__main__":

    n, k = map(int, sys.stdin.readline().split())

    print(bio_co(n, k))