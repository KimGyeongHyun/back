import sys
input = sys.stdin.readline

# 원점에서 보이는 배열을 초기화하여 안 보이는 곳을 False 로 바꾸는 방법을 사용하면
# 시간 초과가 발생하게 된다

# x 축을 기준으로 보면
# x 가 2일 때 y축 방향으로 원점에서 보이는 점이 False, True 가 반복됨을 확인
# 3일 때 False, True, True 가 반복
# 4일 때 False, True, False, True 가 반복
# 5일 때 False, True, True, True, True 반복
# 즉 x의 수만큼 규칙이 반복됨을 확인했다

# 해당 규칙을 리스트로 가져오고
# 리스트가 n 안에서 몇 번 반복하는지, 리스트 안에 True 가 몇개 있는지를 확인한다
# 위의 두 경우를 곱하면 반복되는 리스트의 True 갯수를 한꺼번에 구할 수 있다
# 즉 연산을 줄일 수 있다
# 위의 연산을 x축으로 n번 반복하여 원점에서 보이는 좌표의 개수를 구했다


def set_prime(n):
    """n까지의 소수 여부를 알려주는 리스트 반환"""
    a = [True for _ in range(n+2)]
    a[0] = False
    a[1] = False
    for i in range(2, int(n**(1/2)) + 1):
        if a[i] is True:
            for j in range(2 * i, n+2, i):
                a[j] = False

    return a


if __name__ == "__main__":

    c = int(input())

    for _ in range(c):
        n = int(input())
        count = 2 + n   # (0, 1), (1, 0), x=1 좌표 먼저 계산
        is_prime = set_prime(n)     # 소수 여부 리스트

        for i in range(2, n+1):     # i : x좌표
            # 세로 방향으로 반복하는 리스트
            # i 만큼 세로 방향으로 원점에서 보이는 여부가 반복하게 된다
            l = [True for _ in range(i+1)]

            # 반복하는 리스트 구현
            for j in range(2, i+1):
                if i % j == 0 and is_prime[j]:
                    for k in range(j, i+1, j):
                        l[k] = False

            # 리스트 안의 True 갯수
            true_count = 0
            for boolean in l[1:]:
                if boolean:
                    true_count += 1

            # 리스트 안의 True 개수 * 리스트 반복 횟수
            final_count = n // (len(l)-1) * true_count

            # 리스트 반복 이후 남은 좌표 하나씩 추가
            for i in range(n%(len(l)-1)):
                final_count += l[i+1]

            # x = i 좌표에서의 원점에서 보이는 점의 개수를 최종 개수에 더함
            count += final_count

        print(count)