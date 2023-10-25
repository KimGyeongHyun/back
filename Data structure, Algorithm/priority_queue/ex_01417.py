from sys import stdin
import heapq

# 풀이

# 1) 정렬한 다음 다른 사람 중 득표가 제일 많은 사람의 표부터 시작한다
#   다솜이가 해당 사람의 득표보다 높아질 때까지 표를 한꺼번에 매수한다
#   문제는 표를 사다가 다른 사람의 득표가 더 높아지는 것을 고려하지 못한다
#   ex) 예제1
#   즉 한꺼번에 매수할 수 없고 계속 비교하며 하나씩 매수해야 한다

# 2) 매수를 하나씩 하면서 우선순위 큐에 갱신한다
#   삽입과 추출을 많이 하면서 정렬 상태를 유지하려면 리스트보다 우선순위 큐를 사용하는 것이 시간복잡도 상으로 유리하다
#   처음 득표수를 모아 정렬하는 것은 리스트, 우선순위 큐 둘다 nlog(n)
#   삭제, 삽입, 정렬의 과정 -> 리스트는 nlog(n), 우선순위 큐는 log(n)


if __name__ == "__main__":
    n = int(stdin.readline())
    dasom = int(stdin.readline())
    l = []

    for _ in range(n-1):
        heapq.heappush(l, -int(stdin.readline()))

    if not l:
        print(0)
        exit()

    count = 0

    while True:
        high = -heapq.heappop(l)

        if dasom > high:
            break

        count += 1; high -= 1; dasom += 1;
        heapq.heappush(l, -high)

    print(count)