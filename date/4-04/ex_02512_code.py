from sys import stdin


if __name__ == "__main__":

    # 각 지방에서의 요청 예산 금액이 오름차순 정렬 되어있다면
    # 앞의 리스트 값부터 비교하여 몇 번째 지방까지 요청 예산 금액을 모두 줄 수 있는지를 쉽게 구할 수 있다
    # 따라서 모든 예산 금액을 줄 수 있는 지방의 인덱스를 구한 후
    # 그에 해당하는 상한선을 구하면 된다

    n = int(stdin.readline())
    needs = list(map(int, stdin.readline().split()))
    budget = int(stdin.readline())
    needs.sort()    # 정렬

    # 인덱스 찾기
    s = 0   # 인덱스
    while True:
        sum = 0
        for i in range(s):
            sum += needs[i]
        sum += needs[s] * (n - s)
        s += 1
        if sum > budget or s == n:
            break

    # 상한선 찾기
    if s == 1:
        print(budget // n)
    else:
        s -= 1
        for i in range(s):
            budget -= needs[i]
        if s == n - 1 and budget > needs[s]:
            print(needs[s])
        else:
            print(budget // (n - s))