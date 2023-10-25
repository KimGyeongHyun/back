# BFS 로도 풀 수 있지만 리스트를 이용해서 풀 수도 있다
# BFS 계산보단 조금 느렸다

if __name__ == "__main__":
    x = int(input())
    # key : 해당 숫자, value : 해당 숫자까지 필요한 계산 수
    num_count = [0 for _ in range(x+1)]

    for i in range(2, x+1):
        num_count[i] = num_count[i-1] + 1
        if i%2 == 0:
            num_count[i] = min(num_count[i//2] + 1, num_count[i])

        if i%3 == 0:
            num_count[i] = min(num_count[i//3] + 1, num_count[i])

    print(num_count[x])