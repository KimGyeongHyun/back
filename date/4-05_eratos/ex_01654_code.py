from sys import stdin
input = stdin.readline

# 기존 문제 풀이는 start, end 를 mid 로 갱신했지만
# 그 대신 start = mid + 1, end = mid - 1 로 적용했다
# 그 결과 start = mid 의 경우인 무한루프가 발생하지 않으며
# 무한루프로 인한 추가 조건 연산이 들어가지 않는다
# 또한 zerodivision 은 start = 1 로 잡아 해결했다
# while 문에서 start <= end 의 조건을 걸어
# 문제의 조건을 만족하면서 while 문을 자연스럽게 빠져 나오도록 했다

if __name__ == "__main__":

    # 총 랜선 갯수, 필요한 랜선 갯수
    k, n = map(int, input().split())
    # 랜선 길이 리스트 자료형으로 저장
    d = list()
    for _ in range(k):
        d.append(int(input()))

    len = 0
    s = 1
    e = max(d)

    # 이분법 적용
    while s <= e:
        mid = (s + e) // 2
        count = 0

        # 랜선 갯수 구함
        for i in range(k):
            count += d[i] // mid

        if count >= n:  # 조건에 맞으면
            s = mid + 1     # 그 이상의 길이에도 적용해보기
            len = max(len, mid)     # 해당 조건을 일단 정답으로 적용
        else:   # 조건에 맞지 않으면
            e = mid - 1     # mid 는 조건에 무조건 없으므로 mid - 1을 end 에 적용

    print(len)