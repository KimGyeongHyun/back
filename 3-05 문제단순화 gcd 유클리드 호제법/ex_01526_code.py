from sys import stdin


def check(n):
    while n:
        if n % 10 != 7 and n % 10 != 4:
            return False
        n //= 10
    return True


if __name__=="__main__":
    n = int(stdin.readline())

    # n부터 시작해서 -1씩 감소
    # 금민수가 나올 때까지 반복
    for v in range(n, 0, -1):
        if check(v):
            print(v)
            break
