import sys
input = sys.stdin.readline


# 배열에서 한 줄로 순환할 수열을 한 줄씩 뽑아옴
worm = []


if __name__ == "__main__":
    n, m, r = map(int, input().split())
    l = []
    for _ in range(n):
        l.append(list(map(int, input().split())))

    # worm 에 순환할 수열을 한 줄씩 뽑아 저장
    for i in range(min((n+1)//2, (m+1)//2)):
        t = []
        for j in range(m-1-(2*i)):
            t.append(l[i][i+j])

        for j in range(n-1-(2*i)):
            t.append(l[i+j][m-1-i])

        for j in range(m-1-(2*i), 0, -1):
            t.append(l[n-1-i][i+j])

        for j in range(n-1-(2*i), 0, -1):
            t.append(l[i+j][i])

        worm.append(t)

    # worm 안에 순환하는 수열을 각각 순환시킴
    for i in range(len(worm)):
        j = len(worm[i])
        repeat = r % j
        worm[i] = worm[i][repeat:] + worm[i][:repeat]

    # 순환을 마친 수열을 다시 배열에 저장
    for i in range(min((n+1)//2, (m+1)//2)):
        t = []
        count = 0

        for j in range(m-1-(2*i)):
            l[i][i+j] = worm[i][count]
            count += 1

        for j in range(n-1-(2*i)):
            l[i+j][m-1-i] = worm[i][count]
            count += 1

        for j in range(m-1-(2*i), 0, -1):
            l[n-1-i][i+j] = worm[i][count]
            count += 1

        for j in range(n-1-(2*i), 0, -1):
            l[i+j][i] = worm[i][count]
            count += 1

    # 배열 출력
    for line in l:
        for item in line:
            print(item, end=" ")
        print()