from sys import stdin

if __name__ == "__main__":

    t = int(stdin.readline())

    for _ in range(t):
        x, y = map(int, stdin.readline().split())

        # 이동 횟수 k 라고 했을 때 최대 거리 규칙
        # k, 최대 거리 규칙, 최대 거리
        # 1: 1 -> 1
        # 2: 1 1 -> 2
        # 3: 1 2 1 -> 4
        # 4: 1 2 2 1 -> 6
        # 5: 1 2 3 2 1 -> 9
        # 6: 1 2 3 3 2 1 -> 12
        # ...

        # k가 홀수인 경우 최대 거리는 (k//2 + 1)**2
        # k가 짝수인 경우 최대 거리는 k//2 * (k//2+1)

        # k가 홀수라고 가정, (k//2 + 1)**2 는 제곱식이기 때문에 쉽게 근사값을 찾을 수 있다
        # y - x <= (k//2 + 1)**2 인 경우 중 k가 최소인 홀수를 먼저 찾는다
        # (이동 거리) <= (이동 횟수 k의 최대 거리)

        # 1) 찾은 k가 y - x == (k//2 + 1)**2 를 만족한다면
        #   k를 계산하여 출력

        # 식을 만족하지 않는다면 (찾은 k가 y - x < (k//2 + 1)**2 를 만족한다면)
        # 2) 홀수인 k 대신 짝수인 k-1 을 만족하는지 확인해야 한다
        #   y - x <= ((k-1)//2 * ((k-1)//2 + 1)
        #   해당 식을 만족하면 k를 계산하여 출력
        # 3) 해당 식을 만족하지 않으면
        #   1) 식에서 k를 계산하여 출력

        temp = (y - x) ** (1 / 2)
        if temp % 1 == 0:  # 1)
            print(2 * int(temp) - 1)
        else:
            temp = int(temp)
            if y - x <= temp * (temp + 1):  # 2)
                print(2 * temp)
            else:  # 3)
                print(2 * temp + 1)