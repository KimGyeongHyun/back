import sys
input = sys.stdin.readline


def GCD(a, b):

    # 최대공약수 구할 때 유클리드 호제법을 많이 사용
    # GCD(a, b) = GCD(b, a%b)
    # 즉 b가 0이 될 때까지 반복, 그 때 a의 값이 최대공약수
    if b==0:
        return a
    else:
        return GCD(b, a%b)


if __name__ == "__main__":
    c = int(input())

    for _ in range(c):
        n = int(input())
        count = 2 * n + 1
        for i in range(2, n+1):
            for j in range(2, n+1):
                if GCD(i, j) == 1:
                    count += 1

        print(count)