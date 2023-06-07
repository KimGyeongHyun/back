from sys import stdin

count = 0
flag = True

# 각 연결 요소가 트리인지 확인하고 총 트리의 갯수를 출력하는 문제

# dfs 로 모든 요소를 돌면서 트리의 갯수를 셀 수 있다

# 1. 사이클 확인하기 전 주의사항
#   visit 을 활용할 때 간선이 양방향이므로 이전에 출발했던 노드로 다시 돌아가지 않도록 해야 한다
#   (이전 노드를 확인하기 위해 dfs 메소드에서 before 매개변수를 사용)

# 2. 사이클이 있을 때, 없을 때 데이터를 어떻게 처리할 지 구성
#   노드 하나에 대해 dfs 를 수행하면 모든 연결 요소를 돌게 된다
#   모든 노드를 돌고 사이클이 존재하지 않으면 트리 개수 + 1,
#   중간에 사이클이 나오면 무시한다

#   구성하기 전 정리
#   1) dfs 를 돌다가 사이클을 발견하면 즉시 dfs 를 종료한다
#   중간에 dfs 를 종료하기 때문에 다른 노드가 해당 연결 요소에 접근할 수 있다
#   2) 사이클이 없다면 해당 연결 요소를 모두 순회한다
#   연결 요소의 모든 노드를 돌기 때문에
#   해당 연결 요소 밖에 다른 노드는 해당 연결 요소에 접근할 수 없다 (트리)
#   3) dfs 를 돌다가 이미 방문한 노드를 방문했다면 해당 연결 요소는 사이클을 가진다
#   노드는 트리에 도달할 수 없다 (2번 정리)
#   즉, 사이클이 존재하는 연결 요소에만 도달할 수 있다 (1번 정리)
#   따라서 해당 연결 요소는 사이클이므로 즉시 dfs 를 종료한다
#   4) dfs 를 강제 종료했을 때는 트리를 세지 않고, 모두 돌았을 때는 트리를 센다
#   dfs 시작 전 dfs 를 강제 종료하지 않았다는 것을 나타내는 flag 변수를 True 로 설정
#   dfs 메소드에서 강제 종료 시 해당 flag 를 False 로 설정한다
#   만약 강제 종료하지 않았다면 flag 변수를 True 상태로 유지한다
#   flag 에 따라 트리 개수를 갱신한다


def dfs(data, before, g, visit):

    if visit[data] is True:
        global flag
        flag = False
        return

    visit[data] = True

    for end in g[data]:
        if end == before:
            continue
        dfs(end, data, g, visit)


if __name__ == "__main__":

    case = 1

    while True:
        n, m = map(int, stdin.readline().split())
        if n == 0 and m == 0:
            break
        g = [[] for _ in range(n+1)]
        for _ in range(m):
            a, b = map(int, stdin.readline().split())
            g[a].append(b)
            g[b].append(a)

        visit = [False for _ in range(n+1)]
        count = 0

        for i in range(1, n+1):
            flag = True
            dfs(i, 0, g, visit)

            if flag:
                count += 1

        print("Case {}: ".format(case), end='')

        if count == 0:
            print("No trees.")
        elif count == 1:
            print("There is one tree.")
        else:
            print("A forest of {} trees.".format(count))

        case += 1