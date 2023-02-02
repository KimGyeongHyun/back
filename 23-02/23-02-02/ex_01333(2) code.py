if __name__ == "__main__":
    N, L, D = map(int, input().split())

    t = 0

    # t가 앨범 끝까지 갈 때까지 반복
    while t < N * (L + 5):
        # L + 5 영역에서 뒤쪽 5초 영역 안에 있다면
        if t % (L + 5) >= L:
            break   # 반복을 중단하고 현재 시간을 출력
        t += D

    print(t)