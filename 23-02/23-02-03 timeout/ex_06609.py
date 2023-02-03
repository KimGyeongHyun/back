if __name__ == "__main__":

    while True:
        try:
            # M : 모기
            # P : 번데기
            # L : 유충
            # E : 한 모기가 낳는 알의 수
            # R : 살아남는 유충 비율
            # S : 살아남는 번데기 비율
            # N : 모기 수 구하려는 시점 (N주 후)
            M, P, L, E, R, S, N = map(int, input().split())
        except EOFError:
            break

        M_number = 0

        if N % 3 == 0:
            M_number = M

        elif N % 3 == 1:
            M_number = P
            M_number //= S

        elif N % 3 == 2:
            M_number = L
            M_number //= R
            M_number //= S

        for _ in range(N // 3):
            M_number *= E
            M_number //= R
            M_number //= S

        print(M_number)
