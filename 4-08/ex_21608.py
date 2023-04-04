import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    # 교실
    l = [[0 for _ in range(n+1)] for _ in range(n+1)]
    # key : 학생 숫자, value : 선호 학생 4명 리스트
    fav_dict = {}
    
    for _ in range(n*n):
        fav = list(map(int, input().split()))
        num = fav[0]
        fav_dict[num] = fav[1:]

        # 좋아하는 주변 학생 수
        one = 0
        # 좋아하는 주변 학생 수가 같을 때 좌표값을 저장할 리스트
        onel = []
        for x in range(1, n+1):
            for y in range(1, n+1):

                if l[x][y] != 0:
                    continue

                t_one = 0

                if 2 <= x and (l[x-1][y] in fav[1:]):
                    t_one += 1
                if x <= n-1 and (l[x+1][y] in fav[1:]):
                    t_one += 1
                if y <= n-1 and (l[x][y+1] in fav[1:]):
                    t_one += 1
                if 2 <= y and (l[x][y-1] in fav[1:]):
                    t_one += 1
                if one < t_one:
                    one = t_one
                    onel = [(x, y)]
                elif t_one == one:
                    onel.append((x, y))

        # 주변에 좋아하는 학생 수의 최대값 좌표가 한 개라면 그대로 배치하고 종료
        if len(onel) == 1:
            l[onel[0][0]][onel[0][1]] = num
            continue

        # 첫번째 조건을 만족하는 좌표가 2개 이상 있을 경우
        # 해당 좌표들을 2번째 조건으로 비교

        # 주변 공백 자리의 수
        two = 0
        # 좌표
        twol = (0, 0)
        for x, y in onel:

            t_two = 0
            if 2 <= x and l[x-1][y] == 0:
                t_two += 1
            if x <= n-1 and l[x+1][y] == 0:
                t_two += 1
            if 2 <= y and l[x][y-1] == 0:
                t_two += 1
            if y <= n-1 and l[x][y+1] == 0:
                t_two += 1

            if twol == (0, 0):
                two = t_two
                twol = (x, y)

            # 주변 공백 자리가 많을 때만 좌표값 갱신
            # 공백 자리의 개수가 같을 때는 가장 작은 y, 가장 작은 x 로 유지
            if two < t_two:
                two = t_two
                twol = (x, y)

        l[twol[0]][twol[1]] = num

    fav_sum = 0
    for x in range(1, n+1):
        for y in range(1, n+1):
            f_count = 0
            fav_l = fav_dict[l[x][y]]
            if 2 <= x and (l[x - 1][y] in fav_l):
                f_count += 1
            if x <= n - 1 and (l[x + 1][y] in fav_l):
                f_count += 1
            if y <= n - 1 and (l[x][y + 1] in fav_l):
                f_count += 1
            if 2 <= y and (l[x][y - 1] in fav_l):
                f_count += 1

            if f_count == 0:
                continue
            fav_sum += 10 ** (f_count-1)

    print(fav_sum)