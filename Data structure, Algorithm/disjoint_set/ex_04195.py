import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def find(n):
    """분리 집합 루트 노드 반환"""

    if fr_par[n] == n:
        return n
    fr_par[n] = find(fr_par[n])
    return fr_par[n]


def union(x, y):
    """
    분리 집합 두 친구관계 연결\n
    처음 보는 친구가 있다면 딕셔너리에 추가\n
    루트 노드에 친구수 저장
    """
    # 분리 집합 루트 노드 dp 선행 문제 풀이
    # http://boj.kr/9240f25b99e84f0994457bd54e944f3b

    # 처음 보는 친구 추가
    if x not in fr_par.keys():
        fr_par[x] = x
        fr_num[x] = 1
    if y not in fr_par.keys():
        fr_par[y] = y
        fr_num[y] = 1

    x = find(x)
    y = find(y)

    # 같은 분리 집합이면 친구수 출력
    if x == y:
        print(fr_num[x])
        return

    fr_par[y] = x               # 친구 추가
    fr_num[x] += fr_num[y]      # 분리 집합의 친구수를 갱신
    print(fr_num[x])            # 분리 집합 친구수 출력


if __name__ == "__main__":

    c = int(input())
    for _ in range(c):

        # 딕셔너리를 사용해 처음 나오는 친구를 유동적으로 추가
        fr_par = {}     # 부모 친구
        fr_num = {}     # 친구수

        f = int(input())
        for _ in range(f):
            a, b = input().split()
            union(a, b)