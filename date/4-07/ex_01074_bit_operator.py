def get(n, r, c, s):
    if n == 1:
        return s + 2 * r + c

    # 2의 제곱 표현대신 비트 연산자 표현
    step = (1 << (n-1)) * (1 << (n-1))
    # 4개의 영역 중 어디 있는지만 알면 된다
    # r, c의 n번째 비트만 확인하면 된다
    # nr, nc 는 0, 1 로 표현됨
    nr, nc = r >> (n-1), c >> (n-1)
    # 더해지는 값 재귀적 갱신
    ns = s + step * (2 * nr + nc)

    # r, c 가 반 이상이었다면 제일 상단의 비트 1 제거
    if nr == 1:
        r -= 1 << (n-1)
    if nc == 1:
        c -= 1 << (n-1)


n, r, c = map(int, input().split())
print(get(n, r, c, 0))

