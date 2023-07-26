import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# 기본적인 알고리즘
# 비행기가 gi 게이트에 도킹을 시도하려 할 때
# gi 이하의 도킹할 수 있는 게이트 중 제일 큰 게이트에 도킹해야 함

# 작동 방식
# 게이트를 0 ~ 10**5 까지 구성
# 분리 집합 알고리즘 사용
# 게이트 인덱스를 분리 집합으로 구성
# 부모 : 비행기 도킹을 요청할 게이트
# 처음 도킹을 요청할 게이트는 자기 자신

# x : x번 게이트
# par_x : x번 게이트에서 도킹을 요청할 게이트 (x의 부모)

# par_x == x 라면 x번 게이트는 아직 비행기가 도킹되어 있지 않음
# par_x == x-1 이라면 x번 게이트는 도킹되어 있다는 의미, x-1번 게이트는 확인이 필요

# 1. x번 게이트가 도킹을 요청하는 게이트가 자기 자신일 경우 (x번 게이트에 비행기가 없을 때)
# x 에서 도킹을 요청할 게이트를 x-1 로 설정 (par_x = x-1)

# 2. x번 게이트에 도킹을 요청할 때 par_x 가 본인이 아닌 경우
# find(x) == x 인 곳까지 도킹을 요청하게 된다
#   도킹을 요청하는 게이트를 찾는 행위는 x번 게이트 -> x-1번 게이트 -> x-2번 게이트 ... 의 형태처럼
#   도킹을 요청하는 게이트가 자기 자신일 때까지 요청하는 행위를 말함
# 이 때를 만족하는 x를 y라고 할 때
# y번 게이트에 도킹을 요청할 게이트를 y-1 로 설정한다

# 3. x번 게이트에서 도킹할 게이트를 요청했을 때 0번 게이트가 나왔다면
# 1 ~ x번 까지 비행기가 모두 도킹해 있다는 의미이므로 도킹이 불가능하므로 종료한다

# 도킹을 요청할 게이트를 찾는 find() 함수 최적화
# x에서 도킹을 요청할 게이트는 자기 자신이 아니라면 x-1 밖에 안 되지만
# find(x) = par_x 라면 par_x+1 ~ x 까지 비행기가 도킹되어 있는 것이고,
# par_x번 게이트에 비행기가 없다는 의미이다
# 따라서 x에서 도킹을 요청할 게이트를 x-1 대신 par_x 로 설정할 수 있다


def find(x):
    # x번 게이트에서 도킹을 요청할 게이트를 찾아 리턴
    if par[x] == x:
        return x
    par[x] = find(par[x])    # find() 함수 최적화
    return par[x]


def union(x):
    # x번 게이트에 도킹 요청, 부모 관계 설정
    # 도킹할 게이트가 없다면 전역변수 flag = True 설정 후 함수 종료

    par_x = find(x)

    # 1.
    if par_x == x:
        par[x] = x-1
        return

    # 3.
    if par_x == 0:
        global flag
        flag = True
        return

    # 2.
    par[par_x] = par_x - 1


if __name__ == "__main__":
    g = int(input())
    p = int(input())
    par = [i for i in range(g+1)]
    flag = False
    count = 0
    for _ in range(p):
        union(int(input()))
        if flag:
            break
        count += 1

    print(count)
