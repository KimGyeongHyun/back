from sys import stdin


def GCD(a, b):

    # 최대공약수 구할 때 유클리드 호제법을 많이 사용
    # GCD(a, b) = GCD(b, a%b)
    # 즉 b가 0이 될 때까지 반복, 그 때 a의 값이 최대공약수
    if b==0:
        return a
    else:
        return GCD(b, a%b)


if __name__=="__main__":

    n = int(stdin.readline())

    for _ in range(n):
        a, b = map(int, stdin.readline().split())
        g = GCD(a, b)
        l = a * b // g
        print(l, g)