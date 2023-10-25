from sys import stdin


if __name__ == "__main__":
    n = int(stdin.readline())
    l = list(map(int, stdin.readline().split()))
    a = [0 for _ in range(n)]

    # a는 사람을 배치할 n길이의 0으로 이루어진 리스트 (사람의 키를 value 로 설정)

    # 키가 1인 사람의 경우
    # 모든 사람이 본인보다 키가 크므로 자기 앞에 키가 큰 사람들 수만큼 뒤에 배치시키면 된다

    # 키가 2인 사람의 경우
    # 키가 1인 사람을 제외한 나머지 사람들은 본인보다 키가 크다
    # 즉 a 리스트 내부의 0인 곳은 본인보다 큰 사람이 있다는 의미이다
    # 본인보다 키가 큰 사람의 수만큼 0을 지나서 배치시키면 된다

    # 키가 3 이상인 사람의 경우도 마찬가지로
    # a 리스트 내부의 0인 곳은 본인보다 큰 사람이 있다는 의미이므로
    # 키가 2인 사람처럼 0을 세며 배치시키면 된다

    for i in range(n):
        front_number = l[i]     # 앞의 사람 수
        count_front = 0         #
        for j in range(n):
            if a[j] == 0:
                if count_front == front_number:
                    a[j] = i + 1
                    break
                count_front += 1

    for height in a:
        print(height, end=' ')
